import scrapy

class CommentSpider(scrapy.Spider):
    name = "comment_spider"
    allowed_domains = ["web-site-url.com"]
    start_urls = ["https://web-site-url.com/"]

    def parse(self, response):
        """
        It retrieves all product links from the product listing page.
        """
        product_links = response.css('a.product-link::attr(href)').getall()
        for link in product_links:
            product_url = response.urljoin(link)
            yield scrapy.Request(product_url, callback=self.parse_product)

        # Pagination control
        next_page = response.css('a.next-page::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_product(self, response):
        """
        It retrieves information from the product detail page.
        """
        product_name = response.css('h1.product-title::text').get()
        product_price = response.css('.product-price::text').get()
        product_id = response.url.split('-p-')[-1].split('?')[0]  # Get product ID from URL

        comments_url = f"https://web-site-url.com/product/{product_id}/comments"
        
        yield scrapy.Request(
            comments_url,
            callback=self.parse_comments,
            meta={"product_name": product_name, "product_price": product_price, "product_id": product_id}
        )

    def parse_comments(self, response):
        """
        It pulls reviews and combines them with product information.
        """
        product_name = response.meta["product_name"]
        product_price = response.meta["product_price"]
        product_id = response.meta["product_id"]

        comments = response.css('.comment-text::text').getall()

        yield {
            "product_id": product_id,
            "product_name": product_name,
            "product_price": product_price,
            "comments": comments
        }
