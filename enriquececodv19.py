# -*- coding: utf-8 -*-
"""enriqueceCodv19.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jTC7bu8NiCCdW_JLmnOR_g27Qi2MNLL-

# Enriquecimento de Dados
**O que é Enriquecimento de Dados**

Com a transformação digital e com soluções cada vez mais geridas online, contar com um banco de dados incompleto ou desatualizado pode provocar perdas e expor seu negócio a riscos. É aí que entra o Enriquecimento de Dados: esse recurso possibilita atualizar e encontrar informações rapidamente, gerando uma vantagem competitiva.

Em nosso caso vamos encontrar as coordenadas geográficas das cidades, pois no dataset que tratamos no artigo anterior (https://www.linkedin.com/pulse/consumindo-api-e-tratando-dados-com-python-alexandre-tavares/)

Com essas informações adicionais, nosso dataset fica mais completo. Assim, é possível plotar mapas com marcações de ocorrências do CODIV-19.

Para esta tarefa utilizaremos algumas bibliotecas do Python, são elas:
- **Pandas:**
O pandas é uma biblioteca de análise e manipulação de dados de código aberto, rápida, poderosa, flexível e fácil de usar, construída sobre a linguagem Python .
- **os:**
O módulo os fornece dúzias de funções para interagir com o sistema operacional e a utilizaremos para gerar uma variável de ambiente pra autenticarmos na API do GOOLGLE.
- **geocoder:**
Converta endereços em coordenadas geográficas. A API de geo codificação do Google suporta pesquisa difusa.

Bom agora que já entendemos um pouco sobre enriquecimento de dados, sobre algumas bibliotecas do python e oque vamos fazer vamos colocara mão na massa.

Neste artigo iremos utilizar o Google Colab(https://colab.research.google.com/) pra executarmos o código.

**Instalar as Bibliotecas necessárias**

Vamos precisar instalar as bibliotecas do python citado acima, caso estes não esteja instalado, execute a célula abaixo:
"""

!pip install pandas
!pip install os
!pip install geocoder

"""**Importar as Bibliotecas**

Agora precisamos importar as bibliotecas para que possamos utilizá las em nosso algorítimo.
"""

import pandas as pd
import os

"""**Criar variavel de Ambiente pra Chave da API do Google**

Temos que iniciar uma variável de ambiente com a chave da API do google para que possamos nos identificar e executar as requisições.

Caso não saiba como gerar esta chave leia o artigo: https://www.linkedin.com/pulse/gerando-chave-de-acesso-do-google-alexandre-tavares
"""

os.environ["GOOGLE_API_KEY"] = "Insira Aqui Sua Chave"

"""**Importa Biblioteca de geolocalização do google**

Após gerara variável de ambiente com a chave da API devemos importar o módulo geocoder, devemos importar ela sempre depois de gerar a variável, pois o módulo utiliza a variável para se autenticar.
"""

import geocoder

"""**Lê dataset gerado no Artigo Anterior**

*Será preciso fazer upload do arquivo*

para isso execute os passos abaixo:
- clique no ícone de uma pasta na lateral esquerda do colab:

![alt text](http://www.portalatibaia.com.br/Artigos/colab01.png)

- Com isso teremos a tela a seguir, então clique na opção de Upload:

![alt text](http://www.portalatibaia.com.br/Artigos/colab02.png)

- Na tela seguinte localize o arquivo gerado no artigo anterior(https://www.linkedin.com/pulse/consumindo-api-e-tratando-dados-com-python-alexandre-tavares/) e clique em abrir:

![alt text](http://www.portalatibaia.com.br/Artigos/colab03.png)

Com isso já temos nosso arquivo importado para o colab e podemos seguir.

**Importar arquivo**

Devemos importar o arquivo para que possamos utilizá-lo em nosso algorítimo.
"""

dfCodiv19 = pd.read_csv('datasetCodiv19.csv',encoding ='utf-8', sep=';')

"""**Criar um DataFrame Vazio**

Vamos criar um data frame com a estrutura de colunas que pretendemos ter ao final deste algorítimo.
"""

dfEnriquecido = pd.DataFrame(columns=['Estado', 'Cidade', 'Latitude', 'Longitude', 'casosConfirmados', 'Mortes', 'dtAtualizado'])

"""**Enriquecer dados com as Coordenadas geográficas**

Percorre Data Frame e localizando Coordenadas das Cidades / UF utilizando o módulo geocoder

Ao executar o enriquecimento encontramos um erro e ao verificar vi que existe uma cidade com o nome 'Importados/Indefinidos' e para resolver incluímos a linha 
- if (ocorrencia['cidade'] != 'Importados/Indefinidos'):
"""

for (i, ocorrencia) in dfCodiv19.iterrows():
  if (ocorrencia['cidade'] != 'Importados/Indefinidos'):
    #Gera coordenadas
    coordenadas = geocoder.google(str(ocorrencia['cidade']) + ',' + str(ocorrencia['uf']))
    
    # Cria linha no dataframe zerado
    dfEnriquecido.loc[len(dfEnriquecido)] = [ocorrencia['uf'], ocorrencia['cidade'], coordenadas.latlng[0], coordenadas.latlng[1], ocorrencia['casosConfirmados'], ocorrencia['mortos'], ocorrencia['dataAtualizacao']]

"""**Exibir DataSet**

Após todo o processo temos nosso dataset enriquecido com as coordenadas geográficas.
"""

dfEnriquecido

"""**Gerar Arquivo CSV para próximo artigo**"""

dfEnriquecido.to_csv('datasetCodiv19Enriquecido.csv', index=False,sep=';')

"""Os scripts deste artigo estão em: https://github.com/AleTavares/pyEnriqueceDados

**Autor:**

*Alexandre Tavares*

*Engenheiro de Dados*

https://www.linkedin.com/in/alexandre-tavares/
"""