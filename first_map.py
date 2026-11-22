import pandas as pd
import plotly.express as px

df = pd.read_parquet("pozo_night_2020-02-22.parquet")

# 1. Keep only rows inside the box
df = df[df["in_box"] == True]

# 2. Keep only the rows for the peak hour
peak = pd.Timestamp("2020-02-23 07:00", tz="UTC")
df = df[df["time_utc"] == peak]

# 3. print the shape; it should show (10,000, 13)
print(df.shape)

fig = px.scatter(df, x="x_m", y="y_m", color="t_cold_c", color_continuous_scale="RdBu_r", color_continuous_midpoint=0)
fig.update_yaxes(scaleanchor="x", scaleratio=1)
fig.show()

fig = px.scatter(df, x="x_m", y="y_m", color="elevation_m", color_continuous_scale="Viridis")
fig.update_yaxes(scaleanchor="x", scaleratio=1)
fig.show()

fig = px.scatter(df, x="elevation_m", y="t_cold_c")
fig.show()

