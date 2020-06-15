import pandas as pd 
import numpy as np 
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

table = pd.read_csv("air_data.csv",sep=",",encoding="utf-8")
#print(table.head(5))
#print(table.shape)
table_clean = table[~((table.SUM_YR_1.isin([0]))|(table.SUM_YR_2.isin([0]))|(table.SEG_KM_SUM.isin([0]))|(table.avg_discount.isin([0])))]
#print(table_clean.shape)
#print(table_clean.dtypes)
table_need = table_clean[["FFP_DATE","LOAD_TIME","FLIGHT_COUNT","SEG_KM_SUM","LAST_TO_END","avg_discount"]]
#print(table_need.shape)
table_need.FFP_DATE =  pd.to_datetime(table_need.FFP_DATE)
table_need.LOAD_TIME =  pd.to_datetime(table_need.LOAD_TIME)
#print(table_need.dtypes)
table_need["LL"] = table_need["LOAD_TIME"] - table_need["FFP_DATE"]
table_need["LL"] = table_need["LL"].apply(lambda x: int(x.days))
#print(table_need.head(5))
table_final = table_need[["LAST_TO_END","FLIGHT_COUNT","SEG_KM_SUM","avg_discount","LL"]]
table_final.columns = ["R","F","M","C","L"]
#print(table_final.head(5))
table_final_s = table_final[["R","F","M","C","L"]].apply(lambda x: (x-np.min(x))/(np.max(x)-np.min(x)))
#print(table_final_s.head(5))
KM_model = KMeans(n_clusters=4,init="random",max_iter=500)
KM_model.fit(table_final_s)
r1 = pd.Series(KM_model.labels_).value_counts()
r2 = pd.DataFrame(KM_model.cluster_centers_)
cluster_C = pd.concat([r2,r1],axis=1)
cluster_C.columns = ["R","F","M","C","L","N"]
cluster_C.to_excel("cluster_C.xlsx")
result = pd.concat([table_final_s,pd.Series(KM_model.labels_,index=table_final_s.index)],axis=1)
result.columns = ["R","F","M","C","L","Cluster"]
result.to_excel("result_1.xlsx")
pca = PCA(n_components=2)
data = pd.DataFrame(pca.fit_transform(table_final_s))
d = data[KM_model.labels_==0]
plt.plot(d[0],d[1],"r*")
d = data[KM_model.labels_==1]
plt.plot(d[0],d[1],"go")
d = data[KM_model.labels_==2]
plt.plot(d[0],d[1],"b+")
d = data[KM_model.labels_==3]
plt.plot(d[0],d[1],"k+")
plt.show()