from calculate.roottk import Roottk_report

def printReport(arrs): # [標的, 指標種類, 現在價格, 目標價格] e.g. [ETF-00915, K值, 18, 20]
    s = ""
    for arr in arrs:
        s += arr[0] + " 的當前" + arr[1] + "為 " + str(arr[2]) + " , 設定目標為 " + str(arr[3]) + "\n\n" 

    roottk = Roottk_report(1000, 1000)

    roottk.popUp(s)
    roottk.popup.mainloop()