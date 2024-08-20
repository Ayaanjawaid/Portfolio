import streamlit as st

from form.contact import contact_form

# Background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

st.title("About Me")

col1, col2 = st.columns(2, gap="small",  vertical_alignment="center")
with col1:
    st.image("./assets/AJ.jpg")
with col2:
    st.title("Ayan Jawaid", anchor=False)
    st.write("Junior Data Analyst | Python Developer | Proficient in data Vizualisation")
    
    
    if st.button("✉️ Contact Me "):
        show_contact_form()
    
    st.markdown(
    """
    <a href="https://drive.google.com/file/d/1BDkj7pIZ5uEcifOfk4RSQO9gStccByBp/view?usp=drive_link" target="_blank">
        <button style="background-color:#620707; color:white; padding:10px 20px; border:none; border-radius:10px; cursor:pointer;">
            Download My Resume
        </button>
    </a>
    """,
    unsafe_allow_html=True
)
    
        
st.write("\n")

st.write("""
Hello! I'm Ayan Jawaid, A highly motivated and detail-oriented MCA graduate with a strong foundation in Python, SQL, Tableau, and Excel. I am experienced in creating insightful data visualizations and leveraging generative AI to drive data-driven decision-making. Demonstrated the ability to analyze complex datasets, identify trends, and present actionable insights. Adept at collaborating with cross-functional teams to deliver impactful data solutions.
""")

st.write("\n")
st.write("\n")
st.write("\n")

st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - Python Developer: Developed Desktop Applications
    - Data Science Intern: Developing Data Science Applications
    - Data Visualization Specialist: Expertise in creating visually appealing data visualisations
    - Bachelor's Degree in Computer Application: Maulana Abul Kalam Azad University of Technology
    - Master's Degree in Computer Application: Maulana Abul Kalam Azad University of Technology
    - Training in Data Science & Machine Learning: SCALER
    """
)

st.write("\n")
st.write("\n")
st.write("\n")

st.write("\n")
st.subheader("Technical Skills", anchor=False)

# Create a list of skills
skills = ["Python", "MYSQL", "Data Visualization", "Machine Learning", 
          "Tableau", "Power BI","Git", "Web Scraping", "HTML", "CSS", "Advance-Excel"]

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
            
st.write("\n")
st.write("\n")
st.write("\n")

# SOCIAL LINKS    
st.header("Connect with Me")

st.write("You can connect with me on the following platforms:")

st.write(" ")

col1, col2, col3, col4, = st.columns(4)

with col1:
    st.markdown(
        """
        <a href="https://github.com/Ayaanjawaid">
        <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="40" height="40" >
        </a>
        """, unsafe_allow_html=True)

with col2:
    st.markdown(
        """
        <a href="https://www.linkedin.com/in/ayanjawaid/">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="40" height="40">
        </a>
        """, unsafe_allow_html=True)

with col3:
    st.markdown(
        """
        <a href="https://www.instagram.com/a.y.a.a.n_jawaid/">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174855.png" width="40" height="40">
        </a>
        """, unsafe_allow_html=True)
    
with col4:
    st.markdown(
        """
        <a href="https://public.tableau.com/app/profile/ayan.jawaid/vizzes">
        <img src="https://cdn.worldvectorlogo.com/logos/tableau-software.svg" width="40" height="40">
        </a>
        """, unsafe_allow_html=True)