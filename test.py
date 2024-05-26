# from taiex import taiexAlarm
from calculate import sn_moneydj 
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
def test():
    # taiexAlarm()
    sn_moneydj.taiexKValue_month9()



test()