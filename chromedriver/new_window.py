from selenium import webdriver
import time
from auth_data import inst_pass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://www.avito.ru/kaliningrad/kvartiry"

# options
options = webdriver.ChromeOptions()

# user-agent
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/94.0.4606.81 Safari/537.36')

# disable webdriver
options.add_argument('--disable-blink-features=AutomationControlled')

# # headles_mode
# options.headless = True

driver = webdriver.Chrome(
    executable_path="C:/Chrome/chromedriver.exe",
    options=options
)
xpath_items = '//div[@data-marker="item-photo"]'


try:
    driver.get(url)
    # print(driver.window_handles)
    print(f'Current url is:{driver.current_url}')
    # time.sleep(5)
    driver.implicitly_wait(5)

    items = driver.find_elements(By.XPATH, xpath_items)
    items[0].click()
    # print(driver.window_handles)
    driver.switch_to.window(driver.window_handles[1])
    print(f'Current url is:{driver.current_url}')
    # time.sleep(5)
    driver.implicitly_wait(5)

    username = driver.find_element_by_class_name('seller-info-name')

    print(f'username is:', username.text)
    # time.sleep(3)
    driver.implicitly_wait(5)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print(f'current page:{driver.current_url}')

    items[1].click()
    # time.sleep(3)
    driver.implicitly_wait(5)

    driver.switch_to.window(driver.window_handles[1])
    print(f'current url:', driver.current_url)
    ad_date = driver.find_element(By.XPATH, '//div[@class="title-info-metadata-item-redesign"]')
    print(f'an ad date is:{ad_date.text}')

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
