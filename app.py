import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Titre de l'application
st.set_page_config(page_title="Exemple d'application Streamlit")
st.title("Bienvenue dans mon application Streamlit !")

# Sidebar avec des options
st.sidebar.title("Menu")
option = st.sidebar.selectbox("Choisissez une option", ["Afficher les données", "Visualiser un graphique"])

# Affichage des données
if option == "Afficher les données":
    st.header("Voici un jeu de données")
    data = pd.DataFrame({
        "Nom": ["Alice", "Bob", "Charlie", "David"],
        "Age": [25, 32, 19, 45],
        "Ville": ["Paris", "New York", "Londres", "Tokyo"]
    })
    st.write(data)

# Visualisation de données
elif option == "Visualiser un graphique":
    st.header("Voici un graphique simple")
    data = pd.DataFrame({
        "Catégorie": ["A", "B", "C", "D"],
        "Valeur": [10, 20, 15, 30]
    })
    fig, ax = plt.subplots()
    ax.bar(data["Catégorie"], data["Valeur"])
    ax.set_title("Graphique à barres")
    st.pyplot(fig)

# Bouton d'action
if st.button("Cliquez ici"):
    st.write("Vous avez cliqué sur le bouton !")
