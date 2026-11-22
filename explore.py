import pandas as pd

df = pd.read_parquet("pozo_night_2020-02-22.parquet")
print(df.shape)
print(df.columns.tolist())
print(df.head())
print(df["in_box"].sum())
print(df["x_m"].nunique(), df["y_m"].nunique())
print(df["time_utc"].min(), df["time_utc"].max())