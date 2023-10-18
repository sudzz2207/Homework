import pandas as pd
df= pd.read_csv("cervical-cancer_csv.csv")
df.dropna(inplace=True)
df.drop(['Smokes (packs/year)'], axis=1,inplace=True)
df.drop(['STDs:AIDS'],axis=1, inplace=True)
df.to_csv("processed_cervicalcancer.csv")
