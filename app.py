# Creating your first streamlit application
import streamlit as st
import pandas as pd
import numpy as np


# Give a title and writeup
st.title("My Data Science App")
st.write("Hello Tanzania")

# Components
# Text Elements : Headers, Subheader, Title
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Text and Markdowns
st.text("This is a plain text")

# Markdowns
st.markdown("## Markdown Formatting")
st.markdown("*Italics* and **Bold** text")

# Caption
st.caption("This is a caption with small text")

# Displaying some dataframe
df = pd.DataFrame({
    "Name": ["John", "Grace", "James"],
    "Age" : [40, 23, 53],
    "City" : ['Kisumu', "Dodoma", "Mombasa"]
})
# Display the df as an interactive table
st.dataframe(df)

# Display as a static table 
st.table(df)

# Diplay as row - json
st.json(df.to_dict())

# getting input 
# Text input
name = st.text_input("Enter your name", "Guest")
st.write(f"Hello, {name}!")

# Number input
age = st.number_input("What is your age?", min_value=0, max_value=120, step = 1)

# Text area for longer text
message = st.text_area("Leave your message here", "Type somethhing...")

# Selection widget
# Checkbox
if st.checkbox("Show Data"):
    st.write("Data is visioble")

# Radio button
option = st.radio("Choose an option", ["Opt 1", "opt2"])

# Select box
selected = st.selectbox('Choose a City', ["New York", 'Nairobi', 'Dodoma', "Arusha"])

# Slider 
age = st.slider("Selllect age", 0, 100, 25)

# button
if st.button("Click Me"):
    st.write("Button Clicked")

# Side bar
st.sidebar.header("Side bar header")
selected_page = st.sidebar.radio("Navigation", ['Home', "Ddata", "About"])

if selected_page == "Home":
    st.write("Home Page Content is here")
elif selected_page == "Ddata":
    st.markdown("[Customer](https://desmondonam-nps-application-app-v3i927.streamlit.app/)")
else:
    st.write("This is about page content")


# Charts and visualizations
# Sample data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ['a', 'B', "c"]
)

# Line chart
st.line_chart(chart_data)

# Area chart
st.area_chart(chart_data)

# Bar chart
st.bar_chart(chart_data)

st.subheader("Matplotlib Integration")
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.scatter([1,2,3,4,5], [10, 20, 30, 40, 50])
ax.set_title("Scatter Plot")
ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")

st.pyplot(fig)

# Integrating with plotly
st.subheader("Integrating with Plotly")
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x = "sepal_width", y = "sepal_length", color = "species")

st.plotly_chart(fig)


# Map
st.subheader("Maps")
map_data = pd.DataFrame({
    'lat' : [-1.76, -2.77,-3.78],
    'lon' : [34.4, 34.5, 34.41]
})

st.map(map_data)