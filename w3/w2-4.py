from tkinter.constants import E
import pandas as pd
from pandas.core.frame import DataFrame
from pandas.core.indexes.base import Index
sc = pd.read_csv('score.csv',encoding="utf-8", sep=",")
sc.columns = [ 'Name', 'quiz1', 'quiz2','quiz3','quiz4','mid','final']
sc['mean']=sc.mean(axis=1)
print(sc)
sc_mean_sort3=sc.sort_values('mean',ascending=False).head(3)
sc_mean_3_table=DataFrame({'Name':sc_mean_sort3['Name'],'meanScore':sc_mean_sort3['mean']})
print(sc_mean_3_table)
print('\n',sc[sc['mean']>85],'\n')
array=list()
for i in range(1,5):
    print(f'\nquiz{i}_max:',sc.iloc[sc[f'quiz{i}'].idxmax(),0],sc[f'quiz{i}'].max(),end=' ')
    array.append(sc[f'quiz{i}'].max())
    # arr[f'quiz{i}']=sc.iloc[sc[f'quiz{i}'].idxmax(),0]+sc[f'quiz{i}'].max()
    pd.set_option('mode.chained_assignment', None)
    sc[f'quiz{i}'][sc[f'quiz{i}'].idxmax()]=0
    if(sc[f'quiz{i}'].max()==array[i-1]):
        print(sc.iloc[sc[f'quiz{i}'].idxmax(),0],sc[f'quiz{i}'].max(),end=' ')
print('\nmid_max:',sc.iloc[sc['mid'].idxmax(),0],sc['mid'].max())
print('final_max',sc.iloc[sc['final'].idxmax(),0],sc['final'].max())

sc2 = pd.read_csv('score.csv',encoding="utf-8", sep=",")
sc2.columns = [ 'Name', 'quiz1', 'quiz2','quiz3','quiz4','mid','final']
array=list()
for i in range(1,5):
    print(f'\nquiz{i}_min:',sc2.iloc[sc2[f'quiz{i}'].idxmin(),0],sc2[f'quiz{i}'].min(),end=' ')
    array.append(sc[f'quiz{i}'].min())
    # arr[f'quiz{i}']=sc.iloc[sc[f'quiz{i}'].idxmin(),0]+sc[f'quiz{i}'].min()
    pd.set_option('mode.chained_assignment', None)
    sc[f'quiz{i}'][sc[f'quiz{i}'].idxmin()]=100
    if(sc[f'quiz{i}'].min()==array[i-1]):
        print(sc.iloc[sc[f'quiz{i}'].idxmin(),0],sc[f'quiz{i}'].min(),end=' ')
print('\nmid_min:',sc.iloc[sc['mid'].idxmin(),0],sc['mid'].min())
print('final_min',sc.iloc[sc['final'].idxmin(),0],sc['final'].min())
