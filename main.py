import streamlit as st
import pandas as pd
st.set_option('deprecation.showPyplotGlobalUse', False)
from Pages import train, plots, data, home, predict



pages = {
    "Home":home,
    "Data": data,
    "Plots": plots,
    "Train": train,
    "Predict": predict
}


st.sidebar.title("Navigation")
page = st.sidebar.radio("Pages", list(pages.keys()), key="sidebar")
if page == None:
    home.app()
else:
   pages[page].app()

















