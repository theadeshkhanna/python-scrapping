import requests
from bs4 import BeautifulSoup
import os
from retrying import retry
from cache import Cache

class Scraper:
    def __init__(self, pages=None, proxy=None):
        self.base_url = "https://dentalstall.com/shop/"
        self.pages = pages
        self.proxy = proxy
        self.cache = Cache()

    @retry(wait_fixed=2000, stop_max_attempt_number=3)
    def get_page(self, url):
        proxies = {"http": self.proxy, "https": self.proxy} if self.proxy else None
        response = requests.get(url, proxies=proxies)
        response.raise_for_status()
        return response.text

    def parse_page(self, page_content):
        soup = BeautifulSoup(page_content, "html.parser")
        products = []
        for item in soup.select('.product-item'):
            title = item.select_one('.product-title').get_text()
            price = item.select_one('.price').get_text()
            img_url = item.select_one('.product-image img')['src']
            img_path = self.download_image(img_url)
            products.append({"product_title": title, "product_price": price, "path_to_image": img_path})
        return products

    def download_image(self, url):
        response = requests.get(url)
        filename = os.path.basename(url)
        filepath = os.path.join("images", filename)
        with open(filepath, "wb") as f:
            f.write(response.content)
        return filepath

    def scrape(self):
        scraped_data = []
        for page_num in range(1, (self.pages or 100) + 1):
            page_url = f"{self.base_url}page/{page_num}/"
            page_content = self.get_page(page_url)
            products = self.parse_page(page_content)
            for product in products:
                if not self.cache.is_cached(product["product_title"], product["product_price"]):
                    scraped_data.append(product)
                    self.cache.update_cache(product["product_title"], product["product_price"])
        return scraped_data

