import pandas as pd
import plotly.express as px


df = pd.read_parquet("pozo_night_2020-02-22.parquet")

# 1. Keep only rows inside the box (10km by 10km)
df = df[df["in_box"] == True]

# 2. Find the highest and lowest t_cold_c
lowest = df["t_cold_c"].min()
highest = df["t_cold_c"].max()

print(lowest)
print(highest)

# 3. Build animation with temperature capped at +/- 5 C
print(df.shape)

anim = px.scatter(df, animation_frame="time_utc", x="x_m", y="y_m", color="t_cold_c", color_continuous_scale="RdBu_r", color_continuous_midpoint=0, range_color=[-5, 5])
anim.update_yaxes(scaleanchor="x", scaleratio=1)
anim.show()