import streamlit as st
import requests


def converter_libra_para_real(valor_libra):
    try:
        resposta = requests.get('https://api.exchangerate-api.com/v4/latest/GBP')
        dados = resposta.json()
        cotacao = dados['rates']['BRL']
        valor_real = valor_libra * cotacao
        return valor_real
    except Exception as e:
        st.error(f"Erro: {e}")
        return None


def config_pages():
    st.set_page_config(
        page_title="FIFA23 OFFICIAL DATASET",
        page_icon="⚽",
        layout="wide",
    )
