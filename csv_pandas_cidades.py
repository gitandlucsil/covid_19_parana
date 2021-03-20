import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.offline as py
import plotly.graph_objs as go
from datetime import datetime

#URL do documento
# https://www.saude.pr.gov.br/Pagina/Coronavirus-COVID-19

def grafico_coluna(coluna, tabela):
    fig = px.histogram(tabela, x = coluna)
    fig.show()

def grafico_coluna_sexo(coluna, tabela):
    fig = px.histogram(tabela, x = coluna, color = 'SEXO')
    fig.show()
    
#Realiza a leitura de todo o arquivo
pd.set_option('display.max_rows', None)
data_frame = pd.read_csv(r'informe_epidemiologico_16_03_2021_geral.csv', delimiter = ';')
#print(data_frame)
#Elimimando colunas não uteis
data_frame = data_frame.drop('IBGE_RES_PR', axis = 1)
data_frame = data_frame.drop('IBGE_ATEND_PR', axis = 1)
data_frame = data_frame.drop('MUN_ATENDIMENTO', axis = 1)
data_frame = data_frame.drop('LABORATORIO', axis = 1)
data_frame = data_frame.drop('DATA_DIAGNOSTICO', axis = 1)
data_frame = data_frame.drop('DATA_INICIO_SINTOMAS', axis = 1)
data_frame = data_frame.drop('DATA_OBITO_DIVULGACAO', axis = 1)
data_frame = data_frame.drop('STATUS', axis = 1)
data_frame = data_frame.drop('FONTE_DADO_RECUPERADO', axis = 1)
data_frame = data_frame.drop('DATA_RECUPERADO_DIVULGACAO', axis = 1)
#print(data_frame)
#Mostra o numero de casos por municipio de residencia
#print(df['MUN_RESIDENCIA'].value_counts())
#print(df['MUN_RESIDENCIA'].value_counts(normalize=True))
#Mostra o numero de casos pela cidade
data_frame_cidade_casos = data_frame.query('MUN_RESIDENCIA == "CLEVELANDIA"')
#print(data_frame_cidade_casos) 
#Convertendo para o tipo data
data_frame_cidade_casos["DATA_CONFIRMACAO_DIVULGACAO"] = pd.to_datetime(data_frame_cidade_casos["DATA_CONFIRMACAO_DIVULGACAO"], dayfirst = True) 
#Ordenando do mais velho para o mais recente
data_frame_cidade_casos = data_frame_cidade_casos.sort_values(by='DATA_CONFIRMACAO_DIVULGACAO', ascending = True)
data_frame_cidade_casos['DATA_CONFIRMACAO_DIVULGACAO'] = data_frame_cidade_casos['DATA_CONFIRMACAO_DIVULGACAO'].dt.strftime('%d/%m/%Y')
#print(data_frame_cidade_casos) 
#Printar em arquivo de texto
with open('parana_casos.txt', 'w') as f:
    print(data_frame_cidade_casos, file=f)

#Desenha os graficos
for coluna in data_frame_cidade_casos:
    grafico_coluna(coluna, data_frame_cidade_casos)
#Desenha os graficos por sexo
for coluna in data_frame_cidade_casos:
    grafico_coluna_sexo(coluna, data_frame_cidade_casos)

#Ordenas o numero de casos por sexo
data_frame_cidade_casos_sexo = data_frame_cidade_casos['SEXO'].value_counts()
print(data_frame_cidade_casos_sexo)
with open('parana_casos_SEXO.txt', 'w') as f:
    print(data_frame_cidade_casos_sexo, file=f)
data_frame_cidade_casos['SEXO'].value_counts().plot(kind='bar')
plt.show()
#Ordena o numero de casos por idade
data_frame_cidade_casos_idade = data_frame_cidade_casos['IDADE_ORIGINAL'].value_counts()
print(data_frame_cidade_casos_idade)
with open('parana_casos_IDADE.txt', 'w') as f:
    print(data_frame_cidade_casos_idade, file=f)
#data_frame_cidade_casos['IDADE_ORIGINAL'].value_counts().sort_index().plot()
#plt.show()
#data_frame_cidade_casos['IDADE_ORIGINAL'].value_counts().sort_index().plot(kind='bar')
#plt.show()
#Ordena o numero de casos por data de confirmacao
data_frame_cidade_casos_dia = data_frame_cidade_casos['DATA_CONFIRMACAO_DIVULGACAO'].value_counts()
with open('parana_casos_DATA_CONFIRMACAO.txt', 'w') as f:
    print(data_frame_cidade_casos_dia, file=f)

#Obitos
data_frame_cidade_obitos = data_frame_cidade_casos.query('OBITO == "SIM" | OBITO == "Sim" | OBITO == "sim"')
print(data_frame_cidade_obitos)
#Convertendo para o tipo data
data_frame_cidade_obitos["DATA_OBITO"] = pd.to_datetime(data_frame_cidade_obitos["DATA_OBITO"], dayfirst = True) 
#Ordenando do mais velho para o mais recente
data_frame_cidade_obitos = data_frame_cidade_obitos.sort_values(by='DATA_OBITO', ascending = True)
data_frame_cidade_obitos['DATA_OBITO'] = data_frame_cidade_obitos['DATA_OBITO'].dt.strftime('%d/%m/%Y')
print(data_frame_cidade_obitos) 
#Printar em arquivo de texto
with open('parana_obitos.txt', 'w') as f:
    print(data_frame_cidade_obitos, file=f)
#Ordenas o numero de obitos por sexo
data_frame_cidade_obitos_sexo = data_frame_cidade_obitos['SEXO'].value_counts()
print(data_frame_cidade_obitos_sexo)
with open('parana_obitos_SEXO.txt', 'w') as f:
    print(data_frame_cidade_obitos_sexo, file=f)
#Ordena o numero de obitos por idade
data_frame_cidade_obitos_idade = data_frame_cidade_obitos['IDADE_ORIGINAL'].value_counts()
print(data_frame_cidade_obitos_idade)
with open('parana_obitos_IDADE.txt', 'w') as f:
    print(data_frame_cidade_obitos_idade, file=f)
#Ordena o numero de obitos por data de obito
data_frame_cidade_obitos_dia = data_frame_cidade_obitos['DATA_OBITO'].value_counts()
with open('parana_obitos_DATA_CONFIRMACAO.txt', 'w') as f:
    print(data_frame_cidade_obitos_dia, file=f)

#Desenha os graficos
for coluna in data_frame_cidade_obitos:
    grafico_coluna(coluna, data_frame_cidade_obitos)
#Desenha os graficos por sexo
for coluna in data_frame_cidade_obitos:
    grafico_coluna_sexo(coluna, data_frame_cidade_obitos)

'''
data_frame_cidade_obitos['IDADE_ORIGINAL'].value_counts().plot(kind='bar')
plt.show()
data_frame_cidade_obitos['IDADE_ORIGINAL'].value_counts().sort_index().plot()
plt.show()
'''
'''
data_frame_query = " MUN_RESIDENCIA == \"AMPERE\" "\
                    " | MUN_RESIDENCIA == \"BARRACAO\""\
                    " | MUN_RESIDENCIA == \"BELA VISTA DA CAROBA\""\
                    " | MUN_RESIDENCIA == \"BOA ESPERANCA DO IGUACU\""\
                    " | MUN_RESIDENCIA == \"BOM JESUS DO SUL\""\
                    " | MUN_RESIDENCIA == \"BOM SUCESSO DO SUL\""\
                    " | MUN_RESIDENCIA == \"CAPANEMA\""\
                    " | MUN_RESIDENCIA == \"CHOPINZINHO\""\
                    " | MUN_RESIDENCIA == \"CLEVELANDIA\""\
                    " | MUN_RESIDENCIA == \"CORONEL DOMINGOS SOARES\""\
                    " | MUN_RESIDENCIA == \"CORONEL VIVIDA\""\
                    " | MUN_RESIDENCIA == \"CRUZEIRO DO IGUACU\""\
                    " | MUN_RESIDENCIA == \"DOIS VIZINHOS\""\
                    " | MUN_RESIDENCIA == \"ENEAS MARQUES\""\
                    " | MUN_RESIDENCIA == \"FLOR DA SERRA DO SUL\""\
                    " | MUN_RESIDENCIA == \"FRANCISCO BELTRAO\""\
                    " | MUN_RESIDENCIA == \"HONORIO SERPA\""\
                    " | MUN_RESIDENCIA == \"ITAPEJARA D'OESTE\""\
                    " | MUN_RESIDENCIA == \"MANFRINOPOLIS\""\
                    " | MUN_RESIDENCIA == \"MANGUEIRINHA\""\
                    " | MUN_RESIDENCIA == \"MARIOPOLIS\""\
                    " | MUN_RESIDENCIA == \"MARMELEIRO\""\
                    " | MUN_RESIDENCIA == \"NOVA ESPERANCA DO SUDOESTE\""\
                    " | MUN_RESIDENCIA == \"NOVA PRATA DO IGUACU\""\
                    " | MUN_RESIDENCIA == \"PALMAS\""\
                    " | MUN_RESIDENCIA == \"PATO BRANCO\""\
                    " | MUN_RESIDENCIA == \"PEROLA D'OESTE\""\
                    " | MUN_RESIDENCIA == \"PINHAL DE SAO BENTO\""\
                    " | MUN_RESIDENCIA == \"PLANALTO\""\
                    " | MUN_RESIDENCIA == \"PRANCHITA\""\
                    " | MUN_RESIDENCIA == \"REALEZA\""\
                    " | MUN_RESIDENCIA == \"RENASCENCA\""\
                    " | MUN_RESIDENCIA == \"SALGADO FILHO\""\
                    " | MUN_RESIDENCIA == \"SALTO DO LONTRA\""\
                    " | MUN_RESIDENCIA == \"SANTA IZABEL DO OESTE\""\
                    " | MUN_RESIDENCIA == \"SANTO ANTONIO DO SUDOESTE\""\
                    " | MUN_RESIDENCIA == \"SAO JOAO\""\
                    " | MUN_RESIDENCIA == \"SAO JORGE D'OESTE\""\
                    " | MUN_RESIDENCIA == \"SAUDADE DO IGUACU\""\
                    " | MUN_RESIDENCIA == \"SULINA\""\
                    " | MUN_RESIDENCIA == \"VERE\""\
                    " | MUN_RESIDENCIA == \"VITORINO\""
'''
#data_frame_sudoeste = data_frame.query(data_frame_query)
#data_frame_sudoeste = data_frame_sudoeste.sort_values(by = 'DATA_DIAGNOSTICO', ascending = True)
#print(data_frame_sudoeste)
#print(data_frame_pato_branco['MUN_RESIDENCIA'].value_counts())
#print(data_frame_francisco_beltrao['MUN_RESIDENCIA'].value_counts())
#print(data_frame_sudoeste['MUN_RESIDENCIA'].value_counts())
#print(data_frame_sudoeste['MUN_RESIDENCIA'].value_counts(normalize=True))
#data_frame_sudoeste_count = data_frame_sudoeste_count.sort_values(by = 'MUN_RESIDENCIA', ascending = True)
#print(data_frame_sudoeste_count)
#print(data_frame_sudoeste['MUN_RESIDENCIA'].value_counts())

#Grafico de barras
#grafico = go.Bar(x = data_frame_sudoeste['MUN_RESIDENCIA'], y = data_frame_sudoeste['MUN_RESIDENCIA'].value_counts())
#py.iplot([grafico])
