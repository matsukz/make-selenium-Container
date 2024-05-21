from selenium import webdriver
import time

options = webdriver.ChromeOptions()
driver = webdriver.Remote(
             command_executor = 'http://sele_selenium:4444/wd/hub',
             options = options
             )

driver.implicitly_wait(10)

url = 'https://google.com/' # テストでアクセスするURLを指定
driver.get(url)

time.sleep(3)
driver.save_screenshot('test.png') # アクセスした先でスクリーンショットを取得
driver.quit()