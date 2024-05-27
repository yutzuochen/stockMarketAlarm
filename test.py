# from taiex import taiexAlarm
from calculate import sn_moneydj 
import sys
import os
from playsound import playsound

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
def test():
    # taiexAlarm()
    # playsound("sound\Recording.mp3")
    sn_moneydj.stockPrice_2886()
    # sn_moneydj.taiexKValue_day9()



test()