import streamlit as st
import pandas as pd
import os

# Verificar se o arquivo 'dados.xlsx' existe na raiz
if os.path.exists('dados.xlsx'):
    # Carregar a planilha Excel
    excel_file = pd.ExcelFile('dados.xlsx')

    # Criar um seletor para as abas da planilha
    sheet_options = excel_file.sheet_names
    selected_sheet = st.selectbox('Selecione a aba da planilha:', sheet_options)

    # Ler a aba selecionada
    data = pd.read_excel(excel_file, sheet_name=selected_sheet)

    # Mostrar a tabela de dados na interface
    st.dataframe(data)

    # Campo de busca
    search_query = st.text_input("Digite o termo de busca:", "")

    # Botão de busca
    if st.button('Buscar'):
        # Realizar a busca (considerando todas as colunas)
        search_result = data[data.apply(lambda row: row.astype(str).str.contains(search_query).any(), axis=1)]
        
        # Se houver resultados, mostrá-los
        if not search_result.empty:
            st.write("Resultado(s) da busca:")
            st.dataframe(search_result)
        else:
            st.write("Nenhum registro encontrado.")
else:
    st.error('O arquivo "dados.xlsx" não foi encontrado na raiz.')
