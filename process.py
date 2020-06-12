import pandas as pd
import numpy as np

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
#选择所需的列
data_need = data[['FFP_DATE','LOAD_TIME','FLIGHT_COUNT','SEG_KM_SUM','LAST_TO_END','avg_discount']]
#print(data_need.head(5))
#print(data_need.dtypes)
"""
FFP_DATE         object
LOAD_TIME        object
FLIGHT_COUNT      int64
SEG_KM_SUM        int64
LAST_TO_END       int64
avg_discount    float64
dtype: object
时间是对象类型，格式为 年/月/日"""
#转换类型，助于下一步的处理
data_need.FFP_DATE = pd.to_datetime(data_need.FFP_DATE)
data_need.LOAD_TIME =pd.to_datetime(data_need.LOAD_TIME)
#DataFrame对象.任意列可以选择这一列的所有数据
#pd.to_datetime()可以将格式正确的对象转换为datatime64[ns]类对象
#print(data_need.head(5))
#print(data_need.dtypes)
data_need['LL'] = data_need['LOAD_TIME'] - data_need['FFP_DATE']
#没有某列时DataFrame['列名']会创造新的列
#datetime64[ns]相减后会得到一个timedelta64[ns]类的对象
#将'LL'中的数据转换为int类型
data_need['LL'] = data_need['LL'].apply(lambda x:int(x.days))
#print(data_need.dtypes)
#print(data_need.head(5))
data_op = data_need[['FFP_DATE','LOAD_TIME','FLIGHT_COUNT','SEG_KM_SUM','LAST_TO_END','avg_discount','LL']]
#print(data_op.describe())
#print(data_op.head(3))
data_op.columns = ['FFP','LOAD','F','M','R','C','L']
#print(data_op.head(3))
#数据标准化
#将A的一个原始值x通过min-max标准化映射成在区间[0,1]中的值x'，公式：新数据=（原数据-最小值）/（最大值-最小值）
data_op_s = data_op[['F','M','R','C','L']].apply(lambda x: (x-np.min(x))/ (np.max(x)-np.min(x)))
