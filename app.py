import streamlit as st
import pandas as pd
import plotly.express as px

# Config da tabela para ser wide
st.set_page_config(layout="wide")

# Atribuicao de variaveis a funcao de ler do pandas
df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

# Slider
price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max)
df_books = df_top100_books[df_top100_books["book price"] <= max_price]
df_books

# Graficos 
fig = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])

col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)