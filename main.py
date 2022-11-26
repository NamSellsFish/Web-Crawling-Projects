import requests
import argparse
import json
from bs4 import BeautifulSoup

# Get numbers. (This might help: https://stackoverflow.com/questions/
# 15753701/how-can-i-pass-a-list-as-a-command-line-argument-with-argparse)
parser = argparse.ArgumentParser()
parser.add_argument("numbers", nargs='*', help='Get lottery numbers')
args = parser.parse_args()._get_kwargs()[0][1]

# Find winners
ses = requests.session()
ses = requests.get("https://ketqua.vn/")
soup = BeautifulSoup(ses.content, "html.parser")
prizeJson = json.loads(soup.find("div", class_="data-kqxs hidden").text)
prizeJson[' đặc biệt'] = prizeJson.pop('g0')
if not args:
    print("                 *Kết quả sổ xố miền Bắc*")
    for key, prize in prizeJson.items():
        print("- Giải {}: {}".format(key[1:], prize))
else:
    for prize, num in prizeJson.items():
        check = False
        for arg in args:
            if num.find(arg) != -1:
                print("Bạn đã trúng giải {} với số {}".format(prize[1:], arg))
                check = True
    if check is False:
        print("Bạn không trúng gì cả!")
