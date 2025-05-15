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

## 4. Definição de Pipeline de Treinamento

1. **Divisão dos dados**

   * Treino / Validação / Teste (por exemplo, 70/15/15)
2. **Transformações sequenciais**

   * Normalização / padronização de features numéricas
   * Encoding conceitual de categorias (se houver)
3. **Seleção de modelo**

   * Modelos “clássicos” (Random Forest, XGBoost) para espessura e empenamento
   * Modelos de visão (CNN leve) para riscos — ou use HOG/LBP + classificador se já extraiu features de textura

---

## 5. Validação e Ajuste

* **Cross-validation**: garantir robustez do desempenho
* **Análise de erros**: investigar casos de falso positivo e falso negativo para cada defeito
* **Ajuste de hiperparâmetros**: conceitualmente, defina busca em grade (“grid search”) sobre parâmetros-chave

---

## 6. Protótipo de Inferência

* **Fluxo de inferência**:

  1. Entrada de novas leituras + imagens
  2. Aplicação das mesmas transformações de treino
  3. Geração de predição para cada defeito
* **Critério de alerta**: defina limiares de confiança mínimas para acionar retrabalho ou inspeção manual

---

## 7. Planejamento de Deploy e Monitoramento

* **Ambiente de execução**: edge device ou servidor local na fábrica
* **Monitoramento de performance**: acompanhar queda de acurácia e distribuição de previsões (detecção de drift)
* **Ciclo de retraining**: agendar retreinamentos periódicos conforme novos dados rotulados forem coletados

=======================================
