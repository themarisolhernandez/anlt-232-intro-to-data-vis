import streamlit as st

col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.metric("Revenue", "$120K")
with col2:
    st.metric("Users", "3.2K")
with col3:
    st.metric("Churn", "5.3%")
