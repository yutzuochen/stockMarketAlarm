from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import re
import os
from constant import constant




def taiexKValue_day9():
    path = os.getenv("ChromedriverPath")
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
        kValue = float(match.group(1))

    if kValue < constant.taiex_KValueFloor_day_9_alarm:
        print("大盤的 K 值已小於目標值(", constant.taiex_KValueFloor_day_9_alarm, ")，目前 K 值為: ", kValue)

    # input('等待回车键结束程序')
    driver.quit()


def taiexKValue_month9():
    path = os.getenv("ChromedriverPath")
    # 创建 WebDriver 对象，指明使用chrome浏览器驱动
    # wd = webdriver.Chrome(service=Service(r'd:\tools\chromedriver.exe'))
    driver = webdriver.Chrome()
    driver.get('https://www.moneydj.com/Z/ZB/ZBH/ZBH.djhtm')


    element = driver.find_element(By.NAME, 'T')
    select = Select(element)
    # select.select_by_value("月線")
    select.select_by_visible_text('月線')

    kdElement = driver.find_element(By.ID, 'fg2')
    kdString = kdElement.text

    pattern = r'K\(9,3\) (\d+(?:\.\d+)?)'
    match = re.search(pattern, kdString)
    if match:
        kValue = float(match.group(1))

    if kValue < constant.taiex_KValueFloor_month_9_alarm:
        print("大盤的 K 值已小於目標值(", constant.taiex_KValueFloor_month_9_alarm, ")，目前 K 值為: ", kValue)

    input('等待回车键结束程序')
    driver.quit()

if __name__ == "__main__":
    print("XDDDDDDDDDDDDDDDDDDDDDDDD")
    taiexKValue_day9()
# if __name__ == "__main__":
#     taiexKValue_month9()