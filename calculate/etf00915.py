from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from calculate.roottk import Roottk
import re
# import tkinter as tk
# from tkinter import font
# import targetValue
from playsound import playsound
# import targetValue
import logSys
import threading
import time
logger = logSys.Logger

def get_chrome_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--profile-directory=Profile 6')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)  # 隐式等待5s
    return driver
# ETF-00915日K值
def etf_00915_kValue_day9_nstock():
    logger.debug("==== start etf_00915_kValue_day9 ====")
    #!!! TODO:targetValue.stock_KValueFloor_day_9_00915_alarm
    targetK_floor = 100
    driver = get_chrome_browser()
    driver.get('https://www.nstock.tw/stock_info?stock_id=00915&status=0')
    
    select_element = driver.find_element("xpath", '//*[@id="__layout"]/div/div[5]/div/div[8]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]')
    time.sleep(4)
    # select = Select(select_element)
    # select.select_by_visible_text('KD,J')
    select_element.click()

    kdSelect = driver.find_element("xpath", '//*[@id="__layout"]/div/div[5]/div/div[8]/div/div[1]/div[1]/div[1]/div[3]/div[1]')
    kdString = kdSelect.text

    # pattern = r'K\(9,3\) (\d+(?:\.\d+)?)'
    pattern = r'K9\s+(\d+\.\d+)'
    
    match = re.search(pattern, kdString)
    if match:
        kValueStr = match.group(1)
        # test case
        # kValueStr = "+9u"
        # examine element from website
        try:
            kValue = float(kValueStr)
        except:
            logger.warning("[etf_00915_kValue_day9_from_money_link] kValueStr cant be float. kValueStr is %s", kValueStr)
            return
        if kValue < 0 or kValue > 100:
            logger.warning("[etf_00915_kValue_day9_from_money_link] kValue < 0 or kValue > 100. kValueStr is %s", kValueStr)
            return
        if kValue < targetK_floor:
            # 語音提醒 
            plan_A_thread = threading.Thread(target = alertReachTarget)
            # 執行執行緒
            plan_A_thread.start()
            print("ETF 00915的 K 值已小於目標值(", targetK_floor, ")，目前 K 值為: ", kValue)
            roottk = Roottk(3000, 3000)
            roottk.popUp(kValue, targetK_floor,"ETF 00915", "日K值")
            roottk.move()
            roottk.popup.mainloop()
    driver.quit()

# ETF-00915日K值
def etf_00915_kValue_day9_yahoo():
    logger.debug("==== start etf_00915_kValue_day9 ====")
    #!!! TODO:targetValue.stock_KValueFloor_day_9_00915_alarm
    targetK_floor = 100
    driver = get_chrome_browser()
    driver.get('https://tw.stock.yahoo.com/quote/00915/technical-analysis')
    time.sleep(4)
    select_element = driver.find_element("xpath", '//*[@id="TAChartIndex"]')
    time.sleep(4)
    select = Select(select_element)
    select.select_by_visible_text('KD,J')
    # select_element.click()

    kdSelect = driver.find_element("xpath", '//*[@id="TAChartLabel2"]')
    kdString = kdSelect.text

    # pattern = r'K\(9,3\) (\d+(?:\.\d+)?)'
    pattern = r'K9\s+(\d+\.\d+)'
    
    match = re.search(pattern, kdString)
    if match:
        kValueStr = match.group(1)
        # test case
        # kValueStr = "+9u"
        # examine element from website
        try:
            kValue = float(kValueStr)
        except:
            logger.warning("[etf_00915_kValue_day9_from_money_link] kValueStr cant be float. kValueStr is %s", kValueStr)
            return
        if kValue < 0 or kValue > 100:
            logger.warning("[etf_00915_kValue_day9_from_money_link] kValue < 0 or kValue > 100. kValueStr is %s", kValueStr)
            return
        if kValue < targetK_floor:
            # 語音提醒 
            plan_A_thread = threading.Thread(target = alertReachTarget)
            # 執行執行緒
            plan_A_thread.start()
            print("ETF 00915的 K 值已小於目標值(", targetK_floor, ")，目前 K 值為: ", kValue)
            roottk = Roottk(3000, 3000)
            roottk.popUp(kValue, targetK_floor,"ETF 00915", "日K值")
            roottk.move()
            roottk.popup.mainloop()
    driver.quit()
def alertReachTarget():
    playsound("sound/Recording.mp3")


# etf_00915_kValue_day9_nstock()