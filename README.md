# Decupalytic

Decupalytic é um software em Python Streamlit para gerenciar bibliotecas, permitindo buscas eficientes em uma planilha Excel.

## Instalação

Para instalar e executar o Decupalytic, siga os passos abaixo:

1. **Clone o Repositório**

   Primeiro, clone o repositório do Decupalytic para sua máquina local usando o seguinte comando no terminal:

   ```
   git clone https://github.com/almmello/decupalytic.git
   ```

2. **Crie um Ambiente Virtual (Opcional)**

   Recomenda-se criar um ambiente virtual para instalar as dependências do projeto. Isso pode ser feito com o seguinte comando:

   ```
   python -m venv venv
   ```

   Ative o ambiente virtual com:

   - No Windows: `venv\Scripts\activate`
   - No Unix ou MacOS: `source venv/bin/activate`

3. **Instale as Dependências**

   Com o ambiente virtual ativado, instale todas as dependências necessárias executando:

   ```
   pip install -r requirements.txt
   ```

4. **Adicione a Planilha `dados.xlsx`**

   Por questões de privacidade, a planilha `dados.xlsx` não é incluída no repositório. Você deve copiar sua própria planilha para a raiz do projeto. Certifique-se de que ela siga o formato esperado pelo software:

   - Nome do arquivo: `dados.xlsx`
   - Abas representando diferentes categorias ou seções.
   - Primeira linha para cabeçalhos de colunas.
   - Segunda linha para orientações gerais.
   - Dados começando da terceira linha em diante.

5. **Execute o Aplicativo**

   Com tudo configurado, inicie o aplicativo com o seguinte comando:

   ```
   streamlit run app.py
   ```

   O Streamlit abrirá automaticamente uma janela no navegador com o aplicativo Decupalytic.

## Contribuindo

Contribuições são sempre bem-vindas! Para contribuir, por favor, crie um fork do repositório, faça suas alterações e envie um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
