
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path = "C:\\Users\\ASUS\\Documents\\chromedriver-win64\\chromedriver.exe"
# 创建 WebDriver 对象，指明使用chrome浏览器驱动
# wd = webdriver.Chrome(service=Service(r'd:\tools\chromedriver.exe'))
driver = webdriver.Chrome()
# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
# wd.get('https://www.baidu.com')

# 程序运行完会自动关闭浏览器，就是很多人说的闪退
# 这里加入等待用户输入，防止闪退
# input('等待回车键结束程序') 

driver.get('https://histock.tw/stock/tchart.aspx?no=0000&m=t')


element = driver.find_element(By.LINK_TEXT, '多空力道')
# element.send_keys('泰國')
element.click()
# print(element.text)

# a = driver.find_element(By.ID, 'info2')
# print("a.text: ", a.text)
blog = driver.execute_script('return document.getElementById("info2").innerText;')
print(blog)
# Find element and get text

# print(search_box.text)

input('等待回车键结束程序')
driver.quit()