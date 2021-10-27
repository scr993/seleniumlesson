from selenium import webdriver
import time
from auth_data import inst_pass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://instagram.com/"

# options
options = webdriver.ChromeOptions()

# user-agent
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36')

# disable webdriver
options.add_argument('--disable-blink-features=AutomationControlled')

# headles_mode
options.headless = True

driver = webdriver.Chrome(
    executable_path="C:/Chrome/chromedriver.exe",
    options=options
)
test_xpath_login = '//*[@id="loginForm"]/div/div[1]/div/label/input[@name="username"]'
test_xpath_pass = '//*[@id="loginForm"]/div/div[2]/div/label/input[@name="password"]'
test_xpath_save_login = '//*[@id="react-root"]/section/main/div/div/div/section/div/button[@type="button"]'
test_xpath_notif = '/html/body/div[5]/div/div/div/div[3]/button[1][@tabindex="0"]'

try:
    driver.get(url)
    time.sleep(10)
    print('Passing authentication...')

    login_input = driver.find_element(By.XPATH, test_xpath_login)
    login_input.clear()
    login_input.send_keys('user9578213')
    time.sleep(3)

    pass_input = driver.find_element(By.XPATH, test_xpath_pass)
    pass_input.clear()
    pass_input.send_keys(inst_pass)
    time.sleep(3)

    pass_input.send_keys(Keys.ENTER)
    time.sleep(10)

    print('Going to the post...')
    video_post = driver.get('https://www.instagram.com/p/CVSJOdQAUat/?utm_source=ig_web_copy_link')
    print('Start wathing video...')
    time.sleep(5)
    print('Unmuting audio...')
    unmute_audio = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[1]/div/div/span/div')
    unmute_audio.click()
    time.sleep(20)
    print('Finish watching video...')
except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
