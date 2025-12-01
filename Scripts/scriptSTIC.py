import pandas as pd # for pandas information https://www.w3schools.com/python/pandas/default.asp
from pyargon2 import hash

# Read the csv
df = pd.read_csv('')

# remove multiples column
df = df.drop(columns=['ts_ms', 'mac'])

# Documentation for argon2 https://pypi.org/project/pyargon2/
df['username'] = hash(df['username'],"salt")

print(df.head()) 