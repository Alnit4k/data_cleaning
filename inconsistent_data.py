import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('./data_folder/clientes_limpeza')

print(df.head())

# Mascarar dados pessoais
df['cpf_mascara'] = df['CPF'].apply(lambda cpf: f'{cpf[:3]}.***.***-{cpf[-2:]}')

# Corrigir datas e colocar no formato correto
df['data'] = pd.to_datetime(df['Data'], format='%Y-%m-%d', errors='coerce')

data_atual = pd.to_datetime('today')
df['data_atualizada'] = df['data'].where(df['data'] <= data_atual, pd.to_datetime('1900-01-01'))
df['idade_ajustada'] = data_atual.year - df['data_atualizada'].dt.year
df['idade_ajustada'] -= ((data_atual.month - df['data_atualizada'].dt.month) & (data_atual.day < df['data_atualizada'].dt.day)).astype(int)
df.loc[df['idade_ajustada'] > 100, 'idade_ajustada'] = np.nan

# Corrigir campos com informacoes
df['endereco_curto'] =df['Endereço'].apply(lambda x: x.split('\n')[0].strip())

# Verificando a formatacao do endereco
df['endereco_curto'] = df['Endereço'].apply(lambda x: 'Endereco invalido' if len(x) > 50 or len(x) < 5 else x)

# Corrigir dados erroneos
df['cpf'] = df['CPF'].apply(lambda x: x if len(x) == 14 else 'CPF invalido')

df['CPF'] = df['cpf_mascara']
df['Idade'] = df['idade_ajustada']
df['Endereço'] = df['endereco_curto']
df_salvar = df[['Nome','CPF','Idade', 'Endereço']]
df_salvar.to_csv('clientes_tratados.csv', index=False)

