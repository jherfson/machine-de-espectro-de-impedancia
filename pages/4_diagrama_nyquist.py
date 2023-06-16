import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go


st.set_page_config(page_title='Diagrama de Nyquist', page_icon='📈')

def plot(df, legend):
    fig = go.Figure()
    for i in range(len(df)):
        fig.add_trace(go.Scatter(
            x=df['Z_re'][i], 
            y=df['Z_im'][i],
            mode='markers',
            name=i,
            marker_size=10
        )
    )
    fig.update_layout(
        xaxis=dict(
            gridcolor='white', 
            gridwidth=2
        ),
        yaxis=dict(
            autorange='reversed',
            gridcolor='white',
            gridwidth=2
        ),
        autosize=True,
        width=900,
        height=900,
        legend_title_text=legend
    )
    fig.update_xaxes(title_text="Z'(Ω)")
    fig.update_yaxes(title_text='Z"(Ω)')
    st.plotly_chart(fig, theme=None, use_container_width=True)

bar = st.sidebar

escolha = bar.selectbox(
    'Escolha um modelo de circuito',
    ['RQ_RQ', 'RQRQ_RQ']
)

if escolha == 'RQ_RQ':
    rq_rq = pd.read_json('https://raw.githubusercontent.com/jherfson/machine-de-espectro-de-impedancia/main/dados/amostra_RQ_RQ.json')
    plot(rq_rq, legend='RQ_RQ')

    
    
if escolha == 'RQRQ_RQ':
    rqrq_rq = pd.read_json('https://raw.githubusercontent.com/jherfson/machine-de-espectro-de-impedancia/main/dados/amostra_RQRQ_RQ.json')
    plot(rqrq_rq, legend='RQRQ_RQ')



