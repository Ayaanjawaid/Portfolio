import streamlit as st 

st.header("Omega HR Insights Dashboard")

st.markdown(
    """
    <a href="https://public.tableau.com/app/profile/ayan.jawaid/viz/OmegaHrDashboard/OmegaHrInsightsDashboard" target="_blank">
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
- I developed this interactive HR dashboard, leveraging advanced data visualization techniques to provide insightful analysis and enhance decision-making processes. 
- The dashboard integrates various visual elements such as line graphs, histograms, pie charts, bar plots, and map plots to present comprehensive HR-related information.
- The hiring trends over time are depicted using a line graph, offering a clear visualization of recruitment patterns and enabling stakeholders to identify peaks and troughs in hiring activity. 
- An age distribution histogram provides a detailed view of the workforce's age demographics. By visualizing the age range, HR managers can identify generational gaps and implement targeted strategies for employee engagement, training, and succession planning.
- Gender distribution is illustrated using a pie chart, presenting a straightforward and easily interpretable visualization of gender diversity within the organization. 
- The distribution of employees across various departments is captured through a bar plot. This categorical data visualization allows for a comparative analysis of department sizes, helping in resource allocation and identifying departments with potential overstaffing or understaffing issues.
- Geographical distribution of employees is represented with a map plot, providing a spatial analysis of the workforce. By visualizing the data geographically, it is easier to identify regional concentrations of employees, which can inform decisions regarding regional office locations.

In summary, this HR dashboard harnesses the power of data visualization to transform raw data into actionable insights. The dashboard facilitates a holistic understanding of HR metrics, promoting data-driven decision-making and strategic planning. The integration of these visual tools not only enhances the interpretability of complex data but also supports the organization in achieving its HR objectives more efficiently.
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

image_path = "./assets/project-3.png" 
st.image(image_path, width=950, caption="Dashboard Screenshot")