import pandas as pd 

table = pd.read_csv("air_data.csv",sep=",",encoding="utf-8")
#print(table.head(5))
#print(table.shape)
#print(table.info())
table_clean = table[~((table.SUM_YR_1.isin([0]))|(table.SUM_YR_2.isin([0]))|(table.SEG_KM_SUM.isin([0])|(table.avg_discount.isin([0]))))]
#print(table_clean.shape)
table_need = table_clean[["FFP_DATE","LOAD_TIME","FLIGHT_COUNT","SEG_KM_SUM","","avg_discount"]]