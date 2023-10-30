import requests
import pickle
import streamlit as st

st.title("Ensaio sobre dados do Portal Nacional de Compras Públicas (PNCP) 🛒🛒")

aba1, aba2, aba3, aba4 = st.tabs(['Adesão ao Portal', 'Publicadores de Contratos', 'Overview Fornecedores', 'Fornecedores com Sanções'])

#@st.cache(allow_output_mutation=True)  #para melhorar o desempenho da página   --deprecated!
@st.cache_data
#carregar dados de mapas e gráficos, em formato pickle, de um repositório remoto e os organiza em uma estrutura de dicionário para posterior uso no aplicativo. 
def load_data_sancoes():
    pickle_filenames = ['barra-sancao_top10_fornecedores.pkl', 'barra-sancao_Uffornecedores.pkl', 'lolipop-sancao_top10_fornecedores.pkl', 'treemap-sancao_fornecedoresUf.pkl',
                         'barra-sancao_top10_orgaos.pkl', 'boxplot-sancao_esferaOrgaos.pkl',
                         'heatmap-sancao_municipiosFornecedores.pkl', 'heatmap-sancao_orgao.pkl']

    url = 'https://raw.githubusercontent.com/JoyceBelga/bootcamp_PNCP/main/' 
    figures = {}
    for filename in pickle_filenames:
        response = requests.get(f'{url}{filename}', stream='True')        
        figures[filename] = pickle.load(response.raw) 
    return figures 

dic_sancoes = load_data_sancoes()

with aba1: 
    st.plotly_chart(dic_sancoes['barra-sancao_top10_fornecedores.pkl'])
    st.plotly_chart(dic_sancoes['barra-sancao_Uffornecedores.pkl'])

