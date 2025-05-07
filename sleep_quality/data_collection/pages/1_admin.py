import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Admin", layout="wide")
st.title("🔐 Espace Administrateur")
PASSWORD = "nihad2003"  

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    password = st.text_input("Mot de passe", type="password")
    if st.button("Connexion"):
        if password == PASSWORD:
            st.success("Connexion réussie")
            st.session_state["authenticated"] = True
        else:
            st.error("Mot de passe incorrect")
else:
    st.subheader("📥 Télécharger les données des utilisateurs")

    if os.path.exists("data_sommeil.csv"):
        df = pd.read_csv("data_sommeil.csv")
        st.dataframe(df)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇️ Télécharger le fichier CSV",
            data=csv,
            file_name='data_sommeil.csv',
            mime='text/csv'
        )
    else:
        st.warning("Aucune donnée encore soumise.")
