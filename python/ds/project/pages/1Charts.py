import streamlit as st 
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px 
import base64
import seaborn as sns
import matplotlib.pyplot as plt 
st.set_page_config(page_icon='📊',page_title="CHARTS")
st.title('MADYA PRADESH 2026 CROPS ARRIVAL PRICES ')
df=pd.read_csv("Marketwise_Price_Arrival_05-01-2026_02-00-10_PM.csv")
df.rename(columns={"Unnamed: 0":"Commodity Group","Unnamed: 1":"Commodity","Unnamed: 2":"MSP (Rs./Quintal) 2026-27","Unnamed: 3":"Price on 03 Jan, 2026","Marketwise Price & Arrival Report (03-01-2026)":"Price on 02 Jan, 2026","Unnamed: 5":"Price on 01 Jan, 2026","Unnamed: 6":"Arrival on 03 Jan, 2026","Unnamed: 7":"Arrival on 02 Jan, 2026","Unnamed: 8":"Arrival on 01 Jan, 2026"},inplace=True)
df.drop([0,1],inplace=True)
df
var=df.loc[:,"Commodity Group"].value_counts().index
with st.sidebar:
    select=st.selectbox(label="select Commodity",options=var)
df_sel=df[df.loc[:,"Commodity Group"]==select]
# tar=df[df["Commodity Group"]=="Cereals"].index
char=px.pie(df_sel,values="Price on 01 Jan, 2026",names="Commodity",title="𝗣𝗿𝗶𝗰𝗲𝘀 𝗼𝗻 𝗡𝗲𝘄 𝗬𝗲𝗮𝗿")
st.plotly_chart(char)
char=px.pie(df_sel,values="Price on 02 Jan, 2026",names="Commodity",title="𝗣𝗿𝗶𝗰𝗲𝘀 𝗼𝗻 2𝗻𝗱 𝗝𝗮𝗻𝘂𝗮𝗿𝘆")
st.plotly_chart(char)
char=px.pie(df_sel,values="Price on 03 Jan, 2026",names="Commodity",title="𝗣𝗿𝗶𝗰𝗲𝘀 𝗼𝗻 3rd 𝗝𝗮𝗻𝘂𝗮𝗿𝘆")
st.plotly_chart(char)

char=px.scatter(data_frame=df, x="Commodity Group", y='MSP (Rs./Quintal) 2026-27', color="Commodity",title="𝗠𝗦𝗣 𝗢𝗙 𝗗𝗜𝗙𝗙𝗘𝗥𝗘𝗡𝗧 𝗖𝗢𝗠𝗠𝗢𝗗𝗜𝗧𝗜𝗘𝗦 𝗙𝗢𝗥𝗘𝗖𝗔𝗦𝗧 𝗙𝗢𝗥 2026–2027 𝗣𝗘𝗥 𝗤𝗨𝗜𝗡𝗧𝗔𝗟")
st.plotly_chart(char)


char1=px.bar_polar(df,r="Arrival on 01 Jan, 2026",theta="Commodity Group",color="Commodity Group",title="𝗤𝗨𝗔𝗡𝗧𝗜𝗧𝗬 𝗔𝗥𝗥𝗜𝗩𝗘𝗗 𝗢𝗡 𝗡𝗘𝗪 𝗬𝗘𝗔𝗥 𝗔𝗖𝗖𝗢𝗥𝗗𝗜𝗡𝗚 𝗧𝗢 𝗖𝗢𝗠𝗠𝗢𝗗𝗜𝗧𝗬 𝗚𝗥𝗢𝗨𝗣")
st.plotly_chart(char1)

char3=px.scatter(df,x="Commodity",y="Arrival on 01 Jan, 2026",title="𝗤𝗨𝗔𝗡𝗧𝗜𝗧𝗬 𝗔𝗥𝗥𝗜𝗩𝗘𝗗 𝗢𝗡 𝗡𝗘𝗪 𝗬𝗘𝗔𝗥",color="Commodity")
st.plotly_chart(char3)

char2=px.scatter_3d(df,x="Arrival on 03 Jan, 2026",y="Arrival on 02 Jan, 2026",z="Arrival on 01 Jan, 2026",color="Commodity",title="𝗗𝗜𝗙𝗙𝗘𝗥𝗘𝗡𝗖𝗘 𝗢𝗙 𝗤𝗨𝗔𝗡𝗧𝗜𝗧𝗬 𝗢𝗡 𝗝𝗔𝗡 𝟭, 𝗝𝗔𝗡 𝟮 𝗔𝗡𝗗 𝗝𝗔𝗡 𝟯 𝗜𝗡 𝗧𝗢𝗡")
st.plotly_chart(char2)

