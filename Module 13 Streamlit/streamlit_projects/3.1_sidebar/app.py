import streamlit as st

st.sidebar.title("Sidebar Controls")
user_name = st.sidebar.text_input("Enter your name")
color = st.sidebar.selectbox("Choose a theme color:", ["Blue", "Green", "Orange"])