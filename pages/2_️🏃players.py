import streamlit as st
import locale
from lib import utilities as util

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
util.config_pages()
st.header("Página de Jogadores")

df_data = st.session_state["data"]

clubes = df_data["Club"].unique()
club = st.sidebar.selectbox("Clube", clubes)
df_players = df_data[(df_data["Club"] == club)]
players = df_players["Name"].unique()
player = st.sidebar.selectbox("Jogador", players)

player_stats = df_data[df_data["Name"] == player].iloc[0]

st.image(player_stats["Photo"])
st.title(player_stats["Name"])


st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}m ")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)'] * 0.453:.2f}Kg")
st.divider()

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

col1, col2, col3, col4 = st.columns(4)
valor_mercado = locale.format_string('%1f', util.converter_libra_para_real(player_stats['Value(£)']), grouping=True)
col1.metric(label="Valor de mercado", value=f'R$ {valor_mercado}')
col2.metric(label="Remuneração semanal", value=f"R$ {util.converter_libra_para_real(player_stats['Wage(£)']):,}")
col3.metric(label="Cláusula de rescisão", value=f"R$ {util.converter_libra_para_real(player_stats['Release Clause(£)']):,}")

st.write(player_stats)
