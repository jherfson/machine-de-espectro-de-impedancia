import streamlit as st
from stoichiometric.stoichiometric import Stoichiometric
import json


st.set_page_config(
    page_title='Cálculo Estequiométrico ',
    page_icon='🧮'
)
st.markdown('## Cálculo Estequiométrico ')
st.sidebar.header('Cálculo Estequiométrico!')

with st.form(key='insert'):
    input_equacao = st.text_input(label='Insira a equação estequiométrica', placeholder='BaCO3 + MoO3 -> BaMoO4 + CO2')
    input_massa = st.number_input(label='Insira a massa')
    button_submit = st.form_submit_button('Calcular')

    if button_submit:
        st.markdown('## Equação fornecida')
        st.text(3 * '' + str(input_equacao))

        equacao = Stoichiometric(input_equacao, input_massa)

        st.divider()
        st.markdown('## Equação Balanceada')
        st.text(equacao.reaction)

        result = json.loads(equacao.print_mass())
        reagentes = {}
        produtos = {}
        for item, valor in result.items():
            if valor < 0:
                reagentes[str(item).strip()] = str(abs(valor))
            else:
                produtos[str(item).strip()] = str(abs(valor))
        st.divider()
        st.markdown('## Reagentes')
        massa_total = 0
        for r, m in reagentes.items():
            s = 3 * ' ' + '{reagente}:{massa} g'.format(reagente=r.ljust(30, '.'),
                                                        massa='{:10.4f}'.format(float(m)))
            massa_total += float(m)
            st.text(s)
        
        st.divider()
        st.markdown('## Produtos')
        massa_total = 0
        for p, m in produtos.items():
            s = 3 * ' ' + '{produto}:{massa} g'.format(produto=p.ljust(30, '.'),
                                                      massa='{:10.4f}'.format(float(m)))
            massa_total += float(m)
            st.text(s)

