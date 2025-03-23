# Importando a biblioteca para manipulacao de dados
import os
import pandas as pd

from data_cleaning_1 import csv_file_path, folder_path

# inserindo os dados e indexando a coluna "nome"

df = pd.read_csv("./clientes2.csv", index_col="ID_Cliente")
pd.set_option("display.width", None)

# Removendo dados desnecessarios
# Como nao temos nenhum dado para remover, podemos deixar como esta

# Normalizando os campos de texto
df['Nome'] = df['Nome'].str.title()
df['Endereço'] = df['Endereço'].str.lower()

# Tratar valores nulos
# Primeiro irei conferir a quantidade de valores nulos que tenho

print('valores nulos: \n', df.isnull().sum(), df.isnull().sum().sum())

# Agora, teremos varias opcoes para o tratamento, dependendo da situacao podemos combinar algumas,
# Mas geralmente utilizaremos apenas uma

df_fillna = df.fillna(0) # Substituir valores nulos por 0
df_dropna = df.dropna() # Remover registro com valores nulos
df_dropna4 = df.dropna(thresh=4) # Manter registros com no minimo 4 valores nao nulos
df = df.dropna(subset=['CPF']) # Remover registro de uma determinada coluna


print('Qtd de registros nulos com fillna:', df_fillna.isnull().sum().sum())

print('Qtd de registros nulos com fillna: ', df_dropna.isnull().sum().sum())
print('Qtd de registros nulos com fillna:', df_dropna4.isnull().sum().sum())
print('Qtd de registros nulos com fillna:', df.isnull().sum().sum())

# Outra forma tambem de usar o fillna e fazeno o preenchimento com outros valores
df.fillna({'Email': 'Desconhecido'}, inplace=True)
df['Endereço'] = df['Endereço'].fillna('Endereco nao informado')

#Converter tipos de dados

df['Idade'] = df['Idade'].astype(int)

# Tratar formato de dado

df['data_corrigida'] = pd.to_datetime(df['Data_de_Nascimento'], format='%d/%m/%Y', errors='coerce' )

# Tratar dados duplicados
print('Qtd registros atual:', df.shape[0])
df.drop_duplicates(subset='CPF', inplace=True)

# Salvando modificacoes e ordenando o dataframe
df['Data'] = df['data_corrigida']
df_salvar = df[['Nome', 'CPF', 'Idade', 'Data', 'Endereço']]

folder_path = '/Users/alnit/PycharmProjects/data_cleaning/data_folder'
csv_file_path = os.path.join(folder_path, 'clientes_limpeza')

df_salvar.to_csv(csv_file_path, index=False)

print(df)

