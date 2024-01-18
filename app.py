import streamlit as st
import pandas as pd
import plotly.express as px

# Config da tabela para ser wide
st.set_page_config(layout="wide")

# Atribuicao de variaveis a funcao de ler do pandas
df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

# Criando Slider

price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max)
df_books = df_top100_books[df_top100_books["book price"] <= max_price]
df_books
