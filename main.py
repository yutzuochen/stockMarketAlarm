# from taiex import taiexAlarm
from calculate import sn_moneydj 
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
def main():
    # 兆豐金
    sn_moneydj.stockPrice_2886()
    # 大盤日K值下限
    sn_moneydj.taiexKValue_day9()
    # 大盤月K值下限
    sn_moneydj.taiexKValue_month9()
    

    # sn_moneydj.stockPrice_2886()



main()