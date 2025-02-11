import scrapy
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

class CommentSpider(scrapy.Spider):
    name = "comment_spider"
    allowed_domains = ["web-site-url.com"]
    start_urls = ["https://web-site-url.com/"]

    def __init__(self):
        """
        Selenium start
        """
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    def parse(self, response):
        """
        It retrieves product links from the product listing page and scrolls the page for dynamic loading.
        """
        self.driver.get(response.url)
        time.sleep(2)  # Wait for the page to load

        # Scroll the page to capture dynamically loaded products
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Wait for new products to load
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # Get the HTML content of the page
        page_source = self.driver.page_source
        sel_response = HtmlResponse(url=response.url, body=page_source, encoding='utf-8')
        product_links = sel_response.css('a.product-link::attr(href)').getall()

        for link in product_links:
            product_url = response.urljoin(link)
            yield scrapy.Request(product_url, callback=self.parse_product)

    def parse_product(self, response):
        """
        Click on the 'All Comments' button on the product detail page and be directed to the comments page.
        """
        self.driver.get(response.url)
        time.sleep(2)

        try:
            # Click on the "All Comments" button
            comments_button = self.driver.find_element(By.CLASS_NAME, "navigate-all-reviews-btn")
            comments_button.click()
            time.sleep(2)

            # Get the comments page URL
            comments_url = self.driver.current_url
            self.log(f"Redirecting to the comments page: {comments_url}")
            yield scrapy.Request(comments_url, callback=self.parse_comments)

        except Exception as e:
            self.log(f"Error redirecting to comments page: {e}")

    def parse_comments(self, response):
        """
        Pulls comments from the comments page.
        """
        comments = response.css('.review-comment::text').getall()
        yield {
            "comments": comments
        }

    def __del__(self):
        """
        When Spider is closed, close Selenium driver.
        """
        self.driver.quit()
