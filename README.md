# Distribuição Normal, Visualização de Dados e Análise Exploratória de Dados - EDA

Este projeto tem como objetivo criar uma aplicação web que permita a verificação da normalidade dos dados. A ideia é atender às necessidades dos colegas e clientes ao possibilitar o upload de arquivos e a realização de análises exploratórias automatizadas.

## Funcionalidades

1. **Visualização com Histograma**: Gera histogramas para inspecionar a distribuição dos dados carregados.
2. **Diagrama de Probabilidade Normal (Q-Q Plot)**: Permite verificar visualmente a aderência dos dados à distribuição normal.
3. **Teste de Shapiro-Wilk**: Realiza uma análise estatística formal para determinar se os dados seguem uma distribuição normal.

---

## Tecnologias Utilizadas

- **Python**: Linguagem principal para o desenvolvimento.
- **Pandas e NumPy**: Manipulação e processamento de dados.
- **SciPy**: Realiza os testes estatísticos.
- **Matplotlib/Seaborn**: Gera os gráficos para visualização de dados.
- **Streamlit**: Cria uma interface web simples e intuitiva para interagir com os dados e resultados.

---

## Estrutura do Repositório

```
├── data.csv            # Dados de exemplo para teste.
├── app.py              # Código principal da aplicação.
├── LICENSE             # Arquivo de licença do projeto.
├── README.md           # Documentação do projeto.
├── requirements.txt    # Lista de dependências necessárias.
```

---

## Pipeline da Análise

1. **Divisão dos Dados**:
   - 70% dos dados para treinamento.
   - 30% para teste e validação.

2. **Treinamento do Modelo**:
   - Uso de algoritmos para a classificação ou regressão (ex.: Random Forest, Regressão Linear).
   - Ajuste de hiperparâmetros para otimização de desempenho.

3. **Avaliação do Modelo**:
   - Métricas como acurácia, precisão, recall e F1-Score são avaliadas.
   - Apenas modelos com desempenho superior ao limiar definido são considerados para produção.

4. **Visualização e Análise**:
   - Gera relatórios e gráficos baseados nos resultados.

5. **Implantação**:
   - Modelos aprovados são integrados ao ambiente de produção.

---

## Exemplo de Fluxo

1. **Entrada de Dados**: O usuário insere informações por meio de upload de arquivos CSV no sistema.
2. **Divisão dos Dados**:
   - Os dados são divididos em conjuntos de treino (70%) e teste (30%).
3. **Análise Inicial**:
   - O sistema gera histogramas e diagramas de probabilidade normal (Q-Q plots) para a inspeção visual dos dados.
4. **Teste Estatístico**:
   - O teste de Shapiro-Wilk é aplicado para determinar a aderência dos dados à distribuição normal.
5. **Exibição de Resultados**:
   - Os resultados são exibidos por meio de gráficos e estatísticas com interpretação dos valores obtidos (ex.: p-value e conclusão).

---

## Exemplos de Código

### Gerar Histograma
```python
ax_hist.hist(data.iloc[:, 0].dropna(), bins="auto", color="blue", alpha=0.7, rwidth=0.85)
```
**Explicação**:
- **ax_hist.hist(...)**: Cria um histograma para inspecionar a distribuição.
- **bins="auto"**: Define automaticamente os intervalos.
- **alpha=0.7**: Define a transparência das barras.

### Gerar Q-Q Plot
```python
stats.probplot(data.iloc[:, 0].dropna(), dist="norm", plot=ax_qq)
```
**Explicação**:
- **stats.probplot(...)**: Gera um diagrama de probabilidade.
- **dist="norm"**: Compara com a distribuição normal.

### Realizar Teste de Shapiro-Wilk
```python
shapiro_test = stats.shapiro(data.iloc[:, 0].dropna())
```
**Explicação**:
- **stats.shapiro(...)**: Avalia a normalidade estatisticamente.
- **shapiro_test.pvalue**: Retorna o valor-p para a decisão sobre normalidade.

---

## Como Rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/analise-normalidade-dados.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd analise-normalidade-dados
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o aplicativo:
   ```bash
   streamlit run app.py
   ```

---

## Dataset

O sistema suporta arquivos CSV com os seguintes formatos e atributos:
- **Colunas Numéricas**: Dados para os quais a distribuição será analisada.
- **Colunas Categóricas** (opcional): Para informações contextuais.

---

## Resultados Esperados

1. **Visualizações Intuitivas**:
   - Histogramas e Q-Q plots para exploração dos dados.

2. **Análise Estatística**:
   - Teste de Shapiro-Wilk com estatísticas claras.

3. **Interface Simplificada**:
   - Usuário pode carregar os dados e obter resultados com mínimo esforço.

4. **Decisões Baseadas em Dados**:
   - Ferramenta que permite classificar e entender os dados de forma rápida e eficiente.

---

## Licença

Este projeto está sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

---

## Autor

👩‍💻 **Seu Nome**
- Email: nayysobrall@gmail.com
- GitHub: nayarasobral

Sinta-se à vontade para dar feedback ou contribuir! 🌟

