import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns

df = sns.load_dataset("penguins").dropna()

# Sidebar
st.sidebar.title("Filters")
species = st.sidebar.multiselect("Species", options=df["species"].unique(), default=df["species"].unique())
island = st.sidebar.selectbox("Island", options=df["island"].unique())

# Filtered data
filtered = df[(df["species"].isin(species)) & (df["island"] == island)]

# Main layout
st.title("Penguin Dashboard")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Bill Length vs Depth")
    fig1 = px.scatter(filtered, x="bill_length_mm", y="bill_depth_mm", color="species")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Body Mass Distribution")
    fig2 = px.histogram(filtered, x="body_mass_g", color="species", barmode="overlay")
    st.plotly_chart(fig2, use_container_width=True)

# Expandable section
with st.expander("See raw data"):
    st.dataframe(filtered)
