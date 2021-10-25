import requests #匯入套件
from bs4 import BeautifulSoup #解析網頁
import csv #處理CSV檔案
from time import localtime, strftime #處理時間
from os.path import exists #台銀匯率網站
html = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW") #回傳HTML檔案，轉存html物件
bsObj = BeautifulSoup(html.content,'lxml') #解析網頁，建立bs物件
tmp1=0
tmp2=0
c={}
for single_tr in bsObj.find("table", {"title":"牌告匯率"}).find("tbody").findAll("tr"): #針對匯率表格分析
    cell = single_tr.findAll("td") #找到每一個表格
    currency_name = cell[0].find("div", {"class":"visible-phone"}).contents[0] #找到表格中幣別
    currency_name = currency_name.replace("\r","") #取代不需要的字元
    currency_name = currency_name.replace("\n","")
    currency_name = currency_name.replace(" ","")
    currency_rate = cell[2].contents[0] #找到幣別匯率
    currency_rate2 = cell[4].contents[0]
    currency_rate = currency_rate.replace("-","0") #找到幣別匯率
    currency_rate2 = currency_rate2.replace("-","0") #找到幣別匯率
    c[currency_name]=float(currency_rate)-float(currency_rate2)
    
    # print(currency_name, currency_rate,currency_rate2)
    file_name = "bankRate" + currency_name + ".csv" #每種幣別存一個檔案
    now_time = strftime("%Y-%m-%d %H:%M:%S", localtime()) #記錄目前時間
    
    if(currency_name=='英鎊(GBP)'):
        print('英鎊(GBP)')
        print(f'現金匯率:本行賣出:{currency_rate}')
        print(f'即期匯率:本行賣出:{currency_rate2}')
        print("抓取(牌告)時間:",now_time,'\n')
    if(currency_name=='加拿大幣(CAD)'):
        print('加拿大幣(CAD)')
        print(f'現金匯率:本行賣出:{currency_rate}')
        print(f'即期匯率:本行賣出:{currency_rate2}')
        print("抓取(牌告)時間:",now_time,'\n')
    if(currency_name=='歐元(EUR)'):
        print('歐元(EUR)')  
        print(f'現金匯率:本行賣出:{currency_rate}')  
        print(f'即期匯率:本行賣出:{currency_rate2}')
        print("抓取(牌告)時間:",now_time,'\n') 
# print(c)
# num=0
# for key, value in sorted(c.items(), key=lambda item:item[1], reverse=True):
#     if (num>=10): break
#     if(2<=num<=4):print(key, ',', value)
#     num = num +1 
# print("現金賣出最高:",tmp1_name,tmp1)
# print("即期賣出最高:",tmp2_name,tmp2)
