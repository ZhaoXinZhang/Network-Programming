from __future__ import unicode_literals, print_function
import urllib
from bs4 import BeautifulSoup
import urllib.request
request_url = 'http://invoice.etax.nat.gov.tw/' # 財政部官網
htmlContent = urllib.request.urlopen(request_url).read() # 開啟網址取得HTML
soup = BeautifulSoup(htmlContent, "html.parser") #以"html.parser"解析設為soup物件
#用soup的find_all找網頁所有標籤為"span"且class屬性值"t18Red"內容，設給result物件
results = soup.find_all("span", class_="t18Red")
subTitle = ['特別獎', '特獎', '頭獎', '增開六獎'] # 獎項
# 找網頁中所有標籤為'h2'且id屬性值為'tabTitle'內容，設給months物件
months = soup.find_all('h2', {'id': 'tabTitle'})
#運用months物件find_next_sibling找標籤為'h2'的下二個內容，
#將text設定為month_newest(最新一期)與month_previous(上一期)物件。
month_newest = months[0].find_next_sibling('h2').text # 最新一期
month_previous = months[1].find_next_sibling('h2').text # 上一期
print(results[1].text)
numbers={}
print("最新一期統一發票開獎號碼 ({0})：".format(month_newest))
for index, item in enumerate(results[:4]):
    numbers[subTitle[index]]= item.text
jackpot=numbers['頭獎'].split('、')
user_number = input('請輸入你發票號碼：')
if(user_number==numbers['特別獎']):
    print('恭喜你中特別獎')
if(user_number==numbers['特獎']):
    print('恭喜你中特獎')
for i in jackpot:
    if(user_number==i):
        print('恭喜你中頭獎')
        break
    if(user_number[1:]==i[1:]):
        print('恭喜你中二獎')
        break
    if(user_number[2:]==i[2:]):
        print('恭喜你中三獎')
        break
    if(user_number[3:]==i[3:]):
        print('恭喜你中四獎')
        break
    if(user_number[4:]==i[4:]):
        print('恭喜你中五獎')
        break
    if(user_number[5:]==i[5:]):
        print('恭喜你中六獎')
        break
if(user_number[5:]==numbers['增開六獎']):
    print('恭喜你中增開六獎')
