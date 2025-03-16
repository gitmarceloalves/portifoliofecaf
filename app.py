import streamlit as st
import pandas as pd
import plotly.express as px
from supabase import create_client
import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

# Configurar Supabase com variáveis do .env
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Verificar se as credenciais estão configuradas corretamente
if not SUPABASE_URL or not SUPABASE_KEY:
    st.error("Erro: As credenciais do Supabase não foram encontradas no .env")
    st.stop()

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("Dashboard com Supabase e Streamlit")                          

# Buscar dados do Supabase
@st.cache_data
def get_data():
    try:
        response = supabase.table("iot_temp").select("*").execute()
        if not response.data:
            return pd.DataFrame()
        return pd.DataFrame(response.data)
    except Exception as e:
        st.error(f"Erro ao buscar dados: {e}")
        return pd.DataFrame()

df = get_data()

# Garantir que temos dados antes de continuar
if df.empty:
    st.warning("Nenhum dado encontrado no Supabase.")
    st.stop()

# Converter coluna de data para datetime
df["noted_date"] = pd.to_datetime(df["noted_date"])

# Criar seletor de tipo de gráfico
chart_type = st.selectbox("Escolha o tipo de gráfico", ["Barras", "Linha", "Dispersão"])

# Gerar o gráfico com base na escolha do usuário
if chart_type == "Barras":
    fig = px.bar(df, x="noted_date", y="temp", title="Gráfico de Barras")
elif chart_type == "Linha":
    fig = px.line(df, x="noted_date", y="temp", title="Gráfico de Linha")
elif chart_type == "Dispersão":
    fig = px.scatter(df, x="noted_date", y="temp", title="Gráfico de Dispersão")

st.plotly_chart(fig)

st.title("UNIFECAF") 
st.text("Portfólio criado com Supabase e Streamlit")
st.text("Aluno: Marcelo Antônio Alves")
