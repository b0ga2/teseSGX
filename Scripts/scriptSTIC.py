import pandas as pd # for pandas information https://www.w3schools.com/python/pandas/default.asp

df = pd.read_csv('data.csv')

# remove multiples column
df = df.drop(columns=['ColunaA', 'ColunaB'])

# Alter the value of a column
df['Preco'] = df['Preco'] * 1.23

# Documentation for argon2 https://pypi.org/project/pyargon2/

print(df.to_string()) 