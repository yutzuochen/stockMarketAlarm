# from taiex import taiexAlarm
from calculate import sn_moneydj  
import sys
import os
import setting
from logSys import Logger
import time
from datetime import datetime
from calculate.report import printReport

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
def main():
    # 訂定一天的結束時間
    Logger.info("==== start main ====")
    # Convert the end time string to a datetime object for comparison
    end_time_obj = datetime.strptime(setting.endTime, "%H:%M").time()

    # Get the current time
    now = datetime.now().time()

    # Check if the current time is before the end time
    if now > end_time_obj:
        Logger.debug("已到休班時間，提醒程式不啟動~")
        return
    
    reportArr = []
    # ETF-00915
    sn_moneydj.etf_00915_kValue_day9(reportArr)
    # 兆豐金
    sn_moneydj.stockPrice_2886(reportArr)
    # 大盤日K值下限
    sn_moneydj.taiexKValue_day9(reportArr)
    # 大盤月K值下限
    sn_moneydj.taiexKValue_month9(reportArr)

    # 結算報告
    printReport(reportArr)
    print("=== all end ===")

main()