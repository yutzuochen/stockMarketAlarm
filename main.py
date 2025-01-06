# from taiex import taiexAlarm
from calculate import sn_moneydj  
import sys
import os
from logSys import Logger
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
def main():
    Logger.info("==== start main ====")
    # ETF-00915
    sn_moneydj.etf_00915_kValue_day9()
    # 兆豐金
    sn_moneydj.stockPrice_2886()
    # 大盤日K值下限
    sn_moneydj.taiexKValue_day9()
    # 大盤月K值下限
    sn_moneydj.taiexKValue_month9()
    print("=== all end ===")

main()