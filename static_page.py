import streamlit as st
import plotly.express as px
import pandas as pd
from data import load_data


st.header("Static Maps")

df = load_data()
peak = pd.Timestamp("2020-02-23 07:00", tz="UTC")
df_peak = df[df["time_utc"] == peak]


st.subheader("Peak Map")
peak_map = px.scatter(df_peak, x="x_m", y="y_m", color="t_cold_c", color_continuous_scale="RdBu_r", color_continuous_midpoint=0)
peak_map.update_yaxes(scaleanchor="x", scaleratio=1)
st.plotly_chart(peak_map)

st.subheader("Elevation Map")
elevation_map = px.scatter(df_peak, x="x_m", y="y_m", color="elevation_m", color_continuous_scale="Viridis")
elevation_map.update_yaxes(scaleanchor="x", scaleratio=1)
st.plotly_chart(elevation_map)

st.subheader("Scatter Map")
scatter_map = px.scatter(df_peak, x="elevation_m", y="t_cold_c")
st.plotly_chart(scatter_map)
