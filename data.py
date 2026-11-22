import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    df = pd.read_parquet("pozo_night_2020-02-22.parquet")
    df = df[df["in_box"] == True]
    return df