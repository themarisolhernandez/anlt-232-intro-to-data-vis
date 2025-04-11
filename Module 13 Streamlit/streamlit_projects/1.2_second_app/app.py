import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Welcome to Streamlit")

st.write("This is a sample app to display data and charts.")

# Create a sample dataframe
df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [100, 150, 200, 80]
})

# Display dataframe
st.subheader("Sample Data")
st.dataframe(df)

# Create and display a chart
st.subheader("Bar Chart")
fig, ax = plt.subplots()
ax.bar(df['Category'], df['Value'], color="skyblue")
st.pyplot(fig)

# Add interactive text input
name = st.text_input("What's your name?", "Streamlit user")
st.write(f"Hello, {name}!")