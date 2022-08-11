import pandas as pd

df = pd.read_csv("https://bit.ly/3kGDuKx", na_values="?")

df['starostne_kategorije'] = pd.cut(df["age"], bins=3, labels=("mladi", "srednjih_let", "stari"))
print(df.groupby(["starostne_kategorije"])["survived"].sum())