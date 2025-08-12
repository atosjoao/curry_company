# Projeto Final - Fome Zero

## 1. Problema de negócio

A Fome Zero é uma empresa de marketplace de restaurantes, e o recém-contratado CEO, Kleiton Guerra, busca uma compreensão aprofundada do negócio para tomar decisões estratégicas. Sua principal tarefa como Cientista de Dados é auxiliar o CEO respondendo a uma série de perguntas através da análise dos dados da empresa. O objetivo é gerar dashboards a partir dessas análises para fornecer uma visão clara e acionável do negócio. O modelo de negócio da Fome Zero é intermediar a negociação entre clientes e restaurantes, que se cadastram na plataforma para disponibilizar informações como endereço, tipo de culinária, se possuem reservas ou fazem entregas, e uma nota de avaliação.

As perguntas do CEO, que servem como guia para a análise, são categorizadas em tópicos específicos para cobrir diferentes aspectos da empresa:

- **Geral**: Foco em métricas de alto nível, como a quantidade total de restaurantes únicos, países, cidades e tipos de culinária registrados, além do número total de avaliações.
- **País**: Esta seção busca entender o desempenho da empresa em nível nacional, identificando o país com o maior número de cidades, restaurantes e avaliações. Também explora o país com a maior diversidade de culinárias, o maior número de restaurantes com entrega ou reservas, e a média de preço de um prato para dois.
- **Cidade**: A análise aqui se aprofunda no nível municipal, identificando a cidade com mais restaurantes e a com mais restaurantes com notas médias altas (acima de 4) e baixas (abaixo de 2.5). Também busca a cidade com o maior valor médio de um prato para dois, a maior diversidade de culinárias e a maior quantidade de restaurantes que fazem reservas, entregas ou aceitam pedidos online.
- **Restaurantes**: Esta parte do projeto foca em restaurantes individuais. O objetivo é encontrar o restaurante com o maior número de avaliações, a maior nota média e o prato mais caro para duas pessoas. Também inclui a comparação entre restaurantes com determinadas características, como a culinária brasileira no Brasil e nos Estados Unidos, e a relação entre serviços oferecidos (como pedidos online e reservas) e o desempenho (avaliações e preço médio).
- **Tipos de Culinária**: Esta seção se concentra nos diferentes tipos de culinária. A análise visa identificar os melhores e piores restaurantes em termos de avaliação para culinárias específicas, como italiana, americana, árabe, japonesa e caseira. Além disso, busca o tipo de culinária com o maior valor médio de prato para duas pessoas, a maior nota média e o maior número de restaurantes que aceitam pedidos online e fazem entregas.

O produto final do projeto será um dashboard que sintetize as respostas a todas essas perguntas, permitindo que o CEO tenha uma visão clara e rápida do negócio.

## 2. Premissas do negócio

A principal premissa do projeto é que a Fome Zero opera com um modelo de negócio de marketplace, atuando como intermediária entre restaurantes e clientes. A empresa fornece uma plataforma para que os restaurantes se cadastrem e os clientes possam fazer pedidos.

## 3. Estratégia da solução

A estratégia para resolver o desafio é estruturada em algumas etapas:

- **Coleta e Compreensão dos Dados**: A primeira etapa é coletar os dados disponíveis na plataforma Kaggle e entender a fundo cada coluna do conjunto de dados, o que elas representam e se há colunas que podem ser removidas por serem irrelevantes para a análise.
- **Limpeza e Tratamento dos Dados**: A segunda etapa é garantir a qualidade dos dados. Isso envolve verificar e remover dados duplicados e faltantes, além de realizar uma análise estatística descritiva das variáveis para ter uma visão geral do conjunto de dados.
- **Exploração e Resposta às Perguntas**: Esta é a fase central do projeto. O plano é responder a cada uma das perguntas do CEO, primeiro de forma conceitual, pensando em como a resposta seria obtida, e depois implementando o código para obter a resposta. Gráficos podem ser usados para validar e consolidar os resultados. Casos específicos, como perguntas que se mostram falsas, precisam ser demonstrados com os dados.
- **Criação do Dashboard**: Por fim, a solução será apresentada através de um dashboard interativo, utilizando a ferramenta Streamlit, para que o CEO possa visualizar os insights e as respostas de forma clara e acessível.

### 4. Top 3 Insights de dados

1. A diversidade de culinárias é fundamental para o crescimento e a diferenciação do marketplace.
2. Restaurantes que oferecem opção de entrega, tendem a receber mais avaliações
3. A aceitação de reservas é um serviço que impacta positivamente a média de avaliação dos restaurantes

### 5. O produto final do projeto

O produto final deste projeto será um painel online, hospedado na nuvem e acessível de qualquer dispositivo conectado à internet. Este painel irá sintetizar as informações e os insights obtidos na análise de dados, oferecendo ao CEO uma ferramenta visual para acompanhar as métricas estratégicas da empresa Fome Zero.

### 6. Conclusão

O projeto representa um desafio de Ciência de Dados que simula uma situação real de negócios. O objetivo é aplicar os conhecimentos de análise de dados para resolver um problema de negócio, que é fornecer ao CEO da Fome Zero uma compreensão aprofundada da empresa. A conclusão do projeto é a criação de um conjunto de gráficos e tabelas que exibem as métricas de forma otimizada para a tomada de decisões estratégicas.
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
*  **Adicionais mais comparações temporais.**
*  **Aumentar a performance de carregamento da página**

---

### Resultado

Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet.
O painel pode ser acessado através desse link: <br>
[https://project-currycompany.streamlit.app/](https://j-atos-fome-zero.streamlit.app/) <br>
