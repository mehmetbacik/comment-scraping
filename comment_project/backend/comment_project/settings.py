# Scrapy settings for comment_project project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import random
from faker import Faker

fake = Faker()

def get_random_user_agent():
    return fake.user_agent()

import requests

def get_proxies():
    # Free Proxy List URL
    url = "#"
    response = requests.get(url)
    proxies = []
    return proxies


def get_random_proxy(proxies):
    return random.choice(proxies)


BOT_NAME = "comment_project"

SPIDER_MODULES = ["comment_project.spiders"]
NEWSPIDER_MODULE = "comment_project.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# DOWNLOAD_DELAY = 3

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Enable or disable spider middlewares
# SPIDER_MIDDLEWARES = {
#     "comment_project.middlewares.CommentProjectSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": 110,
    "comment_project.middlewares.RandomProxyMiddleware": 100,
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
    "comment_project.middlewares.RandomUserAgentMiddleware": 200,
    'comment_project.middlewares.SeleniumMiddleware': 543,
}

# Proxy list - Free Proxy List
PROXIES = [
    "http://ip1:port",
    "http://ip2:port",
    "http://ip3:port",
    # Daha fazla proxy ekleyebilirsiniz
]

# User-Agent list
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
    'Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0',
    # Daha fazla User-Agent ekleyebilirsiniz
]

# Random Proxy Middleware
class RandomProxyMiddleware:
    def process_request(self, request, spider):
        request.meta['proxy'] = get_random_proxy(PROXIES)

# Random User-Agent Middleware
class RandomUserAgentMiddleware:
    def process_request(self, request, spider):
        request.headers['User-Agent'] = get_random_user_agent()

# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

FEED_FORMAT = 'json'
FEED_URI = 'output/reviews.json'

# Enable and configure HTTP caching (disabled by default)
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Enable extensions if needed
# EXTENSIONS = {
#     "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Enable AutoThrottle extension if needed
# AUTOTHROTTLE_ENABLED = True
# AUTOTHROTTLE_START_DELAY = 5
# AUTOTHROTTLE_MAX_DELAY = 60
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# AUTOTHROTTLE_DEBUG = False

# Enable and configure item pipelines (disabled by default)
# ITEM_PIPELINES = {
#     "comment_project.pipelines.CommentProjectPipeline": 300,
# }
