import process as datas
import numpy as np 
import pandas as pd 
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt 

k = 4
iteration = 500
#建立模型
model_KMeans = KMeans(n_clusters=k,init='random',max_iter=iteration)
#迭代运算
model_KMeans.fit(datas.data_op_s)
#存储分类的结果，分类个数为行、一列为编号、一列为样本中的个数
r1 = pd.Series(model_KMeans.labels_).value_counts()
#存储每个类的均值属性
r2 = pd.DataFrame(model_KMeans.cluster_centers_)
#连接两个表
r = pd.concat([r2,r1],axis=1)
r.columns = list(datas.data_op_s.columns)+['类别的样本量']
#print(r)
#存储结果
"""
result_km = pd.concat([datas.data_op_s,pd.Series(model_KMeans.labels_,index=datas.data_op_s.index)],axis=1)
result_km.columns = list(datas.data_op_s.columns)+['聚类类别']
result_km.to_excel('result.xlsx')"""
#绘制聚类图
pca = PCA(n_components=2)
data = pd.DataFrame(pca.fit_transform(datas.data_op_s))
d = data[model_KMeans.labels_==0]
plt.plot(d[0],d[1],'r*')            #
d = data[model_KMeans.labels_==1]
plt.plot(d[0],d[1],'go')            #
d = data[model_KMeans.labels_==2]
plt.plot(d[0],d[1],'b+')            #
d = data[model_KMeans.labels_==3]
plt.plot(d[0],d[1],'k+')            #
plt.show()