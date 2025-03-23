import pandas as pd
from scipy import stats

# Configurando a altura do nosso Data Frame
pd.set_option('display.width', None)

df = pd.read_csv('data_folder/clientes_limpeza')

df_filtro_idade = df[df['Idade'] > 100]

#print('Filtro de idade \n', df_filtro_idade[['Nome', 'Idade']])

# Identificar Outiliers com Z-score


z_scores = stats.zscore(df['Idade'].dropna())
outliers_z = df[z_scores >= 3]
print("Outliers pelo Z-Score:\n", outliers_z)

# Filtra outliers com Z-score
df_zscore = df[(stats.zscore(df['Idade']) < 3)]

# Identificar outliers com IQR
Q1 = df['Idade'].quantile(0.25)
Q3 = df['Idade'].quantile(0.75)
IQR = Q3 - Q1

limite_baixo = Q1 - 1.5 * IQR
limite_alto = Q3 + 1.5 * IQR

print("Limites IQR: ", limite_baixo, limite_alto)

# Filtrar outliers com IQR
limite_alto = 100
limite_baixo = 1
df_iqr = df[(df['Idade'] >= limite_baixo) & (df['Idade'] > limite_alto)]
print('Outliers pelo IQR:\n', df_iqr)

#Filtrar enderecos invalidos.
df['Endereço'] = df['Endereço'].astype(str)
df['Endereço'] = df['Endereço'].apply(lambda x: 'Endereco invalido' if len(x.split('\n')) < 3 else x)

#Filtrar campos de texto
df['Nome'] = df['Nome'].apply(lambda x: 'Nome invalido' if isinstance(x, str) and len(x) > 10 else x)
print('Qtd registros com nomes grande:', (df['Nome'] == 'Nome Invalido').sum())

print(df)

# todo salvar dados tratados
# todo adicionar enderecos incompletos e nomes muitos grandes ou tambem incompletos no nosso arquivo
# todo Organizar repositorio