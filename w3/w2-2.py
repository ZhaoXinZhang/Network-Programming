# #total_amt(成交頭數-總數)、average_weight(成交頭數-平均重量)
# # average_price(成交頭數-平均價格)
# import numpy as np
# # 讀入資料，檔案以","分隔，跳過第一行標題
# print("75kg以上+75kg以下")
# nf1 = np.genfromtxt('Network Programming(jykuo)\w3\pig.csv',delimiter=',',skip_header=1)
# print("市場全年成交最高平均重量"+str((nf1[:,4].max(axis=0)+nf1[:,7].max(axis=0))))
# print("市場全年成交最低平均價"+str(nf1[:,5].min(axis=0)+nf1[:,8].min(axis=0)))
# print("市場全年總成交頭數"+str(nf1[:,3].sum(axis=0)+nf1[:,6].sum(axis=0)))
# #計算每日成交金額，設定為total_sales物件
# total_sales=(nf1[:,3]*nf1[:,4]*nf1[:,5])
# total_sales1=(nf1[:,6]*nf1[:,7]*nf1[:,8])
# total_sales2=total_sales+total_sales1
# print("市場全年總成交金額"+str(total_sales2.sum(axis=0)))
# print("市場全年成交平均每頭金額"+str(total_sales2.sum(axis=0)/nf1[:,0].sum(axis=0)))

# --------------
# import numpy as np
# # 讀入'president_heights.csv'檔案中以","分隔，欄位：
# # order(排序)、name(姓名)、height(cm)(身高)，跳過第一行標題
# data = np.genfromtxt('Network Programming(jykuo)\w3\president_heights.csv', delimiter=',',skip_header=1 )
# # 第三欄height(cm)另存為heights陣列，列印
# heights = np.array(data[:,2])
# print(heights)
# print("Mean height: ", heights.mean())
# print("Standard deviation:", heights.std())
# print("Minimum height: ", heights.min())
# print("Maximum height: ", heights.max())
# # 輸出美國總統身高第一四分位數
# print("25th percentile: ", np.percentile(heights, 25))
# # 輸出美國總統身高第中位數
# print("Median: ", np.median(heights))
# # 輸出美國總統身高第三個四分位數
# print("75th percentile: ", np.percentile(heights, 75))

# -----------------------
import pandas as pd
import numpy as np
data = {'name' : ['Tom', 'John', 'Mary'],
'score' : [88.5, 90.5, 75],
'rank' : [5, 1, 2]}
# 使用字典建構，'grade'欄位為缺失值 NaN
df = pd.DataFrame(data, columns=['name','score','rank','grade']
)
# 設定索引名稱
df.index.name = 'id'
print(df,'\n')
#用欄位名稱索引此欄位資料
print(df['name'],'\n')
print(df.score,'\n')
#用欄位名稱索引此欄位資料
print(df.iloc()[0],'\n')
#重新索引，多加一個 rwo，均為缺失值
df2=df.reindex(list(reversed(range(0, 10))))
print(df2)