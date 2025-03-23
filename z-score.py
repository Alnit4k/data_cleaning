import numpy as np
import pandas
import pandas as pd
from scipy import stats

# Exemplo de idades

df = pd.read_csv("clientes_limpeza_outliers.csv")

# df_idade = df[df["Idade"]]

# # Media e desvio padrao
# media = np.mean(df_idade)
# desvio_padrao = np.std(df_idade)

# Calculando o Z-score para cada Idade
z_scores = stats.zscore(df["Idade"])

# Exibindo os valores
for i, z in enumerate(z_scores):
    if z > 3:
        print(f"Idade: {df["Idade"].iloc[i]}, Z-score: {z:.2f}")

#TODO entender pq o for esta assim

