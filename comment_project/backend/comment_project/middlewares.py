from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from scrapy.http import HtmlResponse
import time

class SeleniumMiddleware:
    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    def process_request(self, request, spider):
        self.driver.get(request.url)
        time.sleep(2)  # Wait for the page to load

        # Page scrolling (For dynamic loading)
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        html = self.driver.page_source
        return HtmlResponse(url=request.url, body=html, encoding='utf-8', request=request)

    def __del__(self):
        self.driver.quit()
