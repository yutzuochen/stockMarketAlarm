# # from taiex import taiexAlarm
# from calculate import sn_moneydj 
# import sys
# import os
from playsound import playsound

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# def test():
#     # taiexAlarm()
#     # playsound("sound\Recording.mp3")
#     sn_moneydj.stockPrice_2886()
#     # sn_moneydj.taiexKValue_day9()

# 語音提醒
# sound_file = "/sound/alert.mp3"
# sound_file = "sound/Recording.mp3"
sound_file = "C:/Users/ASUS/Documents/stockMarketAlarm/sound/Recording.mp3"
# playsound(r"C:\path\to\your\audiofile.mp3")
# Play the audio file
playsound(sound_file)

# test()