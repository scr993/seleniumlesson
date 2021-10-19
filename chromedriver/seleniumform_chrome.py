from selenium import webdriver
import time

url = "https://instagram.com/"
options = webdriver.ChromeOptions()
options.add_argument('user-agent=Internet Explorer 11 (Win 8.1 x64): Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; ASU2JS; rv:11.0) like Gecko')


driver = webdriver.Chrome(
    executable_path="C:/Chrome/chromedriver.exe",
    options=options
)

try:
    
except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
