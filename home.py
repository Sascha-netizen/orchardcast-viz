import streamlit as st


st.title("OrchardCast Test: 22 February 2020")

if st.button("Static Maps"):
    st.switch_page("static_page.py")
    
if st.button("Animation"):
    st.switch_page("animation_page.py")

