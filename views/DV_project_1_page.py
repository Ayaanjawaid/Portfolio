import streamlit as st

st.header("Super Store Interactive Dashboard")

st.markdown(
    """
    <a href="https://public.tableau.com/app/profile/ayan.jawaid/viz/SuperStoreInteractiveDashboard_17176142631760/SuperStoreInteractiveDashboard" target="_blank">
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
Super Store Interactive Dashboard is a comprehensive and dynamic visualization tool designed to provide in-depth insights into sales, profit, and quantity metrics. This project showcases the power of data visualization in transforming raw data into actionable business intelligence, enhancing decision-making processes.
Project Highlights:
         
- Dynamic Parameter Control:
Implemented radio buttons to switch between sales, profit, and quantity views, updating charts dynamically for tailored insights.

- Sub-Category and Category Analysis:
Visualized performance metrics at sub-category and category levels for detailed analysis of sales trends and profitability.

- Segment and Ship Mode Insights:
Analyzed sales, profit, and quantity across customer segments and shipping modes, aiding targeted marketing and logistics optimization.

- State-Level Performance:
Created state-wise visualizations to highlight regional performance variations, supporting strategic regional planning.

- Profit, Sales, and Quantity Trends:
Utilized line charts and trend analysis to track changes over time, identifying seasonal patterns and growth trends.

- Interactive Dashboards:
Developed an intuitive interface with tooltips, filters, and drill-down capabilities for deeper insights and data exploration.

This Super Store Interactive Dashboard showcases the potential of data visualization in driving business growth and efficiency. By leveraging advanced techniques and interactive elements, the dashboard offers a holistic view of key performance metrics, empowering stakeholders to make informed, strategic decisions.
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

image_path = "./assets/project-1.png" 
st.image(image_path, width=900, caption="Dashboard Screenshot")
