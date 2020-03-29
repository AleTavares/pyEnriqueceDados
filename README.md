# Enriquecimento de Dados
**O que é Enriquecimento de Dados**

Com a transformação digital e com soluções cada vez mais geridas online, contar com um banco de dados incompleto ou desatualizado pode provocar perdas e expor seu negócio a riscos. É aí que entra o Enriquecimento de Dados: esse recurso possibilita atualizar e encontrar informações rapidamente, gerando uma vantagem competitiva.

Em nosso caso vamos encontar as coordenadas geográficas das cidades, pois no dataset que tratamos no artigo anterior (https://www.linkedin.com/pulse/consumindo-api-e-tratando-dados-com-python-alexandre-tavares/)

Com essas informações adicionais, nosso dataset fica mais completo. Assim, é possível plotar mapas com marcações de ocorrencias do CODIV-19.

Para esta tarefa utilizaremos algumas bibliotecas do Python, são elas:
- **Pandas:**
O pandas é uma biblioteca de análise e manipulação de dados de código aberto, rápida, poderosa, flexível e fácil de usar, construída sobre a linguagem Python .
- **os:**
O módulo os fornece dúzias de funções para interagir com o sistema operacional e a utilizaremos para gerar uma variavel de ambiente pra autenticarmos na API do GOOLGLE.
- **geocoder:**
Converta endereços em coordenadas geográficas. A API de geocodificação do google suporta pesquisa difusa.

Bom agora que já entendemos um pouco sobre enriqueciment de dados, sobre algumas bibliotecas do python e oque vamos fazer vamos colocara mão na massa.

Neste artigo iremos utiligar o Google Colab(https://colab.research.google.com/) pra executarmos o código.