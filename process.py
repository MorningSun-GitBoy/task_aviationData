import pandas as pd
data = pd.read_csv('air_data.csv',sep=',',encoding='utf-8')
#清洗数据
#将SUM_YR_1=0或SUM_YR_2=0或avg_discount=0的数据
#print(data.shape)
#unuse = data[(data.SUM_YR_1.isin([0]))|(data.SUM_YR_2.isin([0]))|(data.avg_discount.isin([0]))]
data = data[~((data.SUM_YR_1.isin([0]))|(data.SUM_YR_2.isin([0]))|(data.avg_discount.isin([0])))]
#data[.....]是条件选择，“[]”中是选择条件，“~”代表排除
#print(data.shape)
#print(unuse.shape)
"""
(62988, 44)
(41516, 44)
(21472, 44)
直接筛掉两万多条"""
#print(data.isnull().any())
#print(data.isnull().sum())