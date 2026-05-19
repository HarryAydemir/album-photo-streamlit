import streamlit as st
import pandas as pd

st.set_page_config(page_title="Album Photo", page_icon="🐒")

# Chargement des comptes depuis le CSV avec pandas
users = pd.read_csv("users.csv")

# Initialisation de l'état de connexion
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# Liste des photos de singes (URLs)
photos = [
    "https://placemonkeys.com/300/300",
    "https://placemonkeys.com/301/300",
    "https://placemonkeys.com/300/301",
    "https://placemonkeys.com/302/300",
    "https://placemonkeys.com/300/302",
    "https://placemonkeys.com/303/300",
]


def page_authentification():
    st.title("🔐 Authentification")
    nom = st.text_input("Nom d'utilisateur")
    mot_de_passe = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        ligne = users[(users["name"] == nom) & (users["password"] == mot_de_passe)]
        if not ligne.empty:
            st.session_state.logged_in = True
            st.session_state.username = nom
            st.rerun()
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect.")


def page_accueil():
    st.title("🏠 Page d'accueil")
    st.write(f"Bienvenue sur l'application, {st.session_state.username} !")
    st.write("Utilise le menu à gauche pour naviguer vers l'album photo.")


def page_album():
    st.title("🐒 Album photo des singes")
    # Affichage des images : 3 par ligne
    for i in range(0, len(photos), 3):
        colonnes = st.columns(3)
        for col, photo in zip(colonnes, photos[i:i + 3]):
            col.image(photo, use_container_width=True)


# --- Logique principale ---
if not st.session_state.logged_in:
    page_authentification()
else:
    # Barre latérale
    st.sidebar.write(f"Bienvenue {st.session_state.username}")
    menu = st.sidebar.radio("Menu", ["Accueil", "Album photo"])

    if st.sidebar.button("Déconnexion"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

    if menu == "Accueil":
        page_accueil()
    else:
        page_album()
