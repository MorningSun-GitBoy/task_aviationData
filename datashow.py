import pandas as pd
data = pd.read_csv('air_data.csv',sep=',',encoding='utf-8')
print(data.head(5))#head(n)返回前n行数据
print(data.tail(5))#tail(n)返回后n行数据
print(data.columns)#columns为其列名数组（Index）
print(data.columns[1])#可以单独查找
print(data.info())#返回字段信息，但是我看不懂
print(data.shape)#数据集大小的对象"(数据数，列数)"
print(data.dtypes)#存储各字段类型的对象
print(data.describe())#返回数据的大体情况
print(data.isnull().any())#isnull()会返回任意数据是否为缺失值的表，any()判断每列的值是否都为true
print(data.isnull().sum())#sum()统计true的数量