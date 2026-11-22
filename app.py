import streamlit as st


home = st.Page("home.py", title="Home")
animation = st.Page("animation_page.py", title="Animation")
static = st.Page("static_page.py", title="Static maps")

pg = st.navigation([home, static, animation])
pg.run()
