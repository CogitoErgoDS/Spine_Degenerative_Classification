"""
    This  python script is related to the Eda part of our Streamlit Web App.
"""

### Import libraries
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# this is how we import streamlit
import streamlit as st


st.title('Penguins 🐧')
st.image('penguins.png')
st.markdown('*These are our lovely penguins that lives on Palmer Island in Antartide*')

st.header('About Penguins')

penguins = pd.read_csv("data/penguins_pimped.csv")
# Let's add a filter for getting data based on island
islands = penguins['island'].unique().tolist()
user_island = st.sidebar.selectbox(label="Where do you Want to Waddle?",options=islands)

if st.checkbox(label='Do you really want to Waddle?'):
    filtered_penguins = penguins[penguins['island'] == user_island]
    #st.dataframe(penguins)
    st.dataframe(filtered_penguins)
st.header('Plotting 🐧')
 
 

figure = px.scatter(
    data_frame=penguins, 
    x='bill_length_mm', 
    y='body_mass_g',
    color='island',
    title='Bill Length vs Bill Depth'
    )
st.plotly_chart(figure)     

st.write('___') 
kpi1,kpi2,kpi3 = st.columns(3)
kpi1.metric(label='AVG body mass', delta = +10,  value = 3000) 
kpi2.metric(label='AVG bill length', delta = -10, value = 3000)
kpi3.metric(label='AVG bill depth', value = 3000)
