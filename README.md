# bootcamp_unisenai
Repositório criado para compartilhar os arquivos e scripts do Bootcamp em ciencia de Dados e IA - Unisenai

## O projeto foi baseado em problemas enfrentados na industria siderurgica.
==========================================================

Segue um roteiro conceitual para iniciar a solução de ML.

## 1. Definição do Problema e Métricas

* **Objetivo**: Prever os três tipos de defeito (espessura fora de tolerância, empenamento, riscos superficiais)
* **Formato de saída**:

  * Classificação binária para cada defeito (presença/ausência)
* **Métricas de avaliação**:

  * Acurácia, precisão, recall e F1-score para cada classe
  * Matriz de confusão para entender erros por tipo de defeito

---

## 2. Análise Exploratória de Dados (EDA)

* **Distribuição das variáveis**: examine quantas amostras positivas vs. negativas para cada defeito
* **Correlação**: verifique relações entre suas features (sensores, medições geométricas, indicadores de processo)
* **Identificação de outliers**: garanta que valores extremos façam sentido ou sejam tratados

---

## 3. Preparação Conceitual de Features

* **Seleção de colunas**: determine quais sensores ou métricas têm maior relevância para cada defeito
* **Engenharia de atributos**: pense em combinações, razão de variáveis ou estatísticas de janelas de tempo
* **Tratamento de desequilíbrio**: se alguma classe for muito rara, avalie técnicas como oversampling conceitual (SMOTE) ou penalização de classe

=======================================
