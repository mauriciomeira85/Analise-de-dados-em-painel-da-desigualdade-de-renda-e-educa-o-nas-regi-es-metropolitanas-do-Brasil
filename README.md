# Análise-de-dados-em-painel-da-desigualdade-de-renda-e-educação-nas-regiões-metropolitanas-do-Brasil

Analisa a relação entre desigualdade de renda e educação nas regiões metropolitanas do Brasil, utilizando dados da PNAD entre 2013 e 2023. A pesquisa investiga o impacto da educação sobre a desigualdade de renda, utilizando dados em painel.

# 1. Introdução

Esta se propõe a analisar a relação entre desigualdade de renda e educação nas regiões metropolitanas do Brasil, utilizando uma abordagem de dados em painel que permite investigar a dinâmica da desigualdade ao longo do tempo. A partir de dados da Pesquisa Nacional por Amostra de Domicílios (PNAD) entre 2013 e 2023, o estudo busca responder à seguinte questão: qual o impacto da educação sobre a desigualdade de renda nas regiões metropolitanas brasileiras? A análise econométrica com dados em painel, combinada com a inclusão de variáveis de controle relevantes, visa aprofundar a compreensão sobre os determinantes da desigualdade de renda e fornecer subsídios para a formulação de políticas públicas eficazes de combate à desigualdade e promoção da justiça social. 

# 2. Objetivo

O objetivo deste artigo é analisar a relação entre desigualdade de renda e educação nas regiões metropolitanas do Brasil, utilizando dados da PNAD entre 2013 e 2023. A pesquisa investiga o impacto da educação sobre a desigualdade de renda, utilizando dados em painel. As variáveis de interesse incluem o Índice de Gini, anos de estudo, taxa de analfabetismo, e renda média habitual, além de variáveis de controle como idade média, proporção de homens e mulheres, proporção de pessoas brancas e pretas, e proporção de pessoas na força de trabalho. A partir de dados da Pesquisa Nacional por Amostra de Domicílios (PNAD) entre 2013 e 2023, o estudo busca responder à seguinte questão: qual o impacto da educação sobre a desigualdade de renda nas regiões metropolitanas brasileiras?

# 3. Justificativa

A análise econométrica com dados em painel, combinada com a inclusão de variáveis de controle relevantes, visa aprofundar a compreensão sobre os determinantes da desigualdade de renda e fornecer subsídios para a formulação de políticas públicas eficazes de combate à desigualdade e promoção da justiça social.

# 4. Metodologia

# 4.1 Procedimentos metodológicos

Este trabalho propõe uma análise da desigualdade de renda nas regiões metropolitanas do Brasil, utilizando dados em painel da Pesquisa Nacional por Amostra de Domicílios (PNAD) entre os anos de 2013 e 2023. Segundo Wooldridge, a abordagem por meio de dados em painel combina elementos de dados de séries temporais e de corte transversal, observando as mesmas unidades ao longo do tempo. Ela permite estudar mudanças dentro das unidades e entre elas. É útil para controlar por características não observadas e estudar efeitos dinâmicos.

Além disso, a estimação foi feita a partir de um modelo de efeitos fixos e também de um modelo de efeitos aleatórios. De acordo com Wooldridge (2006), o método de efeitos fixos é usado para eliminar o viés causado por fatores não observados constantes no tempo. Já o modelo de efeitos aleatórios é baseado na suposição de que o efeito não observado não é correlacionado com as variáveis explicativas. Desse modo, o modelo de efeitos fixos controla a heterogeneidade não observada através da inclusão de um efeito fixo para cada unidade de corte transversal, enquanto o modelo de efeitos aleatórios considera o efeito fixo como parte do termo erro. Posteriormente, seguindo Wooldridge (2006), realizamos o teste de Hausman, que indicou o modelo de efeitos aleatórios como mais eficiente para a análise. 

As informações coletadas foram: índice de Gini, renda média habitual, anos de estudo, e taxa de analfabetismo. Além dessas, foram selecionadas as seguintes variáveis de controle: idade média da população, proporção de homes e mulheres na população, proporção de pessoas brancas e pretas, e proporção de pessoas na força de trabalho. A coleta foi feita a partir de dados disponíveis na Pesquisa Nacional por Amostra de Domicílios (PNAD) para as regiões metropolitanas brasileiras entre os anos de 2013 e 2023.

### Tabela 1: Variáveis do Modelo


Para analisar a relação entre desigualdade de renda e educação nas regiões metropolitanas do Brasil, este estudo utiliza um modelo de efeitos aleatórios com dados em painel. A escolha do modelo de efeitos aleatórios se justifica pelos resultados do teste de Hausman, que indicou ser este o modelo mais eficiente. Para o presente caso, a especificação do modelo de efeitos aleatórios é: 

onde, lnGINI é a variável dependente, explicada pelas variáveis independentes lnESTUDO, lnANALFABETISMO e lnRENDA, e as demais variáveis de controle. Os indicadores foram observados em sua forma logarítmica natural (ln), com o intuito de auferir melhor ajustamento dos dados ao modelo estimado. Outrossim, em consonância com o lecionado por Hoffman (2016), o coeficiente β0 corresponde ao intercepto, ou seja, a resposta para variável explicada quando as variáveis explicativas se igualam a zero. Ademais, os coeficientes β1, β2, β3, β4, β5, β6, β7  e β8  representam a proporção do quanto o índice de gini se altera, caso seja acrescido um ponto no valor da respectiva variável. Por fim, ai representa o efeito fixo individual para a região metropolitana i e uit é o termo erro idiossincrático.

Para garantir a robustez da inferência estatística, foram realizados testes de diagnóstico para verificar a presença de heterocedasticidade e autocorrelação serial nos resíduos de ambos os modelos, de efeitos fixos e de efeitos aleatórios. Seguindo Wooldridge (2006), a heterocedasticidade foi verificada através do teste de Breusch-Pagan. A presença de heterocedasticidade viola uma das hipóteses do modelo de regressão e pode levar a estimativas ineficientes dos erros padrão. Já a autocorrelação serial foi verificada através do teste de Breusch-Godfrey/Wooldridge para dados em painel. A autocorrelação serial também viola uma das hipóteses do modelo e pode gerar estimativas inconsistentes dos erros padrão. 

# 4.2 Variáveis e Base de dados  

A agenda de pesquisa em desigualdade avançou muito ao longo dos anos, com a preocupação na mensuração da mesma. Assim, várias medidas de desigualdade foram sendo construídas. Dentre elas, as principais são: coeficiente de Gini, mais conhecido por índice de Gini, coeficiente de concentração, classe de medidas de Atkinson, índices T de Theil e L de Theil, dentre outros. O presente trabalho tomou como base o índice de Gini como medida de desigualdade, para entender a relação entre a mesma e a educação, sendo esta última representada por: anos de estudos e proporção de analfabetismo. 

O coeficiente de Gini é uma medida que sintetiza o nível de desigualdade de uma distribuição de renda em um único número, sendo o indicador mais conhecido e usado de desigualdade. Ele é um instrumento usado para medir o grau de concentração de renda, o qual aponta a diferença entre os rendimentos dos mais pobres e dos mais ricos e, numericamente, varia de 0 a 1, sendo que 0 representa a situação de total igualdade, ou seja, todos têm a mesma renda, e o valor 1 significa completa desigualdade de renda, ou seja, uma só pessoa detém toda a renda do lugar. Para esta pesquisa, o índice de Gini foi calculado a partir da renda domiciliar per capita.

Para analisar o impacto da educação sobre a desigualdade de renda, foram utilizadas as seguintes variáveis: 

**- Anos de estudo:** Representa a média de anos de estudo da população com 14 anos ou mais de idade em cada região metropolitana. Essa variável busca capturar o nível de escolaridade da população, que é um importante determinante da produtividade do trabalho e da renda individual. 

**- Proporção de analfabetismo:** Representa a proporção de pessoas com 14 anos ou mais de idade que não sabem ler e escrever em cada região metropolitana. O analfabetismo é um indicador de exclusão social e de baixa qualificação da mão de obra, o que pode contribuir para a desigualdade de renda. 

Além das variáveis de educação, foram incluídas no modelo as seguintes variáveis de controle: 

**- Idade média da população:** A idade média da população pode influenciar a desigualdade de renda, uma vez que faixas etárias mais jovens e mais velhas tendem a ter rendimentos mais baixos. 

**- Renda média habitual:** Representa a renda média habitualmente recebida pelas pessoas com 14 anos ou mais de idade em cada região metropolitana. Essa variável busca controlar pelo efeito da renda média na desigualdade, uma vez que regiões com maior renda média podem apresentar menor desigualdade. 

**- Proporção de homens e mulheres:** A proporção de homens e mulheres na população pode refletir diferenças na participação no mercado de trabalho e nos níveis de renda entre os sexos. 

**- Raça:** A variável raça busca controlar por possíveis diferenças na desigualdade de renda entre grupos raciais, que podem estar associadas a fatores históricos e sociais. 

**- Proporção de pessoas na força de trabalho:** A proporção de pessoas na força de trabalho em relação à população total pode influenciar a desigualdade de renda, uma vez que uma maior participação no mercado de trabalho pode estar associada a uma distribuição mais equitativa da renda. 

A inclusão dessas variáveis de controle visa isolar o efeito da educação sobre a desigualdade de renda, controlando por outros fatores que podem influenciar a distribuição de renda nas regiões metropolitanas. 

# 4.3 Ferramentas de Análise

A análise de dados deste estudo foi conduzida utilizando a linguagem de programação R, em um fluxo de trabalho que combinou os ambientes Google Colab e Jupyter Notebook (via Anaconda) para otimizar as etapas de coleta e análise. A coleta de dados foi realizada por meio de web scraping dos microdados da Pesquisa Nacional por Amostra de Domicílios (PNAD) Contínua para o período de 2013 a 2023, usando as linguagens R e SQL. Para esta tarefa, foi empregado o ambiente Google Colab, aproveitando seus recursos de nuvem para lidar com o grande volume de dados. O processo foi automatizado com o pacote PNADcIBGE, que gerencia a complexidade de acesso e download dos arquivos diretamente dos repositórios do IBGE. O pacote googledrive foi utilizado para armazenar os dados brutos coletados em nuvem, garantindo a integridade e a portabilidade dos dados. Posteriormente, a limpeza, o tratamento e toda a análise econométrica foram desenvolvidos no ambiente Jupyter Notebook, escolhido por sua interatividade e capacidade de organização da pesquisa. Para a manipulação e agregação dos dados, foi utilizado o pacote dplyr. A estimação dos modelos de dados em painel, incluindo efeitos fixos e aleatórios, foi realizada com o pacote plm. Os testes de diagnóstico, como o Teste de Hausman e os testes para heterocedasticidade e autocorrelação, foram conduzidos com o pacote lmtest, e as correções de erros-padrão robustos (Driscoll-Kraay) foram aplicadas com o auxílio do pacote sandwich. Finalmente, a formatação das tabelas de resultados para apresentação no artigo foi feita com os pacotes stargazer e kableExtra. As técnicas e ferraments utilizadas foram:
   
- Web scrapping
- R
- SQL
- Google Colab
- Jupyter Notebook pelo Anaconda

# 5. Análise dos Resultados
   
# 5.1  Análise descritiva dos resultados econométricos






