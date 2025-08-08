### Resumo do Projeto: Análise de Dados para a Empresa Fome Zero

Este projeto é a resolução de um desafio de Ciência de Dados, que simula um cenário real em uma empresa fictícia, a Fome Zero, um marketplace de restaurantes. Como um Cientista de Dados recém-contratado, minha missão foi analisar os dados da empresa e criar um dashboard para responder a perguntas estratégicas do CEO, Kleiton Guerra.

O objetivo principal foi fornecer ao CEO uma compreensão aprofundada do negócio para que ele pudesse tomar decisões mais assertivas.

---

### O Contexto do Negócio

A Fome Zero atua como intermediadora entre clientes e restaurantes. Sua plataforma cadastra restaurantes, registrando informações como endereço, tipo de culinária, opções de entrega e reservas, e uma nota de avaliação. O CEO Guerra, também novo na empresa, precisava de uma análise detalhada para entender a dinâmica do negócio.

---

### O Desafio

O projeto foi dividido em quatro partes principais de análise, com perguntas específicas a serem respondidas:

* **Geral:** Análise do número total de restaurantes, países, cidades, avaliações e tipos de culinária únicos.
* **País:** Análise e ranqueamento de países com base em métricas como número de cidades, restaurantes, avaliações e notas médias.
* **Cidade:** Ranqueamento de cidades com base no número de restaurantes, notas médias e valor médio de pratos.
* **Restaurantes & Tipos de Culinária:** Ranqueamento de restaurantes e tipos de culinária com base em avaliações, notas médias e valor de pratos para duas pessoas.

Além disso, foi solicitada a criação de um dashboard para apresentar essas informações de forma visual e acessível.

---

### Como o Projeto foi Desenvolvido

Para a resolução do desafio, foram realizadas as seguintes etapas:

1.  **Coleta de Dados:** O conjunto de dados foi obtido do Kaggle, utilizando o arquivo `zomato.csv`.
2.  **Preparação e Limpeza dos Dados:**
    * Verificação e remoção de dados duplicados.
    * Tratamento de dados faltantes.
    * As colunas foram renomeadas para um formato padronizado (snake_case) com a ajuda de uma função auxiliar.
    * A coluna de culinárias foi categorizada, mantendo apenas o primeiro tipo de culinária para cada restaurante.
    * Funções auxiliares foram usadas para preencher os nomes dos países com base nos códigos, criar categorias de preço e nomes de cores.
3.  **Análise dos Dados:** Foram elaboradas perguntas de negócios para nortear as análises, como por exemplo: *'Qual o tipo de culinária com o maior valor médio de um prato para duas pessoas e a maior nota média?'*. Essas perguntas foram respondidas em formas de gráficos ou métricas.
4.  **Criação do Dashboard:** O framework **Streamlit** foi usado para construir o dashboard solicitado, garantindo que as respostas às perguntas estivessem disponíveis de forma interativa.

---

### Ferramentas Utilizadas

* **Jupyter Lab:** Para prototipagem e desenvolvimento inicial da solução.
* **Python:** Linguagem principal para a análise de dados.
* **Streamlit:** Framework para a criação do dashboard interativo e compartilhável.
* **Pandas:** Biblioteca essencial para manipulação e análise de dados.
* **Plotly Express:** Para a criação de gráficos e visualizações de dados no dashboard.
* **Folium:** Para visualizações de mapas.
* **Inflection:** Biblioteca auxiliar para padronização de nomes de colunas.

### Próximo passos
* **Reduzir o número de métricas.**
*  **Criar novos filtros.**
*  **Adicionar novas visões de negócio.**

---

### Resultado

Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet.
O painel pode ser acessado através desse link: 
[https://project-currycompany.streamlit.app/](https://j-atos-fome-zero.streamlit.app/)
Este trabalho demonstrou habilidades de manipulação de dados, raciocínio analítico e criação de soluções de visualização, servindo como um projeto de portfólio robusto.
