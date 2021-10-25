# 讀入 csv 文字檔
import pandas as pd
csv_file = "https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv"
gdp = pd.read_csv(csv_file)

gdp1=gdp.sort_values('lifeExp',ascending=False).head(1)
gdp1_table=pd.DataFrame({'country':gdp1['country'],'continent':gdp1['continent'],'year':gdp1['year'],'lifeExp':gdp1['lifeExp'],'pop':gdp1['pop'],'gdpPercap':gdp1['gdpPercap']})
print(gdp1_table)

country = gdp['country']
gdp3=gdp[gdp['year'] == 2007].groupby(by = 'continent')['gdpPercap'].mean()

print(gdp3)





# array=list()
# for i in range(1):
#     print('\n全球lifeExp最老的國家與其相關資料:',gdp.iloc[gdp['lifeExp'].idxmax(),0],gdp['lifeExp'].max(),end=' ')
    # array.append(gdp['lifeExp'].max())
    # # arr[f'quiz{i}']=sc.iloc[sc[f'quiz{i}'].idxmax(),0]+sc[f'quiz{i}'].max()
    # pd.set_option('mode.chained_assignment', None)
    # gdp[f'quiz{i}'][gdp[f'quiz{i}'].idxmax()]=0
    # if(gdp[f'quiz{i}'].max()==array[i-1]):
    #     print(gdp.iloc[gdp[f'quiz{i}'].idxmax(),0],gdp[f'quiz{i}'].max(),end=' ')