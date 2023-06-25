import streamlit as st

st.set_page_config(
    page_title="Model Details", page_icon=None, layout="centered", 
    initial_sidebar_state="auto", menu_items=None)


st.markdown('''

## About the Model

The model used for classifying the landmarks utilizes transfer learning and is made up of 2 main components:

- Pretrained Backbone
- Fine Tuned Head

The details of the above components are as follows:

### Pre-Trained Backbone

The backbone for this model is the famous [ResNet-18](https://www.researchgate.net/figure/Original-ResNet-18-Architecture_fig1_336642248), which is a model built by Microsoft and pretrained on the [Image](https://www.image-net.org/) dataset  

<img src = "https://www.researchgate.net/profile/Sajid-Iqbal-13/publication/336642248/figure/fig1/AS:839151377203201@1577080687133/Original-ResNet-18-Architecture.png" width = 100%></img>

---


### Fine Tuned Head

The fine tuning is done on a stack of 2 ```Linear``` Layers with 256 Neurons each, and ```ReLU``` activation after the first layer
and ```Sigmoid``` activation after the second.


''', unsafe_allow_html = True)

st.image("pages/net.jpg")