import streamlit as st
from utils import load_model, show_image, classify_image

st.set_page_config(
    page_title="Classify", page_icon=None, layout="centered", 
    initial_sidebar_state="auto", menu_items=None)

st.title("Classify any image !")

load_model()

with st.form("classify_form"):
    
    st.write("Upload an image")
    uploaded_image = st.file_uploader("", type = ["png", "jpg", "jpeg"])
    submitted = st.form_submit_button("Classify")
    
    if submitted:
        if uploaded_image is not None:
            classify_image(uploaded_image)