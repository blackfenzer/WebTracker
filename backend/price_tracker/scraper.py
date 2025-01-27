from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


class LazadaScraper:
    def __init__(self):
        # Initialize the WebDriver
        self.driver = webdriver.Chrome()

    def find_price_and_name(self, url):
        try:
            self.driver.get(url)
            time.sleep(5)
            # Wait for the price element
            div = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "pdp-product-price"))
            )
            span = div.find_element(By.TAG_NAME, "span")

            # Wait for the name element
            h1 = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "pdp-mod-product-badge-title")
                )
            )

            name = h1.text
            price = span.text
            return name, price

        except Exception as e:
            print(f"Error scraping {url}: {e}")
            return None, None

    def scrape_urls(self, urls):
        results = []
        for url in urls:
            name, price = self.find_price_and_name(url)
            if name and price:
                results.append({"name": name, "price": price, "url": url})
                print(f"Scraped: {name} - {price}")
            else:
                print(f"Failed to scrape: {url}")
        return results

    def close(self):
        # Close the browser
        self.driver.quit()


# Example Usage
if __name__ == "__main__":
    urls = [
        "https://www.lazada.co.th/products/razer-viper-v2-pro-ultra-lightweight-wireless-esports-mouse-i3720495469-s14096543251.html",
        "https://www.lazada.co.th/products/razer-pro-type-ultra-wireless-mechanical-keyboard-en-100-2-i3850169118-s14694667845.html",
    ]

    scraper = LazadaScraper()
    data = scraper.scrape_urls(urls)
    print("Scraping Results:", data)
    scraper.close()
