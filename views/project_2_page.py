import streamlit as st

st.header("Vizualite")

st.markdown(
    """
    <a href="https://vizualite-5mht3cvffhrg8jd2sedqn5.streamlit.app/" target="_blank">
        <button style="background-color:#620707; color:white; padding:10px 20px; border:none; border-radius:10px; cursor:pointer;">
            Deployed App
        </button>
    </a>
    """,
    unsafe_allow_html=True
)
st.write("\n________________________________________________________________________________________________________________________________")

st.subheader("Project Details:")
st.write("Overview:")
st.write(""" Vizualite is a simple and interactive data visualization tool built with Streamlit. It allows users to upload CSV or Excel files, filter the data based on multiple conditions, and create various types of visualizations. The tool also provides a summary of the data and allows users to download the filtered dataset.""")
st.write("Features:")
st.write("""
File Upload: Upload CSV or Excel files to analyze and visualize the data.

Data Preview: View the first few rows of the dataset to understand its structure.

Data Summary: Get a statistical summary of the dataset, including mean, median, and standard deviation.

Data Filtering: Filter the dataset based on selected values from each column.

Data Visualization: Generate various types of plots: Line Plot, Bar Plot, Scatter Plot, Histogram, Correlation, Heatmap,

Download Filtered Data: Download the filtered dataset as a CSV file for further analysis. 

How It Works File Upload: Upload a CSV or Excel file using the "Upload CSV or Excel file" button. The tool supports .csv and .xlsx file formats. 

Data Preview: After uploading, a preview of the first few rows of the dataset is displayed. 

Data Summary: A statistical summary of the dataset is provided, including key metrics like mean, median, standard deviation, etc. 

Data Filtering: Users can filter the data by selecting specific values for each column. Multiple filters can be applied simultaneously. 

Data Visualization: Choose the type of plot you want to generate: Line Plot: Plots a line chart with selected x and y-axis columns. Bar Plot: Creates a bar chart using the selected x and y-axis columns. 

- Scatter Plot: Generates a scatter plot with the selected columns. 

- Histogram: Displays the distribution of a selected column. 

- Correlation Heatmap: Shows the correlation matrix of the dataset. The visualizations are displayed directly within the app. 

- Download Filtered Data: After filtering the data, users can download the filtered dataset as a CSV file. """)

st.write("\n________________________________________________________________________________________________________________________________") 

st.subheader("Tech Stack:")
skills = ["Python", "Streamlit", "Pandas","Numpy"]

col1, col2, col3 = st.columns(3)
for i, skill in enumerate(skills):
    if i % 3 == 0:
        with col1:
            st.info(skill)
    elif i % 3 == 1:
        with col2:
            st.info(skill)
    else:
        with col3:
            st.info(skill)

st.write("\n________________________________________________________________________________________________________________________________")

st.markdown(
    """
    <a href="https://github.com/Ayaanjawaid/Vizualite" target="_blank">
        <button style="background-color:#620707; color:white; padding:10px 20px; border:none; border-radius:10px; cursor:pointer;">
            Github Repo
        </button>
    </a>
    """,
    unsafe_allow_html=True
)