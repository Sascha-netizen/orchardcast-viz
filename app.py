import streamlit as st
import os
import hmac


password = os.environ.get("APP_PASSWORD")
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    entered = st.text_input("Password", type="password")
    if entered: 
        if password and hmac.compare_digest(entered.encode(), password.encode()):
            st.session_state["authenticated"] = True 
            st.rerun()
        else: 
            st.error("Wrong password")
    st.stop() 


    

home = st.Page("home.py", title="Home")
animation = st.Page("animation_page.py", title="Animation")
static = st.Page("static_page.py", title="Static maps")

pg = st.navigation([home, static, animation])
pg.run()
