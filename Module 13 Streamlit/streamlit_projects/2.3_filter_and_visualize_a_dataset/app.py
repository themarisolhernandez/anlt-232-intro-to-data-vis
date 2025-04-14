import streamlit as st
import pandas as pd
import plotly.express as px

# Load built-in dataset
df = px.data.gapminder()

st.title("Gapminder Explorer")
st.markdown("Use the filters below to explore country-level data over time.")

# Year filter
year = st.slider("Select a year:", min_value=df["year"].min(), max_value=df["year"].max(), step=5, value=df["year"].max())

# Continent filter
continents = st.multiselect("Select continents:", options=df["continent"].unique(), default=["Asia", "Europe"])

# Filter the data
filtered_df = df[(df["year"] == year) & (df["continent"].isin(continents))]

# Show results
st.write(f"Showing data for {year} in {', '.join(continents)}")
st.dataframe(filtered_df)

# Bubble chart
fig = px.scatter(
    filtered_df,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    title=f"Life Expectancy vs GDP Per Capita ({year})"
)

st.plotly_chart(fig)
