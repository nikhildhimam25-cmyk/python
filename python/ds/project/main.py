import streamlit as st 
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px 
import base64 
import seaborn as sns
import matplotlib.pyplot as plt 


st.set_page_config(page_title="HOME",page_icon="🌾")
st.title('MADYA PRADESH 2026 CROPS ARRIVAL PRICES ')
col1,col2,col3=st.columns(3)
with col1:
 st.image("images.jfif")
 st.image("download (1).jfif")
 with col2:
  st.image("download (2).jfif")
  st.image("images (2).jfif")
  with col3:
   st.image("images (3).jfif")
   st.image("images (4).jfif")
st.write("𝗖𝗥𝗢𝗣𝗦")
st.write("Crop prices play an important role in the lives of farmers and consumers. They depend on factors such as weather conditions, availability of water, cost of seeds and fertilizers, and market demand. When production is high, prices usually fall, while low production can lead to higher prices. Fair and stable crop prices help farmers earn a good income and ensure that food remains affordable for everyone.")
st.write("𝗛𝗢𝗪 𝗙𝗔𝗥𝗠𝗘𝗥𝗦 𝗛𝗘𝗟𝗣 𝗦𝗢𝗖𝗜𝗘𝗧𝗬")
im1,im2=st.columns(2)
with im1:
 st.image("images (5).jfif") 
with im2:
 st.image("images (8).jfif") 
st.write("Farmers are fundamental to the survival and progress of society. Through their constant labor, they provide the food that sustains populations and supports economic stability. Their contribution extends beyond agriculture, strengthening communities and ensuring food security for present and future generations.")
st.write("𝗜𝗡𝗙𝗟𝗔𝗧𝗜𝗢𝗡 𝗢𝗡 𝗖𝗥𝗢𝗣𝗦")
im4,im3=st.columns(2)
with im3:
 st.image("images (7).jfif") 
with im4:
 st.image("download (3).jfif") 
st.write(" Inflation has a significant impact on crops by increasing the cost of seeds, fertilizers, fuel, and farm equipment. As production expenses rise, farmers are forced to sell their crops at higher prices to avoid losses. This leads to increased food prices in markets, affecting consumers and reducing affordability. Inflation also makes it difficult for farmers to invest in better technology, which can limit productivity and long-term agricultural growth")
st.write("𝗖𝗥𝗢𝗣𝗦 𝗚𝗥𝗢𝗪𝗡 𝗜𝗡 𝗠𝗔𝗗𝗛𝗬𝗔 𝗣𝗥𝗔𝗗𝗘𝗦𝗛")
t1,t2=st.columns(2)
with t1:
 st.write("𝗖𝗮𝘁𝗲𝗴𝗼𝗿𝘆")
 st.write("Cereals ")
 st.write("Pulses")
 st.write(" Oilseeds")
 st.write("Fibre Crops")
 st.write("vegetables")
with t2:
 st.write("𝗖𝗥𝗢𝗣𝗦")
 st.write("Wheat, Rice, Maize, Sorghum (Jowar), Barley")
 st.write("Potato, Tomato, Onion, Brinjal, Cabbage")
 st.write("Chickpea (Gram), Lentil (Masoor), Pigeon Pea (Arhar/Tur), Moong")
 st.write("Soybean, Groundnut, Mustard, Sunflower")
 st.write("Cotton, Jute")

# with open('download.jfif','rb') as f:
#     file=f.read()
# img =  base64.b64encode(file).decode()

# css=f"""
#     <style>
#     [data-testid="stAppViewContainer"]{{
#         background-image:url('data:image/png;base64,{img}');
#         background-size:cover
#     }}
#     </style>"""
# st.markdown(css, unsafe_allow_html=True)