import os
import pandas as pd

from teste_folder import folder_path

#Criando repositorio para salvar dados

data = 'data_folder'

folder_path = os.path.join(os.getcwd(), data)

os.makedirs(folder_path, exist_ok=True)

df = pd.read_csv('clientes.csv')

#print(df.head().to_string()) #Mostra as 5 primeiras linhas

#print(df.tail().to_string()) #Mostra as 5 ultimas linhas

#print('Mount', df.shape) #mostra a quantidade de culunas e linhas respectivamente

#print('Data Type:\n', df.dtypes) #Mostra os tipos de dados das colunas

print('Null values:\n', df.isnull().sum())

csv_file_path = os.path.join(folder_path, 'clientes.csv')
df.to_csv(csv_file_path, index=False)