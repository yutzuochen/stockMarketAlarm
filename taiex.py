import requests

def taiexAlarm():
    print("======== start taiexAlarm ========")
    url = "https://histock.tw/%E5%8F%B0%E8%82%A1%E5%A4%A7%E7%9B%A4"
    response = requests.get(url)
    if response.status_code == 200:
    # Open a file in write mode
        with open("taiex.html", "w", encoding="utf-8") as f:
            # Write the response content to the file
            f.write(response.text)
        print("Response saved ")
    else:
        print("Failed to retrieve data from the URL")
        # print(response.text)


def testWangoo():
    url = "https://www.wantgoo.com/index/0000"
    # Define headers to mimic a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
    # Open a file in write mode
        with open("test1.html", "w", encoding="utf-8") as f:
            # Write the response content to the file
            f.write(response.text)
        print("Response saved ")
    else:
        print("response.status_code: ", response.status_code)
        print("Failed to retrieve data from the URL")

def test00915():
    url = "https://histock.tw/stock/tchart.aspx?no=00915&m=b"
    # Define headers to mimic a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
    # Open a file in write mode
        with open("s00915.html", "w", encoding="utf-8") as f:
            # Write the response content to the file
            f.write(response.text)
        print("Response saved ")
    else:
        print("response.status_code: ", response.status_code)
        print("Failed to retrieve data from the URL")




test00915()