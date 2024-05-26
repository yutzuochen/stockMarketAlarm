
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = "C:\\Users\\ASUS\\Documents\\chromedriver-win64\\chromedriver.exe"
# 创建 WebDriver 对象，指明使用chrome浏览器驱动
# wd = webdriver.Chrome(service=Service(r'd:\tools\chromedriver.exe'))
driver = webdriver.Chrome()
# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
# wd.get('https://www.baidu.com')


driver.get('https://goodinfo.tw/tw/ShowK_Chart.asp?STOCK_ID=%E5%8A%A0%E6%AC%8A%E6%8C%87%E6%95%B8')


# Find element and get text
# element = driver.find_element(By.CLASS_NAME, 'b1.p4_4.r10.box_shadow').text
# print(element.text)

input('等待回车键结束程序')
driver.quit()
