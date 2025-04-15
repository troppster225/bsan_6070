import streamlit as st
import pandas as pd
import plotly_express as px
'''
# Club and Nationality App

Select your favorite club and player nationalities to see how their
age vs. their overall stacks up!
'''

df = st.cache_data(pd.read_csv)("football_data.csv")

clubs = st.sidebar.multiselect('Show Player for clubs?', df['Club'].unique())
nationalities = st.sidebar.multiselect('Show Player from Nationalities?', df['Nationality'].unique())
new_df = df[(df['Club'].isin(clubs)) &
(df['Nationality'].isin(nationalities))]

st.write(new_df)

# Create distplot with custom bin_size
fig = px.scatter(new_df, x ='Overall',y='Age',color='Name')

'''
### Here is a simple chart showing age vs. overall
'''

st.plotly_chart(fig)