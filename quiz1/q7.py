#抓取7-eleven各門市資訊
import requests #抓取網頁的套件
import pandas as pd #分析資料的套件
# 建立一個縣市的list
# city = ['台北市', '新北市']
city = ['基隆市', '台北市', '新北市', '桃園市', '新竹市','新竹縣','苗栗縣','台中市','彰化縣', '雲林縣', '南投縣', '嘉義縣', '嘉義市', '台南市', '高雄市', '屏東縣', '台東縣', '花蓮縣', '宜蘭縣', '連江縣', '金門縣', '澎湖縣']
#使用迴圈依序取得每一個城市的門市資訊， enumerate(city) 產生 [0, 基隆市] [1, 台北市][2, 新北市][3, 桃園市]
roadAddressRecord ={}
streetAddressRecord={}
fullroadAddressRecord={}
fullstreetAddressRecord={}
for index, city in enumerate(city):
#剛在網頁開發者模式觀察到的Post發出的資訊是那些
    data = {'strTargetField':'COUNTY','strKeyWords':'%s' % city}
    
    #res 取得網頁所有資料
    res = requests.post('https://www.ibon.com.tw/retail_inquiry_ajax.aspx', data=data)
    # 第一次迴圈
    if index == 0:
        #網頁資料的形式是table，使用panda的 read_html 取得資料 [0]第一欄資料
        # res.txt 網頁資料中的文字，[0]第一欄資料, header=0 不要第一列標頭資料
        df_7_11_store = pd.read_html(res.text, header=0)[0]
        #建立dataframe，將城市填入。
        df_7_11_store['縣市'] = city
    # 第二次迴圈以上就將資訊直接append到dataframe裡
    if index > 0:
        oneCity_store = pd.read_html(res.text, header=0)[0]
        oneCity_store['縣市'] = city
        df_7_11_store = df_7_11_store.append(oneCity_store)
    #印出查詢資料進度, shape[0] 查詢本次城市取得資料的筆數
    
    # print('%2d) %-*s %4d' % (index+1, 5, city, pd.read_html(res.text, header=0)[0].shape[0]))
    count = pd.read_html(res.text, header=0)[0].shape[0] 
    data = pd.read_html(res.text, header=0)[0]
    for i in range(count):
    #第三欄資料為地址 iloc[i,2]
        fullAddress = data.iloc[i,2]
        #找城市名稱開頭，路結尾的地址字串
        start = fullAddress.find(city[0])
        end = fullAddress.find('路')+1
        #end = fullAddress.find('街')+1
        if end<3: continue #空的資料跳過
        roadAddress = fullAddress[start:end]
        #print(roadAddress)
        if roadAddress not in roadAddressRecord:
            roadAddressRecord[roadAddress]=1
        else:
            roadAddressRecord[roadAddress]+=1
    for i in range(count):
    #第三欄資料為地址 iloc[i,2]
        fullAddress = data.iloc[i,2]
        #找城市名稱開頭，路結尾的地址字串
        start = fullAddress.find(city[0])
        end = fullAddress.find('街')+1
        if end<3: continue #空的資料跳過
        roadAddress = fullAddress[start:end]
        #print(roadAddress)
        if roadAddress not in streetAddressRecord:
            streetAddressRecord[roadAddress]=1
        else:
            streetAddressRecord[roadAddress]+=1
    # print(roadAddressRecord)
    #針對本次城市所有門市統計同一個路的門市
    # print(streetAddressRecord)
    # print('------%s7-11店數最多之路---------'%city)
    # num=0
    # for key, value in sorted(roadAddressRecord.items(), key=lambda item:item[1], reverse=True):
    #     if (num>=3): break
    #     print(key, ',', value)
    #     num = num +1 
    #     print('------%s7-11店數最多之街---------'%city)
    # num=0
    # for key, value in sorted(streetAddressRecord.items(), key=lambda item:item[1], reverse=True):
    #     if (num>=3): break
    #     print(key, ',', value)
    #     num = num +1 
del roadAddressRecord['高雄市路']
print('------7-11店數最多之路---------')
num=0
for key, value in sorted(roadAddressRecord.items(), key=lambda item:item[1], reverse=True):
    if (num>=3): break
    print(key, ',', value,key[0:3])
    num = num +1 
print('------7-11店數最多之街---------')
num=0
for key, value in sorted(streetAddressRecord.items(), key=lambda item:item[1], reverse=True):
    if (num>=3): break
    print(key, ',', value,key[0:3])
    num = num +1 

#將資料輸出成Excel
df_7_11_store.to_excel('7_11.xlsx', encoding="UTF-8", index=False)
