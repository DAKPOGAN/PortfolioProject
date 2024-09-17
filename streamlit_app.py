import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Titre de l'application
st.title("Ma première application Streamlit")

# Ajouter du texte
st.write("Bienvenue dans cette application de démonstration!")

# Créer des données d'exemple
df = pd.DataFrame({
    'première colonne': [1, 2, 3, 4, 5],
    'deuxième colonne': [10, 20, 30, 40, 50]
})

# Afficher les données
st.subheader("Voici nos données:")
st.write(df)

# Créer un graphique
st.subheader("Et voici un graphique:")
fig = px.line(df, x='première colonne', y='deuxième colonne', title='Ligne simple')
st.plotly_chart(fig)

# Ajouter un widget interactif
option = st.selectbox(
    'Quelle est votre couleur préférée?',
    ['Rouge', 'Vert', 'Bleu'])

st.write('Votre couleur préférée est ', option)
