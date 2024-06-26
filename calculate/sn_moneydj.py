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

g1, g2 = 1000, 1000
path2 = os.getenv("ChromedriverPath")
root = tk.Tk()
# root.withdraw()
popup = tk.Toplevel(root)
def move():
    global g1, g2
    popup.geometry(f'{str(g1)}x{str(g2)}+{random.randint(0, 800)}+{random.randint(0, 600)}')
    popup.after(1000, move)

def taiexKValue_day9():
    targetK_floor = targetValue.taiex_KValueFloor_day_9_alarm
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

        if kValue < targetK_floor:
            print("大盤的 K 值已小於目標值(", targetK_floor, ")，目前 K 值為: ", kValue)
            # root = tk.Tk()
            # root.withdraw()
            # root.withdraw()
            # popup = tk.Toplevel(root)
            popUp(popup, kValue, targetK_floor)
            def move():
                global g1, g2
                popup.geometry(f'{str(g1)}x{str(g2)}+{random.randint(0, 800)}+{random.randint(0, 600)}')
                popup.after(1000, move)

            move()
            popup.mainloop()
    # input('等待回车键结束程序')
    driver.quit()


def taiexKValue_month9():
    # targetKvalue_floor = constant.taiex_KValueFloor_month_9_alarm
    targetKvalue_floor = targetValue.taiex_KValueFloor_month_9_alarm
    
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

        if kValue < targetKvalue_floor:
            print("大盤的 K 值已小於目標值(", targetKvalue_floor, ")，目前 K 值為: ", kValue)
            # root = tk.Tk()
            # root.withdraw()
            # popup = tk.Toplevel(root)
            popUp(popup, kValue, targetKvalue_floor)
            def move():
                global g1, g2
                popup.geometry(f'{str(g1)}x{str(g2)}+{random.randint(0, 800)}+{random.randint(0, 600)}')
                popup.after(1000, move)

            move()
            popup.mainloop()
    input('等待回车键结束程序')
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

def stockPrice_2886():
    # targetPrice = constant.stock_PriceFloor_2886_alarm
    targetPrice = targetValue.stock_PriceFloor_2886_alarm
    driver = webdriver.Chrome()
    driver.get('https://histock.tw/stock/2886')
    element = driver.find_element(By.CLASS_NAME, 'clr-gr')
    price2886 = float(element.text)
    if price2886 < targetPrice:
        print("兆豐金現價已小於目標值(", targetPrice, ")，目前 K 值為: ", price2886)
        # root = tk.Tk()
        # root.withdraw()
        # root.withdraw()
        # popup = tk.Toplevel(root)
        popUp(popup, price2886, targetPrice)
        # def move():
        #     global g1, g2
        #     popup.geometry(f'{str(g1)}x{str(g2)}+{random.randint(0, 800)}+{random.randint(0, 600)}')
        #     popup.after(1000, move)

        move()
        popup.mainloop()

    # input('等待回车键结束程序')
    driver.quit()
    print("========== end ============")

if __name__ == "__main__":
    print("XDDDDDDDDDDDDDDDDDDDDDDDD")
    stockPrice_2886()
# if __name__ == "__main__":
#     taiexKValue_month9()