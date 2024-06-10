# Converta o seguinte dicionário para DataFrame e obtenha:
# Sumário de cada coluna
# Média da coluna idade
# Último nome da coluna nome

# dados = {“nome”:[“Téo”, “Nah”, “Napoleão”], “idade”: [31, 32, 14]}

# %%
import pandas as pd

dados = {"nome":["Téo", "Nah", "Napoleão"], "idade": [31, 32, 14]}
dados_df = pd.DataFrame(dados)
dados_df

# %%
sumario = dados_df.describe()
sumario

# %%
dados_df["nome"]

# %%
dados_df["idade"]

# %%
# Primeira forma de achar a média
dados_df["idade"].mean()

# %%
# Segunda forma de achar a media
sumario["idade"]["mean"]

# %%
# Primeira forma de achar o ultimo nome da coluna nome
dados_df["nome"].iloc[-1]

# %%
# Segunda forma de achar o ultimo nome da coluna nome
dados_df["nome"].tail(1)