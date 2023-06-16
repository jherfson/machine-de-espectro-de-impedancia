import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go





bar = st.sidebar

escolha = bar.selectbox(
    'Escolha um categoria',
    ['RQ_RQ', 'RQRQ_Q']
)

if escolha == 'RQ_RQ':
    #rq_rq = pd.read_csv('https://raw.githubusercontent.com/jherfson/machine-de-espectro-de-impedancia/main/dados/amostra_RQ_RQ.csv')
    #rq_rq_Z_re_serie = pd.Series(rq_rq.Z_re)
    #rq_rq_Z_im_serie = pd.Series(rq_rq.Z_im)
    rq_rq = pd.read_json('/home/jherfson/Dropbox/Research_Jherfson/cnn_impedancia/amostra_RQ_RQ.json')

    fig = go.Figure()
    for i in range(len(rq_rq)):
        fig.add_trace(go.Scatter(
            x=rq_rq.Z_re[i], 
            y=rq_rq.Z_im[i],
            mode='markers',
            name=i,
        ))
    fig.update_layout(
        xaxis=dict(gridcolor='white', gridwidth=2),
        yaxis=dict(autorange='reversed', gridcolor='white', gridwidth=2),
        autosize=True,
        width=100,
        height=800,
        legend_title_text='Espectros_RQ_RQ'
    )
    fig.update_xaxes(title_text="Z'(Ω)")
    fig.update_yaxes(title_text='Z"(Ω)')
    # fig.show()
    st.plotly_chart(fig, theme=None, use_container_width=True)


    
elif escolha == 'RQRQ_RQ':
    rqrq_rq = pd.read_csv('https://raw.githubusercontent.com/jherfson/machine-de-espectro-de-impedancia/main/dados/amostra_RQRQ_RQ.csv')



