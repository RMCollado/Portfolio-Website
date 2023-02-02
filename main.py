import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Rich Collado")
    content = """
    Good day, I'm Rich, an IT specialist, and all around awsome fella. 
    Since 2003, I have been working with databases, networking equipment, 
    web development, and programming.
    """
    st.info(content)

content_2 = """
Below you can find some of the apps I have built in python. Feel free to contact me!
"""
st.write(content_2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]{row['url']}")

