import numpy
from numpy.lib.function_base import average
import pandas as pd
from pandas.core.frame import DataFrame
programmingLanguage=pd.Series(numpy.random.randint(100,size=5),index=['Apple','Ben','Cindy','David','Ella'])
Math=pd.Series(numpy.random.randint(100,size=5),index=['Apple','Ben','Cindy','David','Ella'])
English=pd.Series(numpy.random.randint(100,size=5),index=['Apple','Ben','Cindy','David','Ella'])
table=DataFrame({'programming Languag':programmingLanguage,'Math':Math,'English':English})
print(table)
max_score=DataFrame({'Name':table.idxmax(),'score':table.max()})
print(max_score)
print('\naverage:\n',table.mean())
print('\nmedian:\n',table.median())