# Walmart Sales Analysis

Projeto de analise exploratoria de vendas do Walmart. O notebook investiga padroes de receita, comportamento temporal e variaveis que podem apoiar decisoes de estoque, operacao e planejamento comercial.

## Objetivo

Explorar dados de vendas para identificar tendencias, sazonalidade, variacoes por loja e relacoes entre indicadores comerciais.

## O que o projeto demonstra

- Carga e exploracao inicial de dados tabulares.
- Verificacao de qualidade: tipos, nulos, duplicados e outliers.
- Analises descritivas de variaveis comerciais.
- Visualizacoes interativas com Plotly.
- Estrutura de notebook com secoes de data understanding e exploratory data analysis.

## Stack

- Python
- Pandas e NumPy
- Plotly
- Jupyter Notebook / Google Colab

## Arquivos

| Arquivo | Descricao |
| --- | --- |
| `Walmart.ipynb` | Notebook principal com limpeza e analise exploratoria. |

## Como executar

1. Abra o notebook no Google Colab ou Jupyter.
2. Disponibilize o arquivo `Walmart.csv` no caminho esperado ou ajuste a celula de leitura.
3. Execute as celulas em ordem.

## Pontos fortes para portfólio

O projeto e bom para demonstrar analise de dados de negocio, especialmente varejo, sazonalidade e suporte a decisao. Para Engenharia de Dados Júnior, ele evidencia capacidade de entender uma base operacional antes de propor transformacoes.

## Limitações atuais

- O dataset nao esta versionado nem documentado no repositorio.
- O projeto depende de caminho de Google Drive.
- Falta uma camada de transformacao reutilizavel fora do notebook.
- Nao ha testes, validacao de schema ou ambiente reproduzivel.
- A conclusao executiva poderia ser mais objetiva e orientada a impacto.

## Próximas melhorias recomendadas

- Documentar fonte, granularidade e dicionario de dados.
- Criar pipeline de tratamento em `src/transform.py`.
- Adicionar validacoes para datas, valores negativos e chaves duplicadas.
- Criar um resumo final com principais indicadores e recomendacoes.
- Preparar uma versao SQL das principais consultas analiticas.
