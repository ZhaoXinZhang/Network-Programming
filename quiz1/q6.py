#查詢台灣證交所本國上市證券國際證券辨識號碼一覽表
import pandas as pd #匯入pandas套件
df=pd.read_html('http://isin.twse.com.tw/isin/C_public.jsp?strMode=2',encoding='big5hkscs',header=0)
newdf=df[0][df[0]['產業別'] > '0'] #產業別資料大於 0
del newdf['CFICode'],newdf['備註'] #刪除兩個不需要欄位
df2=newdf['有價證券代號及名稱'].str.split('　', expand=True) #分成兩個欄位回存
df2 = df2.reset_index(drop=True) #重設索引值
newdf = newdf.reset_index(drop=True) #重設索引值
for i in df2.index:
    if '　' in df2.iat[i,0]: #將有價證券代號及名稱
        df2.iat[i,1]=df2.iat[i,0].split('　')[1] #欄位資料內容分割為2，回存df2物件中。
        df2.iat[i,0]=df2.iat[i,0].split('　')[0] #回存df2物件中。
newdf=df2.join(newdf) #將df2合併到newdf物件
newdf=newdf.rename(columns = {0:'股票編號',1:'股票名稱'}) #修改欄位名稱
del newdf['有價證券代號及名稱'] #將"有價證券代號及名稱"欄位刪除
# del newdf['上市日']
del newdf['國際證券辨識號碼(ISIN Code)']
del newdf['市場別']
# newdf.to_excel('stock_.xlsx', sheet_name='Sheet1',index=False) #存入excel
date10=newdf.sort_values('上市日',ascending=True).head(10)
print(date10)
# gdp1_table=pd.DataFrame({'country':gdp1['country'],'continent':gdp1['continent'],'year':gdp1['year'],'lifeExp':gdp1['lifeExp'],'pop':gdp1['pop'],'gdpPercap':gdp1['gdpPercap']})
# print(gdp1_table)

# type=newdf['產業別']
# maxTimesTypeRecord={}
# for i in type:
#     if i in maxTimesTypeRecord:
#         maxTimesTypeRecord[i] += 1
#     else:
#         maxTimesTypeRecord[i] = 1
# maxTimeType = max(maxTimesTypeRecord, key=lambda x: maxTimesTypeRecord[x])#或most_common = max(appear_times)
# print("最多上市公司產業別:",maxTimeType,"\n數量:",maxTimesTypeRecord[maxTimeType])