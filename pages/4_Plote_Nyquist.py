import pandas as pd
import streamlit as st
import plotly.graph_objects as go


def import_csv(df):
    csv = pd.read_csv(df)
    return csv 

bar = st.sidebar

escolha = bar.selectbox(
    'Escolha um categoria',
    ['RQ_RQ', 'RQRQ_Q']
)

if escolha == 'RQ_RQ':
    path='amostra_RQ_RQ'
    rq_rq = import_csv(path)
    st.dataframe(rq_rq)



