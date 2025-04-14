import streamlit as st

st.title("Widget Demo")

# Slider
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"Your age is: {age}")

# Selectbox
language = st.selectbox("Favorite programming language:", ["Python", "R", "JavaScript"])
st.write(f"You selected: {language}")

# Text input
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

# Checkbox
if st.checkbox("Show more info"):
    st.write("Here is some extra information.")
