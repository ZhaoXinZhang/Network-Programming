import urllib.request #匯入套件
import zipfile
import csv
# 公開資料檔案
url ='https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/csv/zip'
zipName = 'F.zip' #壓縮檔案名稱
urllib.request.urlretrieve(url,zipName) #下載壓縮檔
f=zipfile.ZipFile(zipName) #開啟壓縮檔
#file_dir = './FF'
file_dir = './' #解壓縮目錄
for fileName in f.namelist(): #壓縮檔案列表檔名
    f.extract(fileName,file_dir) #擷取壓縮檔案
    print(fileName) #印出解壓縮檔案名稱
f.close() #關檔
with open(fileName,newline='',encoding = 'utf8') as csvfile:
    readFile =csv.DictReader(csvfile)
    for row in readFile: 
        if int(row['tot']) > 10:
            print(row['ar'])
