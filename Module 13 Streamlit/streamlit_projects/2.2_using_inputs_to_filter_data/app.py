import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
df = sns.load_dataset("penguins").dropna()

st.title("Penguin Explorer")

# Widget: Species selector
species = st.selectbox("Choose a species:", df["species"].unique())

# Widget: Show histogram toggle
show_hist = st.checkbox("Show histogram of bill lengths")

# Filter data based on input
filtered_df = df[df["species"] == species]

# Display filtered data
st.subheader(f"Data for {species} Penguins")
st.dataframe(filtered_df)

# Plot if checkbox is selected
if show_hist:
    fig, ax = plt.subplots()
    ax.hist(filtered_df["bill_length_mm"], bins=15, color="coral")
    ax.set_title(f"{species} Bill Lengths")
    st.pyplot(fig)
