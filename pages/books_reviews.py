import streamlit as st
import pandas as pd
import plotly.express as px

# Config da tabela para ser wide
st.set_page_config(layout="wide")

# Atribuicao de variaveis a funcao de ler do pandas
df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

# SelectBox
books = df_top100_books["book title"].unique()
book = st.sidebar.selectbox("books", books)

# Reviews - Titulo
df_book = df_top100_books[df_top100_books["book title"] == book]
df_reviews_f = df_reviews[df_reviews["book name"] == book]

book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

st.title(book_title)
st.subheader(book_genre)
col1, col2, col3 = st.columns(3)

col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year of Publication", book_year)

st.divider()

# Reviews - Mensagem
for row in df_reviews_f.values:
    message = st.chat_message(f"{row[4]}")
    message.write(f"**<span style='font-size:26px'>\"{row[2]}\"</span>**", unsafe_allow_html=True)
    message.write(row[5])






