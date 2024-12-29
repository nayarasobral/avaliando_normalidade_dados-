import streamlit as st  # Biblioteca para criar interfaces de aplicações web interativas e dinâmicas.
import pandas as pd  # Biblioteca para manipulação e análise de dados estruturados (DataFrames e Séries).
import numpy as np  # Biblioteca para operações numéricas e manipulação de arrays multidimensionais.
import matplotlib.pyplot as plt  # Biblioteca para criar gráficos e visualizações de dados.
import scipy.stats as stats  # Biblioteca para cálculos estatísticos, como testes de normalidade e distribuição.


st.set_page_config(page_title="Teste de Normalidade", layout="wide")
st.title("Teste de Normalidade")
# st.set_page_config(...) configura as propriedades da página da aplicação no Streamlit.
# page_title="Teste de Normalidade" Define o título da aba do navegador onde a aplicação está sendo exibida.
# layout="wide" Define o layout da página como "wide" (amplo), o que significa que os elementos da aplicação ocuparão mais espaço horizontal.
# st.title(...) exibe um título em destaque na interface da aplicação.

with st.sidebar: # Tudo que está indentado dentro desse bloco (with) será exibido na barra lateral da aplicação Streamlit.
    upload_file = st.file_uploader("Escolha o arquivo:",type=['csv'],
                                   accept_multiple_files=False) # Define que o componente aceita apenas um arquivo por vez.
    process_button = st.button("Processar") # Exibe um botão com o rótulo "Processar" na barra lateral.



if process_button and upload_file is not None:
    try:
        data = pd.read_csv(upload_file, header=0)
        if data.empty or data.iloc[:,0].isnull().all():
            st.error("O arquivo está vazio ou a primeira coluna não tem dados válidos")
        else:
            col1, col2 = st.columns(2)
            with col1:
                fig_hist, ax_hist = plt.subplots()
                ax_hist.hist(data.iloc[:,0].dropna(),bins="auto",
                             color='blue', alpha=0.7, rwidth=0.85)
                ax_hist.set_title("Histograma")
                st.pyplot(fig_hist)
            with col2:
                fig_qq, ax_qq = plt.subplots()
                stats.probplot(data.iloc[:,0].dropna(), dist='norm', plot=ax_qq)
                ax_qq.set_title("QQ Plot")
                st.pyplot(fig_qq)

            shapiro_test = stats.shapiro(data.iloc[:,0].dropna())
            st.write(f"Valor de P: {shapiro_test.pvalue:.5f}")
            if shapiro_test.pvalue > 0.05:
                st.success("Não existem evidências suficientes para rejeitar a hipótese de normalidade dos dados")
            else:
                st.warning("Existem evidências suficientes para rejeitar a hipótese de normalidade dos dados")
    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")

    # except: Captura erros (exceções) que ocorrem dentro do bloco try.
    # Exception: É a classe base de todas as exceções em Python. Isso significa que ela pode capturar qualquer tipo de erro.
    # as e: Armazena os detalhes do erro capturado na variável e, permitindo que você acesse informações sobre o erro específico.
    # st.error(...): Exibe uma mensagem de erro estilizada na interface Streamlit.
    # f"Erro ao processar o arquivo: {e}": Mensagem formatada que inclui o detalhe do erro específico ({e}).
    # A variável e contém o texto explicativo do erro, o que ajuda o usuário a entender o que deu errado.