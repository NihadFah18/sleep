import streamlit as st
from save_data import save_data

st.set_page_config(page_title="Formulaire Sommeil", layout="wide")
st.markdown("""
    <style>
    #    .stApp {
    #         background-color: #f2f2f2;
    #     }
        body {
            background-color: #f2f2f2;
        }
        .image-container{
            width: 100%;
            object-fit: cover;
            border-radius: 15px;
            text-align: center;
            margin-top:180px;
        }
         .image-container img {
            width: 100%;
            height: 800px;
            object-fit: cover;
            border-radius: 15px;
        }
    </style>
""", unsafe_allow_html=True)
left_col, right_col = st.columns([1.2, 1.5], gap="large")

with left_col:
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.image("quality.jfif", use_container_width=True) 
    st.markdown('</div>', unsafe_allow_html=True)

with right_col:
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    st.header("Comment se porte votre sommeil ?")

    with st.form("form_sommeil"):
        fullname = st.text_input("Nom complet")
        age = st.text_input("Âge")
        genre = st.selectbox("Genre", ["Homme", "Femme"])
        duree_sommeil = st.text_input("Durée de sommeil (en heures)")
        stress = st.selectbox("Niveau de stress (1 à 10)", list(range(1, 11)))
        trouble = st.selectbox("Trouble du sommeil", ["Aucun", "Insomnie", "Apnée du sommeil"])
        bmi_category = st.selectbox("Catégorie d'IMC", ["Underweight", "Normal", "Overweight", "Obese"])

        submitted = st.form_submit_button("Soumettre")


        if submitted:
            save_data(fullname,age,genre,duree_sommeil,stress,trouble,bmi_category)
            st.success("✅ Formulaire soumis avec succès !")
    st.markdown('</div>', unsafe_allow_html=True)
