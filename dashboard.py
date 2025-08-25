# code/dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Sanctions Analysis Dashboard")
df = pd.read_csv('../data/sanctions_cleaned.csv')
st.write("Goal Frequency")
fig = px.bar(df['main goal(s)'].value_counts().reset_index(), x='index', y='main goal(s)')
st.plotly_chart(fig)
