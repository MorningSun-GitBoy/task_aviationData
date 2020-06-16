import pandas as pd 

table = pd.read_csv("air_data.csv",sep=",",encoding="utf-8")
#print(table.dtypes)
table = table[~((SUM_YR_1.isin([0]))|(SUM_YR_2).isin([]))]