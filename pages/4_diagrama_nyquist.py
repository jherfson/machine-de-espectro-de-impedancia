import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import seaborn as sns


sns.set(font_scale = 1.0)

st.set_page_config(page_title='Diagrama de Nyquist', page_icon='📈')

@st.cache_data 
def plot(df, legend, colors):
    fig = go.Figure()
    for i in range(len(df)):
        fig.add_trace(go.Scatter(
            x=df['Z_re'][i], 
            y=df['Z_im'][i],
            mode='markers',
            name=i,
            marker_size=10,
            opacity=1.0,
            marker=dict(
                size=80
            ),
                         
        )
    )
    fig.update_traces(
        mode='markers', 
        marker=dict(
            sizemode='area', 
            sizeref=20, 
            line_width=0.5
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
        #autosize=True,
        width=1500,
        height=600,
        legend_title_text=legend,
        
    )
    fig.update_xaxes(title_text="Z'(Ω)", )
    fig.update_yaxes(title_text='Z"(Ω)', )
    st.plotly_chart(fig, theme=None, use_container_width=True)

bar = st.sidebar

escolha = bar.selectbox(
    'Escolha um modelo de circuito',
    ['RQ_RQ', 'RQRQ_RQ']
)

if escolha == 'RQ_RQ':
    rq_rq = pd.read_json('https://raw.githubusercontent.com/jherfson/machine-de-espectro-de-impedancia/main/dados/amostra_RQ_RQ.json')
    colors = list(range(0, len(rq_rq)))
    plot(rq_rq, legend='RQ_RQ', colors=colors)

    
    
if escolha == 'RQRQ_RQ':
    rqrq_rq = pd.read_json('https://raw.githubusercontent.com/jherfson/machine-de-espectro-de-impedancia/main/dados/amostra_RQRQ_RQ.json')
    colors = list(range(0, len(rqrq_rq)))
    plot(rqrq_rq, legend='RQRQ_RQ', colors=colors)



