import streamlit as st
from config import pagesetup as ps, sessionstates as ss
from apps import app1 as a1, app2 as a2, app3 as a3, app4 as a4

#0. Set page config
page_title = "MagicBook Creator"
page_icon = "📚"
page_layout = "wide"
page_sidebar = "collapsed"
st.set_page_config(
    page_title=page_title,
    page_icon=page_icon,
    layout=page_layout,
    initial_sidebar_state=page_sidebar
)

#1. Initialize Session states
if "initialized" not in st.session_state:
    st.session_state.initialized = True
    ss.initialize_session_states()


#2. Set Title
ps.set_title("MagicBook", "Creator")

#3. Set Tabs
app1, app2, app3, app4 = st.tabs(["Story Elements", "AI Creation", "Display Results", "Download"])
with app1:
    a1.run_app1()
with app2:
    a2.run_app2()
with app3:
    a3.run_app3()
with app4:
    a4.run_app4()