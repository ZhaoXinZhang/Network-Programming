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
n=input('請輸入N張發票')
user_number={}
total=0
for i in range(int(n)):
    user_number[i] = input('請輸入你發票號碼：')
# print(type(len(user_number)))
for j in range(len(user_number)):
    if(user_number[j]==numbers['特別獎']):
        print(f'恭喜你第{j+1}張中特別獎','1,000萬元')
        total=total+10000000
    if(user_number[j]==numbers['特獎']):
        print(f'恭喜你第{j+1}張中特獎','200萬元'),
        total=total+2000000
    for i in jackpot:
        if(user_number[j]==i):
            print(f'恭喜你第{j+1}張中頭獎','20萬元')
            total=total+200000
            break
        if(user_number[j][1:]==i[1:]):
            print(f'恭喜你第{j+1}張中二獎','4萬元')
            total=total+40000
            break
        if(user_number[j][2:]==i[2:]):
            print(f'恭喜你第{j+1}張中三獎','1萬元')
            total=total+10000
            break
        if(user_number[j][3:]==i[3:]):
            print(f'恭喜你第{j+1}張中四獎','4千元')
            total=total+4000
            break
        if(user_number[j][4:]==i[4:]):
            print(f'恭喜你第{j+1}張中五獎','1千元')
            total=total+1000
            break
        if(user_number[j][5:]==i[5:]):
            print(f'恭喜你第{j+1}張中六獎','2百元')
            total=total+200
            break
    if(user_number[j][5:]==numbers['增開六獎']):
        print(f'恭喜你第{j+1}張中增開六獎','2百元')
        total=total+200
print(f'你總共得到{total}元',f'平均為{total/int(n)}')

