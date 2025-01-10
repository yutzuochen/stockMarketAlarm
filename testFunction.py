# from taiex import taiexAlarm
from calculate import sn_moneydj, etf00915
import sys
import os
from logSys import Logger
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
def main():
    Logger.info("==== start main ====")
    # ETF-00915
    # sn_moneydj.etf_00915_kValue_day9_from_money_link()
    # sn_moneydj.etf_00915_kValue_day9_nstock()
    etf00915.etf_00915_kValue_day9_yahoo()
    

main()