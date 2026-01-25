import streamlit as st

row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with row2_col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")