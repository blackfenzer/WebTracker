from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Automatically manages the ChromeDriver version
driver = webdriver.Chrome()



# Find the "English" button using its class and click itce
def find_price(driver):
    try:
        # Wait for the div with the class "pdp-product-price" to appear
        time.sleep(5)
        div = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "pdp-product-price"))
        )
        # Find the span inside the div
        span = div.find_element(By.TAG_NAME, "span")
        h1 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "pdp-mod-product-badge-title"))
        )
        name = h1.text
        return span.text , name
    except Exception as e:
        print("Could not find the price element:", e)
        return None


urls = [
    "https://www.lazada.co.th/products/razer-viper-v2-pro-ultra-lightweight-wireless-esports-mouse-i3720495469-s14096543251.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253Arazer%252Bmouse%252Bviper%253Bnid%253A3720495469%253Bsrc%253ALazadaMainSrp%253Brn%253Ab90b4a34e02cf4cfd420b445aba07908%253Bregion%253Ath%253Bsku%253A3720495469_TH%253Bprice%253A3690%253Bclient%253Adesktop%253Bsupplier_id%253A100183440200%253Bbiz_source%253Ah5_internal%253Bslot%253A1%253Butlog_bucket_id%253A470687%253Basc_category_id%253A7436%253Bitem_id%253A3720495469%253Bsku_id%253A14096543251%253Bshop_id%253A1496044%253BtemplateInfo%253A107882_D_E%2523-1_A3_C%2523&freeshipping=1&fs_ab=2&fuse_fs=&lang=en&location=Samut%20Sakhon&price=3.69E%203&priceCompare=skuId%3A14096543251%3Bsource%3Alazada-search-voucher%3Bsn%3Ab90b4a34e02cf4cfd420b445aba07908%3BoriginPrice%3A369000%3BdisplayPrice%3A369000%3BsinglePromotionId%3A-1%3BsingleToolCode%3AmockedSalePrice%3BvoucherPricePlugin%3A0%3Btimestamp%3A1737982610994&ratingscore=4.75&request_id=b90b4a34e02cf4cfd420b445aba07908&review=4&sale=18&search=1&source=search&spm=a2o4m.searchlist.list.1&stock=1",
    "https://www.lazada.co.th/products/razer-pro-type-ultra-wireless-mechanical-keyboard-en-100-2-i3850169118-s14694667845.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253Arazer%252Bkeyboard%253Bnid%253A3850169118%253Bsrc%253ALazadaMainSrp%253Brn%253Acaf48552c84d1d79d2060a47f6e532bc%253Bregion%253Ath%253Bsku%253A3850169118_TH%253Bprice%253A3790%253Bclient%253Adesktop%253Bsupplier_id%253A100185285167%253Bbiz_source%253Ah5_internal%253Bslot%253A7%253Butlog_bucket_id%253A470687%253Basc_category_id%253A7245%253Bitem_id%253A3850169118%253Bsku_id%253A14694667845%253Bshop_id%253A1692438%253BtemplateInfo%253A107882_A3_D_E%2523-1_C%2523&freeshipping=1&fs_ab=2&fuse_fs=&lang=en&location=Sukhothai&price=3.79E%203&priceCompare=skuId%3A14694667845%3Bsource%3Alazada-search-voucher%3Bsn%3Acaf48552c84d1d79d2060a47f6e532bc%3BoriginPrice%3A379000%3BdisplayPrice%3A379000%3BsinglePromotionId%3A-1%3BsingleToolCode%3AmockedSalePrice%3BvoucherPricePlugin%3A0%3Btimestamp%3A1737984157274&ratingscore=5.0&request_id=caf48552c84d1d79d2060a47f6e532bc&review=4&sale=13&search=1&source=search&spm=a2o4m.searchlist.list.7&stock=1",
]
for url in urls:
    driver.get(url)
    price, name = find_price(driver)
    print(f"Price: {price}, Name: {name}")

# Close the browser window
driver.close()

driver.quit()
