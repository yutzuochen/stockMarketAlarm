from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import re
import os
# from constant import constant
import tkinter as tk
from tkinter import font
import random
import targetValue
# from playsound import playsound
import targetValue
import logSys

logger = logSys.Logger


g1, g2 = 1000, 1000
path2 = os.getenv("ChromedriverPath")
root = tk.Tk()
# root.withdraw()
popup = tk.Toplevel(root)
def move():
    global g1, g2
    popup.geometry(f'{str(g1)}x{str(g2)}+{random.randint(0, 800)}+{random.randint(0, 600)}')
    popup.after(1000, move)
# 大盤日K值
def taiexKValue_day9():
    targetK_floor = targetValue.taiex_KValueFloor_day_9_alarm
    path = os.getenv("ChromedriverPath")
    # 创建 WebDriver 对象，指明使用chrome浏览器驱动
    # wd = webdriver.Chrome(service=Service(r'd:\tools\chromedriver.exe'))
    driver = webdriver.Chrome()
    driver.get('https://www.moneydj.com/Z/ZB/ZBH/ZBH.djhtm')
    # TODO: catch error:if URL change
    # driver.get('https://www.money.com/Z/ZB/ZBH/ZBH.djhtm')
    # if not get:
    # ....
    element = driver.find_element(By.ID, 'fg2')
    kdString = element.text

    pattern = r'K\(9,3\) (\d+(?:\.\d+)?)'
    match = re.search(pattern, kdString)
    if match:
        kValue = float(match.group(1))

        if kValue < targetK_floor:
            print("大盤的 K 值已小於目標值(", targetK_floor, ")，目前 K 值為: ", kValue)
            popUp(popup, kValue, targetK_floor)
            def move():
                global g1, g2
                popup.geometry(f'{str(g1)}x{str(g2)}+{random.randint(0, 800)}+{random.randint(0, 600)}')
                popup.after(1000, move)

            move()
            popup.mainloop()
    # input('等待回车键结束程序')
    driver.quit()

# 大盤月K值
def taiexKValue_month9():
    targetKvalue_floor = targetValue.taiex_KValueFloor_month_9_alarm
    # path = os.getenv("ChromedriverPath")
    # 創建 Web driver 物件，指定使用chrome瀏覽器驅動
    driver = webdriver.Chrome()
    # moneyDJ 的大盤指數，網址可能隨時會動
    driver.get('https://www.moneydj.com/Z/ZB/ZBH/ZBH.djhtm')

    # TODO: catch error:if URL change
    # driver.get('https://www.money.com/Z/ZB/ZBH/ZBH.djhtm')
    # if not get:
    # ....
    element = driver.find_element(By.NAME, 'T')
    select = Select(element)
    select.select_by_visible_text('月線')

    kdElement = driver.find_element(By.ID, 'fg2')
    kdString = kdElement.text

    pattern = r'K\(9,3\) (\d+(?:\.\d+)?)'
    match = re.search(pattern, kdString)
    if match:
        kValue = float(match.group(1))
        if kValue < targetKvalue_floor:
            print("大盤的 K 值已小於目標值(", targetKvalue_floor, ")，目前 K 值為: ", kValue)
            popUp(popup, kValue, targetKvalue_floor)
            def move():
                global g1, g2
                popup.geometry(f'{str(g1)}x{str(g2)}+{random.randint(0, 800)}+{random.randint(0, 600)}')
                popup.after(1000, move)

            move()
            popup.mainloop()
    # input('等待回车键结束程序')
    driver.quit()


# def move():
#     global g1, g2
#     popup.geometry(f'{str(g1)}x{str(g2)}+{random.randint(0, 800)}+{random.randint(0, 600)}')
#     popup.after(1000, move)
    
def exit_application():
    root.destroy()

def on_close():
    print("Closing the window")
    root.destroy()

def popUp(popup, price, targetPrice):
    global g1, g2
    notification_title = "Stock Alert"
    notification_message = f"Stock price is {price}.\n Price > {targetPrice}!"
    # logger.info(notification_message)
    print("notification_message: ", notification_message)
    # popup = tk.Toplevel(root)
    popup.title(notification_title)
    popup.geometry(f'{str(g1)}x{str(g2)}')
    custom_font = font.Font(family="Helvetica", size=16)

    label = tk.Label(popup, text=notification_message, height= 100, padx=40, pady=10, font=custom_font, relief="ridge")
    label.pack()
    popup.protocol("WM_DELETE_WINDOW", on_close)

    # root.mainloop()
    print("ok")
    
# 兆豐金
def stockPrice_2886():
    targetPrice = targetValue.stock_PriceFloor_2886_alarm
    driver = webdriver.Chrome()
    driver.get('https://histock.tw/stock/2886')
    element = driver.find_element(By.CLASS_NAME, 'clr-rd')
    #TODO:catch error
    price2886 = float(element.text)
    if price2886 < targetPrice:
        print("兆豐金現價已小於目標值(", targetPrice, ")，目前 K 值為: ", price2886)

        popUp(popup, price2886, targetPrice)

        move()
        popup.mainloop()

    # input('等待回车键结束程序')
    driver.quit()
    print("========== end ============")

# ETF-00915日K值
def etf_00915_kValue_day9():
    logger.error("Error: Something went wrong!")
    logger.critical("Critical: Serious problem occurred!")
    targetK_floor = targetValue.stock_KValueFloor_day_9_00915_alarm
    # path = os.getenv("ChromedriverPath")
    # 创建 WebDriver 对象，指明使用chrome浏览器驱动
    # wd = webdriver.Chrome(service=Service(r'd:\tools\chromedriver.exe'))
    driver = webdriver.Chrome()
    driver.get('https://www.moneydj.com/ETF/X/Basic/Basic0002.xdjhtm?etfid=00915.TW')
    # TODO: catch error:if URL change
    # driver.get('https://www.money.com/Z/ZB/ZBH/ZBH.djhtm')
    # if not get:
    # ....
    element = driver.find_element(By.ID, 'fg2')
    kdString = element.text

    pattern = r'K\(9,3\) (\d+(?:\.\d+)?)'
    match = re.search(pattern, kdString)
    if match:
        kValue = float(match.group(1))

        if kValue < targetK_floor:
            print("大盤的 K 值已小於目標值(", targetK_floor, ")，目前 K 值為: ", kValue)
            popUp(popup, kValue, targetK_floor)
            def move():
                global g1, g2
                popup.geometry(f'{str(g1)}x{str(g2)}+{random.randint(0, 800)}+{random.randint(0, 600)}')
                popup.after(1000, move)

            move()
            popup.mainloop()
    # input('等待回车键结束程序')
    driver.quit()


# if __name__ == "__main__":
#     print("XDDDDDDDDDDDDDDDDDDDDDDDD")
#     stockPrice_2886()
# if __name__ == "__main__":
#     taiexKValue_month9()