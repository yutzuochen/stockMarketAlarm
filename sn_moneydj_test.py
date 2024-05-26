
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re

path = "C:\\Users\\ASUS\\Documents\\chromedriver-win64\\chromedriver.exe"
# 创建 WebDriver 对象，指明使用chrome浏览器驱动
# wd = webdriver.Chrome(service=Service(r'd:\tools\chromedriver.exe'))
driver = webdriver.Chrome()


driver.get('https://www.moneydj.com/Z/ZB/ZBH/ZBH.djhtm')


element = driver.find_element(By.ID, 'fg2')
kdString = element.text

pattern = r'K\(9,3\) (\d+(?:\.\d+)?)'
# pattern = r'K\(10,3\) (\d+(?:\.\d+)?)'
match = re.search(pattern, kdString)
if match:
    kValue = match.group(1)

# blog = driver.execute_script('return document.getElementById("info2").innerText;')
# print(blog)
# Find element and get text

# print(search_box.text)

input('等待回车键结束程序')
driver.quit()