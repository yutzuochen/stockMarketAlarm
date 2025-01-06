# from taiex import taiexAlarm
from calculate import sn_moneydj 
import logSys 
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
def main():
    # build system of log
    # logger = logSys.Logger
    # logger.error("Error: Something went wrong!")
    # logger.critical("Critical: Serious problem occurred!")
    # ETF-00915
    sn_moneydj.etf_00915_kValue_day9()
    # 兆豐金
    sn_moneydj.stockPrice_2886()
    # 大盤日K值下限
    sn_moneydj.taiexKValue_day9()
    # 大盤月K值下限
    sn_moneydj.taiexKValue_month9()

main()