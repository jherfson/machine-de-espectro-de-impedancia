import pandas as pd
import numpy as np
import streamlit as st
import joblib as jb
import matplotlib.pyplot as plt
from yellowbrick.style.palettes import PALETTES, SEQUENCES, color_palette
from yellowbrick.style import set_palette
import seaborn as sns

set_palette('paired')
sns.set(font_scale = 1.0)

modelo = jb.load('modelo.pkl')

rotulo_collection = [
    'RC', 
    'RQ', 
    'RQRQ_RQ', 
    'RQRQ_RQ_Q', 
    'RQ_Q', 
    'RQ_RQ', 
    'R_L_RQ', 
    'R_L_RQ_Q', 
    'R_L_RQ_RQ', 
    'R_RQ', 
    'R_RQ_RQ'
]

st.set_page_config(page_title='Espectro de impedância', page_icon='🔋')
st.markdown('## Espectro de Impedância Eletroquímico 🔋 🪫')
# st.sidebar.header('Espectro de Impedância Eletroquímico')

arquivo = st.file_uploader(
    'Suba o seu arquivo aqui!',
    type=['csv', 'txt']
)

if arquivo is not None:
    colunas = ['f', "Z'", 'Z"']
    espectro = pd.read_csv(arquivo, sep=' ', names=colunas) 
    espectro_serie = pd.concat([espectro.iloc[:, i] for i in range(len(espectro.columns))])
    espectro_serie_ = np.array(espectro_serie, dtype='float32')
    predicao = modelo.predict_proba([espectro_serie_])[0]
    st.markdown('### ⚡️ O modelo do circuito é :')
    st.warning(rotulo_collection[predicao.argmax()])

    # plot
    fig, ax = plt.subplots(figsize=(12, 12), dpi=100)
    plt.scatter(espectro["Z'"], espectro['Z"'], s=55, alpha=0.57)
    ax.set_title('Espectro')
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel("Z'(Ω)", fontsize=18)
    plt.ylabel('-Z"(Ω)', fontsize=18)
    ax.invert_yaxis()
    st.pyplot(fig)
    
    # Tabela
    st.dataframe(espectro)
