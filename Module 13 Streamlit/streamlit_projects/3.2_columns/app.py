import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.header("Left Panel")
    st.write("This column could hold a data table or chart.")

with col2:
    st.header("Right Panel")
    st.write("This column could display user input or KPIs.")
