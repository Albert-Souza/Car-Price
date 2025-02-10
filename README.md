# Estimação de Preço de Carros
Projeto de Análise, inferência e previsão de preços de carros usados nos EUA

Acesse a aplicação desse projeto [Aqui](https://www.albert-souza.com/projects/car-price-app/).

## Objetivo
O objetivo deste projeto é criar um modelo de Machine Learning capaz de estimar o preço (Price) de carros com base em algumas variáveis, como:

- **Brand** (Marca)
- **Model** (Modelo)
- **Year** (Ano)
- **Engine Size** (Tamanho do motor)
- **Fuel Type** (Tipo de combustível)
- **Transmission** (Transmissão)
- **Mileage** (Quilometragem)
- **Doors** (Número de portas)
- **Owner Count** (Número de proprietários anteriores)

Além da previsão de preços, também foi realizada uma análise exploratória para entender como cada variável influencia no preço do carro.

## Análise Exploratória de Dados (EDA)

### Matriz de Correlação
A matriz de correlação evidencia algumas relações importantes entre as variáveis numéricas:

- Correlação positiva de **0.66** entre **Year** e **Price** (carros mais novos tendem a ser mais caros).
- Correlação positiva de **0.36** entre **Engine_Size** e **Price** (motores maiores tendem a ser mais caros).
- Correlação negativa de **-0.55** entre **Mileage** e **Price** (carros com maior quilometragem tendem a ter preços menores).

![Matriz de Correlação](https://github.com/Albert-Souza/Car-Price/blob/main/visualizations/Correlation%20Matrix.png)

### Correlação com Price
Para uma melhor visualização da correlação entre **Price** e as variáveis mais relevantes, foi utlizado um gráfico Hexbin:

![Hexbin Correlations](https://github.com/Albert-Souza/Car-Price/blob/main/visualizations/Hexbin%20Correlations.png)

### Preço Médio por Tipo de Transmissão
O gráfico abaixo mostra que carros com transmissão **automática** tendem a ser mais caros em relação a outros tipos de transmissão.

![Mean Price by Transmission Type](https://github.com/Albert-Souza/Car-Price/blob/main/visualizations/Mean%20Price%20by%20Transmission%20Type.png)

### Preço Médio por Tipo de Combustível
Carros **elétricos** são, em média, os mais caros, seguidos pelos **híbridos**. Carros **a diesel** e **a gasolina** possuem preços semelhantes.

![Mean Price by Fuel Type](https://github.com/Albert-Souza/Car-Price/blob/main/visualizations/Mean%20Price%20by%20Fuel%20Type.png)

### Preço Médio por Marca
A diferença de preço entre marcas não é tão significativa quanto esperado.

![Mean Price by Brand](https://github.com/Albert-Souza/Car-Price/blob/main/visualizations/Mean%20Price%20by%20Brand.png)

### Preço Médio por Modelo
Há algumas variações de preço conforme o modelo do carro, mas não há uma tendência clara para todos.

![Mean Price by Model](https://github.com/Albert-Souza/Car-Price/blob/main/visualizations/Mean%20Price%20by%20Model.png)

## Modelagem e Previsão

### Seleção de Características
Com base na análise exploratória, foram selecionadas as seguintes variáveis para o modelo:

- **Year**
- **Engine_Size**
- **Fuel_Type**
- **Transmission**
- **Mileage**
- **Model**

As variáveis categóricas (**Fuel_Type, Transmission e Model**) foram transformadas via One-Hot-Encoding, e os dados numéricos foram normalizados utilizando **MinMaxScaler**.

### Divisão dos Dados
Os dados foram divididos em:
- **80% para treinamento**
- **20% para teste**

### Algoritmo Utilizado
O modelo escolhido foi **Regressão Linear**, que foi treinado utilizando os dados de treino.

### Resultados da Previsão
- **Root Mean Squared Error (RMSE):** 64.89
- **RMSE relativo à média dos preços:** 0.01

Apesar do erro ser baixo, alguns **outliers** foram encontrados, com um erro absoluto de até **1715.79**.

![Error Distribution](https://github.com/Albert-Souza/Car-Price/blob/main/visualizations/Error.png)

## Inferência

Os coeficientes do modelo ajustado mostram a influência de cada variável no preço:

- **Cada ano a mais desvaloriza o carro em $299.**
- **Cada litro a mais no motor aumenta o preço em $992.**
- **Cada quilômetro rodado reduz o preço em $0.02.**
- **Carros elétricos são $1987 mais caros do que carros a diesel.**
- **Carros híbridos são $989 mais caros do que carros a diesel.**
- **Carros com transmissão manual são $1490 mais baratos que os automáticos.**
- **Carros com transmissão semi-automática são $1492 mais baratos que os automáticos.**

## Conclusão

O modelo de regressão linear apresentou resultados **muito satisfatórios**, com um erro baixo e coeficientes coerentes com as expectativas do mercado. No entanto, alguns **outliers** ainda foram detectados, indicando que há valores atípicos que poderiam ser analisados mais profundamente.

Os resultados confirmam tendências conhecidas:
- Carros **mais novos** e **com motores maiores** tendem a ser mais caros.
- Maior **quilometragem** reduz o valor do carro.
- **Carros elétricos** são mais caros.
- **Transmissão automática** agrega maior valor ao carro.

O modelo foi salvo para futuras previsões utilizando **joblib**.

---

Este relatório fornece uma visão geral do projeto e seus principais resultados.

