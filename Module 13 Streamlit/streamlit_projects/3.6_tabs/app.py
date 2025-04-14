import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns

df = sns.load_dataset("penguins").dropna()

# App title
st.title("Penguin Dashboard")

# Sidebar filters
st.sidebar.title("Filters")
species = st.sidebar.multiselect("Species", options=df["species"].unique(), default=df["species"].unique())
island = st.sidebar.selectbox("Island", options=df["island"].unique())

# Filtered data
filtered = df[(df["species"].isin(species)) & (df["island"] == island)]

# Create visualizations
fig1 = px.scatter(
    filtered,
    x="bill_length_mm",
    y="bill_depth_mm",
    color="species",
    title="Bill Length vs Depth",
)

fig2 = px.histogram(
    filtered,
    x="body_mass_g",
    color="species",
    barmode="overlay",
    title="Body Mass Distribution",
)

# Tabbed layout
tab1, tab2 = st.tabs(["Scatterplot", "Histogram"])

with tab1:
    st.write("This scatterplot shows the relationship between bill length and depth by species.")
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    st.write("This histogram shows the body mass distribution of penguins by species.")
    st.plotly_chart(fig2, use_container_width=True)
