from selenium import webdriver
import time

url = "https://instagram.com/"

# options
options = webdriver.ChromeOptions()

# user-agent
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36')

# disable webdriver
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(
    executable_path="C:/Chrome/chromedriver.exe",
    options=options
)

try:
    driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
    time.sleep(10)
except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
