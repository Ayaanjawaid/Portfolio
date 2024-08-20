import streamlit as st

# pages setup
about_page = st.Page(
    page = "views/about_me.py",
    title = "About Me",
    icon = ":material/account_circle:",
    default = True,
) 

project_1_page = st.Page(
    page = "views/project_1_page.py",
    title = "Diwali Sale Analysis",
    icon = ":material/bar_chart:",
) 

project_2_page = st.Page(
    page = "views/project_2_page.py",
    title = "Vizualite",
    icon = ":material/smart_toy:",
) 

project_3_page = st.Page(
    page = "views/project_3_page.py",
    title = "Brain Stroke Prediction",
    icon = ":material/smart_toy:",
) 

DV_project_1_page = st.Page(
    page = "views/DV_project_1_page.py",
    title = "Super Store Interactive Dashboard",
    icon = ":material/bar_chart:",
)

DV_project_2_page = st.Page(
    page = "views/DV_project_2_page.py",
    title = "Australian Wine Sales Dashboard",
    icon = ":material/bar_chart:",
)

DV_project_3_page = st.Page(
    page = "views/DV_project_3_page.py",
    title = "Omega Hr Insights Dashboard",
    icon = ":material/bar_chart:",
)


pg = st.navigation(
    {
        "Info": [about_page],
        "Python Projects": [project_1_page, project_2_page, project_3_page],
        "Data Visualization Projects": [DV_project_1_page, DV_project_2_page, DV_project_3_page]
    }
)

st.logo("assets/Page_logo.png")
st.sidebar.text("Made with 💜 by Ayan")


pg.run()
