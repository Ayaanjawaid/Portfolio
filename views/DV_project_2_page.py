import streamlit as st 

st.header("Australian Wine Sales Analysis")

st.markdown(
    """
    <a href="https://public.tableau.com/app/profile/ayan.jawaid/viz/AustralianWineSalesAnalysis_17172653609090/AustralianWineSalesAnalysis" target="_blank">
        <button style="background-color:#620707; color:white; padding:10px 20px; border:none; border-radius:10px; cursor:pointer;">
            View Dashboard
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

st.write("\n________________________________________________________________________________________________________________________________")
st.subheader("Project Details:")
st.write(""" 
The Australian Wine Sales Analysis dashboard, a comprehensive visualization tool designed to illuminate crucial insights within the wine sales domain. 

Here's a breakdown of its key components:

- Revenue by Sales Area and States: Gain a holistic understanding of market performance through detailed revenue breakdowns by sales area and states, facilitating targeted strategic planning.

- Dynamic Parameter Functionality: Implemented dynamic parameters allowing end-users to dynamically change values on the dashboard, enhancing flexibility and enabling tailored analyses based on specific criteria.

- Best Brands by Revenue Analysis: Utilized interactive tools to identify top-performing brands by revenue, providing valuable insights into brand performance and market dominance.

- Product Analysis by Revenue and Order Quantity: Leveraged scatter plots to analyze product performance based on revenue and order quantity relationships, offering nuanced insights into product profitability and popularity.

This dashboard represents a culmination of data visualization expertise aimed at empowering stakeholders with actionable insights to drive informed decision-making and strategic business growth within the Australian wine sales landscape.

   """)

st.write("\n________________________________________________________________________________________________________________________________") 

st.subheader("Tech Stack:")
skills = ["Tableau", "Advance-Excel"]

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

image_path = "./assets/project-2.png" 
st.image(image_path, width=900, caption="Dashboard Screenshot")