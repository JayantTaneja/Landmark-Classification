import streamlit as st
from  PIL import Image
import torch
import torchvision.transforms as T
import numpy as np


def load_model():
    if "model" not in st.session_state:
        with st.spinner("Loading Model"):
            model_reloaded = torch.jit.load("checkpoints/transfer_exported3.pt")
            st.session_state.model = model_reloaded

        
def show_image(uploaded_file):
    image = Image.open(uploaded_file)
    st.image(image)
    

def classify_image(uploaded_image):
    image = Image.open(uploaded_image)
    image = T.ToTensor()(image).unsqueeze_(0)
    model = st.session_state.model
    
    softmax = model(image).data.cpu().numpy().squeeze()    
    
    # Get the indexes of the classes ordered by softmax
    # (larger first)
    idxs = np.argsort(softmax)[::-1]
    
    landmark_id = [0] * 5
    names = [0] * 5
    probs = [0] * 5

    # Loop over the classes with the largest softmax
    for i in range(5):
        # Get softmax value
        p = softmax[idxs[i]]
    
        # Get class name
        landmark_name = model.class_names[idxs[i]]
        
        landmark_id[i] = landmark_name[:2]
        names[i] = landmark_name[3::]
        probs[i] = (int(p*10000))/100

    
    st.markdown(f'''
    ### Predictions
    
    |    Landmard Id    |   Landmark Name    |      Probability       |
    |-------------------|--------------------|------------------------|
    |  {landmark_id[0]} |     {names[0]}     |        {probs[0]} %    |
    |  {landmark_id[1]} |     {names[1]}     |        {probs[1]} %    |
    |  {landmark_id[2]} |     {names[2]}     |        {probs[2]} %    |
    |  {landmark_id[3]} |     {names[3]}     |        {probs[3]} %    |
    |  {landmark_id[4]} |     {names[4]}     |        {probs[4]} %    |
    
    ''')