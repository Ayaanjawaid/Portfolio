import streamlit as st

st.header("Brain Stroke Prediction")

st.write("\n________________________________________________________________________________________________________________________________")

st.subheader("Project Details:")

st.write("""- The project involved utilizing data from Kaggle and implementing five different models - Decision Tree, Random Forest, XGBoost, Logistic Regression, and KNN - for training and testing.

- The primary objective of the project was to predict the occurrence of a brain stroke based on various factors such as age, gender, blood pressure, and smoking habits. Through the implementation of different models, I aimed to identify the most accurate and efficient model for predicting strokes.

- To carry out the project, I utilized the popular data analysis tool, Google Colaboratory, which enabled me to work with large datasets and run complex algorithms using cloud-based resources.

- The project involved extensive data preprocessing, including data cleaning, and feature engineering, to ensure the models were fed with the most relevant and accurate data.

- After implementing and testing the five models, I was able to identify the Random Forest model as the most accurate and efficient model for predicting strokes, achieving an accuracy score of over 90%.

- Overall, this project was an excellent opportunity for me to hone my data analysis and machine learning skills while working on a real-world problem. I am excited to share my experience and insights on this project with others in the Data Science community. """)


st.write("\n________________________________________________________________________________________________________________________________") 

st.subheader("Tech Stack:")
skills = ["Python", "Matplotlib", "Pandas","Numpy"]

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
    <a href="https://github.com/Ayaanjawaid/Brain_Stroke_Prediction" target="_blank">
        <button style="background-color:#620707; color:white; padding:10px 20px; border:none; border-radius:10px; cursor:pointer;">
            Github Repo
        </button>
    </a>
    """,
    unsafe_allow_html=True
)