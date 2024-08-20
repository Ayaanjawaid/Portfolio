import streamlit as st

st.header("Diwali Sales Analysis")
st.write("\n________________________________________________________________________________________________________________________________")
st.subheader("Project Details:")
st.write("""
Analyzed a Diwali sales dataset with 11,251 rows and 15 columns to uncover key insights and trends. 

The project involved:

- Data Cleaning: Removed unwanted columns, handled missing values, and converted data types using pandas.

- Exploratory Data Analysis (EDA): Conducted EDA using pandas, Matplotlib, and seaborn. Applied group by and aggregation functions to analyze key metrics.

- Visualization: Created bar plots, count plots, and summary statistics to effectively communicate findings.

Key Insights:

- Gender: Higher purchasing trends among females.

- Age Group: Most active buyers in the 26-35 age group.

- State: Top-performing states were Uttar Pradesh, Maharashtra, and Karnataka.

- Marital Status: Married women had the highest purchasing power.

- Occupation: Most buyers from IT, Aviation, and Healthcare sectors.

- Product Category: Top-selling categories were Food, Clothing, and Electronics. """)

st.write("\n________________________________________________________________________________________________________________________________") 

st.subheader("Tech Stack:")
skills = ["Python","Numpy","Pandas","Matplotlib","EDA", "Excel", ]

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
    <a href="https://github.com/Ayaanjawaid/Diwali-Sales-Analysis" target="_blank">
        <button style="background-color:#620707; color:white; padding:10px 20px; border:none; border-radius:10px; cursor:pointer;">
            Github Repo
        </button>
    </a>
    """,
    unsafe_allow_html=True
)