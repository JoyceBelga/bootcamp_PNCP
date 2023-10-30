import requests
import pickle
import streamlit as st

st.title("Ensaio sobre dados do Portal Nacional de Compras Públicas (PNCP) 🛒🛒")

aba1, aba2, aba3, aba4 = st.tabs(['Adesão ao Portal', 'Publicadores de Contratos', 'Overview Fornecedores', 'Fornecedores com Sanções'])

#@st.cache(allow_output_mutation=True)  #para melhorar o desempenho da página   --deprecated!
@st.cache_data
#carregar dados de mapas e gráficos, em formato pickle, de um repositório remoto e os organiza em uma estrutura de dicionário para posterior uso no aplicativo. 
def load_data(tipo):
    if tipo == 'sancoes': #Joyce
        pickle_filenames = ['sancao_barra_top10_fornecedores.pkl', 'sancao_barra_top10_orgaos.pkl', 'sancao_treemap_Uffornecedores.pkl', 'sancao_heatmap_municipiosFornecedores.pkl',
                            'sancao_lolipop_top10_fornecedores.pkl', 'sancao_treemap_fornecedoresUf.pkl', 
                            'sancao_boxplot_esferaOrgaos.pkl']
    elif tipo == 'publicadores':  #Gabi
        pickle_filenames = ['publicadores_treemap_qtde_publicador.pkl', 'publicadores_barra_publicador_ente_2.pkl',
                            'publicadores_treemap_top10_3.pkl', 'publicadores_barra_fed_outropub_4.pkl']
    # elif tipo == 'adesao'
    # elif tipo == 'fornecedores'

    url = 'https://raw.githubusercontent.com/JoyceBelga/bootcamp_PNCP/main/' 
    figures = {}
    for filename in pickle_filenames:
        response = requests.get(f'{url}{filename}', stream='True')        
        figures[filename] = pickle.load(response.raw) 
    return figures 

dic_sancoes = load_data('sancoes')
dic_publicadores = load_data('publicadores')

with aba1: 
    st.write("[gráficos da Lia]")
with aba2: 
    st.plotly_chart(dic_publicadores['publicadores_treemap_qtde_publicador.pkl'])
    st.plotly_chart(dic_publicadores['publicadores_barra_publicador_ente_2.pkl'])
    st.plotly_chart(dic_publicadores['publicadores_treemap_top10_3.pkl'])
    st.plotly_chart(dic_publicadores['publicadores_barra_fed_outropub_4.pkl'])
with aba3: 
    st.write("[gráficos da Monica]")    
with aba4: 
    st.plotly_chart(dic_sancoes['sancao_barra_top10_fornecedores.pkl'])
    st.plotly_chart(dic_sancoes['sancao_barra_top10_orgaos.pkl'])
    st.plotly_chart(dic_sancoes['sancao_treemap_Uffornecedores.pkl'])
    st.plotly_chart(dic_sancoes['sancao_heatmap_municipiosFornecedores.pkl'])
    st.plotly_chart(dic_sancoes['sancao_lolipop_top10_fornecedores.pkl'])
    st.plotly_chart(dic_sancoes['sancao_treemap_fornecedoresUf.pkl'])
    st.plotly_chart(dic_sancoes['sancao_boxplot_esferaOrgaos.pkl'])

    

