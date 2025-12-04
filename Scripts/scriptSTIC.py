import pandas as pd # for pandas information https://www.w3schools.com/python/pandas/default.asp
from pyargon2 import hash

# Read the csv
# Think in a way to do this iterative way, due to the input of large files
# Verificar chunks_size
df = pd.read_csv('')

# remove multiples column
# dont do drop, just select the ones i want to work with
df = df.drop(columns=['ts_ms', 'mac'])

# Documentation for argon2 https://pypi.org/project/pyargon2/
# nº de iterações fixo, que seja alto mas razoavel para a perfomance
# fazer um dicionário para não repetir chamada da função
# usar time_cost, enconding = b64, variant = i
# o U.U vai no param password e a password dos STIC no salt
df['username'] = hash(df['username'],"salt")

print(df.head()) 