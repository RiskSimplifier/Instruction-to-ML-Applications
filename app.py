from pathlib import Path

import streamlit as st
from PIL import Image
import base64
from streamlit import components


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
template_file = current_dir / "assets" / "Training Data Format.csv"
f_format = current_dir / "assets" / "format.gif"
f_save = current_dir / "assets" / "save.gif"
f_number = current_dir / "assets" / "number.gif"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Instructions"
PAGE_ICON = ":wave:"



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(template_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
#profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
# col1, col2 = st.row(2, gap="small")
# with col1:
#     st.image(profile_pic, width=230)

# with col2:
st.title("READ THIS BEFORE USING THE AML APPLICATION !!!")
st.write('\n')
st.write('\n')
st.subheader("1. Download the Training Data Format. ")
st.download_button(
    label=" 📄 Download Template",
    data=PDFbyte,
    file_name=template_file.name,
    mime="application/octet-stream",
)


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("2. Ensure the Risk Rating of Accounts are included as well as the last column should be STR.")
st.write(
    """
- ✔️ You can add as many numerical parameters you like.
- ✔️ 0 refers to the account which you did not found suspicious, while 1 refers to accounts that you have found suspicious
- ✔️ Ensure that no data are missing in any of rows, use 0 is to indicate null values.
"""
)
st.image("https://learnwithsiorik.com/wp-content/uploads/2023/05/template.gif", # I prefer to load the GIFs using GIPHY
            width=800, )
st.write('\n')
st.write('\n')
st.subheader("2. Ensure that all numerical figures in the file is converted to numbers.")
st.image("https://learnwithsiorik.com/wp-content/uploads/2023/05/number.gif", # I prefer to load the GIFs using GIPHY
            width=650, )

st.write('\n')
st.write('\n')
st.subheader("3. Don't forget to save the file as csv format.")

st.image("https://learnwithsiorik.com/wp-content/uploads/2023/05/format.gif", # I prefer to load the GIFs using GIPHY
            width=650, )
st.write('\n')
st.write('\n')
st.subheader("5. For the rest of procedures, please follow the steps in the following video.")

    
st.video('https://youtu.be/Dz1hcFskWio') 
    


st.write('\n')
st.subheader("4. if you have any suggestion, feedback or question, please mail at megalosnarik[@]gmail[.]com.")


#4545497