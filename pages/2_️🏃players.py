import streamlit as st

from lib import utilities as util

util.config_pages()
st.header("Página de Jogadores")

df_data = st.session_state["data"]

clubes = df_data["Club"].unique()
club = st.sidebar.selectbox("Clube", clubes)
df_players = df_data[(df_data["Club"] == club)]
players = df_players["Name"].unique()
player = st.sidebar.selectbox("Jogador", players)

