from django.test import TestCase
from .models import TrackedItem, PriceHistory
from .scraper import ShopeeScraper
from unittest.mock import MagicMock, patch
from selenium.webdriver.common.by import By


class ShopeeScraperTestCase(TestCase):
    def setUp(self):
        # Mock data setup, if needed
        self.scraper = ShopeeScraper()

    @patch("selenium.webdriver.Chrome")
    def test_scraper_initialization(self):
        # Test scraper initialization
        self.assertIsNotNone(self.scraper)

    def test_scraper_get_price(self):
        # Mock a WebElement for testing
        mock_driver = MagicMock()
        mock_element = MagicMock()
        mock_element.text = "฿100"
        mock_driver.find_element.return_value = mock_element

        with patch.object(self.scraper, "driver", mock_driver):
            item = self.scraper.scrape_item(
                "https://shopee.co.th/Razer-Viper-V3-Pro-%E0%B9%80%E0%B8%A1%E0%B8%B2%E0%B8%AA%E0%B9%8C%E0%B9%80%E0%B8%81%E0%B8%A1%E0%B8%A1%E0%B8%B4%E0%B9%88%E0%B8%87%E0%B9%84%E0%B8%A3%E0%B9%89%E0%B8%AA%E0%B8%B2%E0%B8%A2-%E0%B8%99%E0%B9%89%E0%B8%B3%E0%B8%AB%E0%B8%99%E0%B8%B1%E0%B8%81%E0%B9%80%E0%B8%9A%E0%B8%B2%E0%B8%9E%E0%B8%B4%E0%B9%80%E0%B8%A8%E0%B8%A9-55-%E0%B8%81%E0%B8%A3%E0%B8%B1%E0%B8%A1-%E0%B8%AA%E0%B8%A7%E0%B8%B4%E0%B8%95%E0%B8%8A%E0%B9%8C-Razer-Optical-Gen-3-i.15300402.25825925564?sp_atk=2cae18b3-7eda-4701-93e3-dfe6279fb6d6&xptdk=2cae18b3-7eda-4701-93e3-dfe6279fb6d6"
            )
            self.assertIsNotNone(item)
            self.assertEqual(item.current_price, 100.0)

        price = self.scraper.get_price(By.XPATH, "//div[@class='price']")
        self.assertEqual(price, "฿100")

    # Add more test cases for scraper methods as needed


# Create your tests here.
