import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# 使用 Chrome 的 WebDriver
driver = webdriver.Chrome()

#關閉瀏覽器通知
options = webdriver.ChromeOptions()
prefs = {
        'profile.default_content_setting_values':
        {
            'notifications': 2
        }
      }
options.add_experimental_option('prefs',prefs)
driver = webdriver.Chrome(chrome_options=options)

# 開啟 popcat 登入頁面
driver.get('https://popcat.click/')

while(1):
    re=driver.find_element_by_xpath('//*[@id="app"]/div')
    re.click()


# #關閉廣告
# ads_btn = driver.find_element_by_css_selector('div.shopee-popup__close-btn')
# ads_btn.click()
# time.sleep(0.1)


# 關閉瀏覽器
# driver.close()