import pandas as pd
import plotly.express as px
import streamlit as st
from data import load_data


st.header("Animation")

# 1. Data Loading: Animation
df = load_data()


# 2. Build animation with temperature capped at +/- 5 C
anim = px.scatter(df, animation_frame="time_utc", x="x_m", y="y_m", color="t_cold_c", color_continuous_scale="RdBu_r", color_continuous_midpoint=0, range_color=[-5, 5])
anim.update_yaxes(scaleanchor="x", scaleratio=1)
anim.update_layout(height=700)
st.plotly_chart(anim)