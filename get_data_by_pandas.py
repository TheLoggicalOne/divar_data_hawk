import pandas as pd

# Login using e.g. `huggingface-cli login` to access this dataset
# df = pd.read_csv("hf://datasets/divaroffical/real_estate_ads/real_estate_ads.csv")
# df.to_csv("real_estate_ads.csv")

df = pd.read_csv("real_estate_ads.csv")
print(df.head())
print(df.columns)
print(df.info())
print(df.describe())