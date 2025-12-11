import pandas as pd

# Carregar o dataset original
df = pd.read_csv("input_data.csv")

# Número de réplicas
N = 10000

# Replicar o dataset 10000 vezes
df_big = pd.concat([df] * N, ignore_index=True)

# Guardar o resultado
df_big.to_csv("input_data_10000x.csv", index=False)
