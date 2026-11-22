import streamlit as st
import plotly.express as px
import pandas as pd
from data import load_data


st.header("Static Maps")

df = load_data()
peak = pd.Timestamp("2020-02-23 07:00", tz="UTC")
df_peak = df[df["time_utc"] == peak]


st.subheader("Peak Map")
st.info("Temperature (t_cold_c, corrected for altitude and cold air) for each 100 m square of the 10 × 10 km study area at the 07:00 UTC peak on 23 February 2020, with blue below 0 °C and red above.")
peak_map = px.scatter(df_peak, x="x_m", y="y_m", color="t_cold_c", color_continuous_scale="RdBu_r", color_continuous_midpoint=0)
peak_map.update_yaxes(scaleanchor="x", scaleratio=1)
st.plotly_chart(peak_map)

st.subheader("Elevation Map")
st.info("Terrain height for the same squares, from the lowest ground (dark purple) to the highest (yellow).")
elevation_map = px.scatter(df_peak, x="x_m", y="y_m", color="elevation_m", color_continuous_scale="Viridis")
elevation_map.update_yaxes(scaleanchor="x", scaleratio=1)
st.plotly_chart(elevation_map)

st.subheader("Scatter Map")
st.info("Each dot is one square, showing that squares at the same height can differ by several degrees, so height alone does not explain the temperature pattern.")
scatter_map = px.scatter(df_peak, x="elevation_m", y="t_cold_c")
st.plotly_chart(scatter_map)
