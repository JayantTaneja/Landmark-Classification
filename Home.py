import streamlit as st

st.set_page_config(
    page_title="Home", page_icon=None, layout="centered", 
    initial_sidebar_state="auto", menu_items=None)

st.title("Landmark Classification And Tagging Web App")

st.markdown('''
---

This web app was made as a stand alone frontend for the Landmark Classification and tagging ML models
that I trained as part of Udacity's Machine Learning Nanodegree Scholorship program.

<img src = https://vitalflux.com/wp-content/uploads/2020/10/feed_forward_neural_network-1.gif, width = 100%></img>

To use this web app, simply click on the classify page in the side bar on the left, upload a photo,
and click classify

''', unsafe_allow_html = True)