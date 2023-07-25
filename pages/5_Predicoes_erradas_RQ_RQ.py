import seaborn as sns
import plotly.graph_objects as go
import json, requests
import streamlit as st
from tqdm import tqdm


st.set_page_config(
    page_title='Predições erradas RQ_RQ',
    page_icon='📊'
)

st.write('## Predições erradas feita pelo modelo de Machine Learning!')
st.write('#### O modelo cometeu um erro ao afirmar que era RQ_RQ, porém a correção é que são RQRQ_RQ')


# importando os dados do gthub
url = 'https://raw.githubusercontent.com/jherfson/machine-de-espectro-de-impedancia/main/dados/resultados_preditos_errados.json'
resp = requests.get(url)
espectros = json.loads(resp.text)

# Temas do gráfico
sns.set_theme()
sns.set_style("darkgrid")
sns.set(font_scale=1.0)

# gerar o gráfico
fig = go.Figure()
for espectro in tqdm(range(len(espectros['RQ_RQ']))):
    fig.add_trace(go.Scatter(
        x = espectros['RQ_RQ'][espectro][181:362],
        y = espectros['RQ_RQ'][espectro][362:],
        mode='markers',
        marker_size=10,
        opacity=1.0,
        marker=dict(
        size=80
        ),
    ))

fig.update_layout(
    yaxis = dict(
        autorange='reversed'
    ),
    autosize=False,
    width=1500,
    height=600,
    legend_title_text='Espectro'
)

fig.update_traces(
    mode='markers',
    marker=dict(
        sizemode='area',
        sizeref=20,
        line_width=0.5
    )
)

fig.update_xaxes(title_text="Z'(Ω)")
fig.update_yaxes(title_text='Z"(Ω)')
st.plotly_chart(fig, theme=None, use_container_width=True)



