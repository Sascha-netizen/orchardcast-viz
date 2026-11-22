import streamlit as st


st.title("OrchardCast Test: 22 February 2020")

if st.button(":green[Static Maps]"):
    st.switch_page("static_page.py")
    
if st.button(":red[Animation]"):
    st.switch_page("animation_page.py")

