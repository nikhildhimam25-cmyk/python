import streamlit as st 
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px 
import base64
import seaborn as sns
import matplotlib.pyplot as plt
st.set_page_config(page_icon="🧾",page_title="ABOUT")
st.title("ORIGNAL DATASET OF ALL INDIA CROPS")
st.link_button(label="CLICK HERE",url="https://agmarknet.gov.in/home")
# st.video("https://www.shutterstock.com/shutterstock/videos/3833711813/preview/stock-footage-aerial-view-of-beautiful-landscape-with-a-crop-sprayer-applying-pesticide-in-a-wheat-field-at.webm",autoplay=True)

import streamlit.components.v1 as components

video_url = "https://www.shutterstock.com/shutterstock/videos/3833711813/preview/stock-footage-aerial-view-of-beautiful-landscape-with-a-crop-sprayer-applying-pesticide-in-a-wheat-field-at.webm"

components.html(
    f"""
    <video autoplay muted loop playsinline width="100%">
        <source src="{video_url}" type="video/webm">
        Your browser does not support the video tag.
    </video>
    """,
    height=500,
)
# with st.form(key='key'):
#     col1,col2=st.columns(2)
#     with col1:
#      name=st.text_input("Name",placeholder="Enter your name")
#      num=st.number_input("number",placeholder="contact number")