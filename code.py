import pandas as pd 
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt 

table = pd.read_csv("air_data.csv",sep=",",encoding="utf-8")
#print(table.head(5))
#print(table.shape)
#print(table.info())
table_clean = table[~((table.SUM_YR_1.isin([0]))|(table.SUM_YR_2.isin([0]))|(table.SEG_KM_SUM.isin([0])|(table.avg_discount.isin([0]))))]
#print(table_clean.shape)
table_need = table_clean[["FFP_DATE","LOAD_TIME","FLIGHT_COUNT","SEG_KM_SUM","LAST_TO_END","avg_discount"]]
table_need.FFP_DATE = pd.to_datetime(table_need.FFP_DATE)
table_need.LOAD_TIME = pd.to_datetime(table_need.LOAD_TIME)
#print(table_need.dtypes)
table_need["LL"] = table_need["LOAD_TIME"] - table_need["FFP_DATE"]
table_need["LL"] = table_need["LL"].apply(lambda x: int(x.days))
#print(table_need.dtypes)
table_final = table_need[["LAST_TO_END","FLIGHT_COUNT","SEG_KM_SUM","avg_discount","LL"]]
table_final.columns = ["R","F","M","C","L"]
#print(table_final.head(5))
table_final_s = table_final[["R","F","M","C","L"]].apply(lambda x: (x-np.min(x))/(np.max(x)-np.min(x)))
#print(table_final_s.head(5))
k = 4
iteration = 500
cluster_c = "random"
KM_models = KMeans(n_clusters=k,init=cluster_c,max_iter=iteration)
KM_models.fit(table_final_s)
r1 = pd.Series(KM_models.labels_).value_counts()
r2 = pd.DataFrame(KM_models.cluster_centers_)
#print(r2.head(4))
r2.columns = ["R","F","M","C","L"]
r = pd.concat([r2,r1],axis=1)
#print(r.head(4))
r.columns = ["R","F","M","C","L","numbers"]
r.to_excel("clusterCenter.xlsx")
result = pd.Series(KM_models.labels_,index=table_final_s.index)
cluster_result = pd.concat([table_final_s,result],axis=1)
cluster_result.to_excel("result.xlsx")
pca = PCA(n_components=2)
data = pd.DataFrame(pca.fit_transform(table_final_s))
d = data[KM_models.labels_==0]
plt.plot(d[0],d[1],'r*')            #红色
d = data[KM_models.labels_==1]
plt.plot(d[0],d[1],'go')            #绿色
d = data[KM_models.labels_==2]
plt.plot(d[0],d[1],'b+')            #蓝色
d = data[KM_models.labels_==3]
plt.plot(d[0],d[1],'k+')            #黑色
plt.show()