#get to know the data beforen you change or analyzing
import pandas as pd
df=pd.read_csv("sales.csv")
print(df.head())
print(df.tail(3))
print(df.columns.tolist())