from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


class LazadaScraper:
    def __init__(self):
        # Initialize the WebDriver
        os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(options=chrome_options)

    def find_price_and_name(self, url):
        try:
            # Step 1: Open Lazada homepage
            self.driver.get("https://www.lazada.co.th/")
            time.sleep(2)  # Wait for the homepage to load

            # Step 2: Navigate to the target product URL
            self.driver.get(url)
            time.sleep(2)  # Wait for the product page to load

            # Scroll to the price element
            price_element = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "pdp-price_color_orange")
                )
            )
            actions = ActionChains(self.driver)
            actions.move_to_element(price_element).perform()

            # Wait for the price element to be visible
            WebDriverWait(self.driver, 3).until(EC.visibility_of(price_element))
            price = price_element.text.strip()

            # Get the product name
            name_element = self.driver.find_element(
                By.CLASS_NAME, "pdp-mod-product-badge-title"
            )
            name = name_element.text.strip()
            
            
            ratings_element = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, ".pdp-review-summary__link")
                    )
                )

            rating = ratings_element.text.split(" ")[0]
            price = float(price.replace("฿", "").replace(",", "").strip())

            return name, price , rating

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

    def find_many(self, urls):
        results = []
        try:
            # Step 1: Open Lazada homepage
            self.driver.get("https://www.lazada.co.th/")
            time.sleep(2)  # Wait for the homepage to load

            # Step 2: Navigate to the target product URL
            for url in urls:
                self.driver.get(url)
                time.sleep(2)  # Wait for the product page to load

                # Scroll to the price element
                price_element = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located(
                        (By.CLASS_NAME, "pdp-price_color_orange")
                    )
                )
                actions = ActionChains(self.driver)
                actions.move_to_element(price_element).perform()

                # Wait for the price element to be visible
                WebDriverWait(self.driver, 3).until(EC.visibility_of(price_element))
                price = price_element.text.strip()

                # Get the product name
                name_element = self.driver.find_element(
                    By.CLASS_NAME, "pdp-mod-product-badge-title"
                )
                name = name_element.text.strip()

                # Get the product rating
                ratings_element = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, ".pdp-review-summary__link")
                    )
                )

                ratings_text = ratings_element.text.split(" ")[0]
                price = float(price.replace("฿", "").replace(",", "").strip())

                results.append(
                    {"name": name, "price": price, "url": url, "rating": ratings_text}
                )
                print(f"Scraped: {name} - {price} - {ratings_text} rating")

            return results

        except Exception as e:
            print(f"Error scraping {url}: {e}")
            return []


# Example Usage
if __name__ == "__main__":
    urls = [
        "https://www.lazada.co.th/products/razer-black-shark-v2-gaming-headset-with-microphone-headphone-i2852515507-s10405410866.html",
        "https://www.lazada.co.th/products/-i4994538597-s21073262330.html",
    ]

    scraper = LazadaScraper()
    scraper.find_many(urls)
    # data = scraper.scrape_urls(urls)
    # print("Scraping Results:", data)
    scraper.close()
