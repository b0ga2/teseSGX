import pandas as pd # for pandas information https://www.w3schools.com/python/pandas/default.asp
from pyargon2 import hash
import sys
import os

# Read the csv
# Think in a way to do this iterative way, due to the input of large files
# Use chunks_size
# df = pd.read_csv('')

# remove multiples column
# dont do drop, just select the ones i want to work with
# df = df.drop(columns=['ts_ms', 'mac'])

# Documentation for argon2 https://pypi.org/project/pyargon2/
# nº de iterações fixo, que seja alto mas razoavel para a perfomance
# fazer um dicionário para não repetir chamada da função
# usar time_cost, enconding = b64, variant = i
# o U.U vai no param password e a password dos STIC no salt


# Conf
INPUT_FILE = 'input_data_10000x.csv'
OUTPUT_FILE = 'dados_anonimizados.csv'
CHUNK_SIZE = 50000 # TODO: Test this value somehow
SALT_STATIC = "password_dos_STIC" # This is a password introduced by STICK

# Dictionary used to keep hashes so we dont process the same data twice
user_hash_cache = {}

def anonimize_user(username):
    # Verify if the value is null
    if pd.isna(username):
        return username
        
    # Convert to string
    username_str = str(username)
    
    # Verify if the name is in the dictionary
    if username_str in user_hash_cache:
        #print(f"The user {username_str} is already in the dictionary")
        return user_hash_cache[username_str]
    
    # Argon2 config
    # time_cost: 4 TODO: verificar este valor
    # type: 'i' (Argon2i) 
    # encoding: 'b64' (Base64)
    hashed_value = hash(
        password = username_str,
        salt = SALT_STATIC,
        time_cost = 4,          
        variant = 'i',            
        encoding = 'b64'       
    )
    
    # Saves the hash and username to the dictionary
    user_hash_cache[username_str] = hashed_value
    return hashed_value


print(f"Processing the file {INPUT_FILE}...")

# Verify if file exists
if os.path.exists(OUTPUT_FILE):
    os.remove(OUTPUT_FILE)

first_chunk = True

counter = 0

df = pd.read_csv(INPUT_FILE)
num_row = len(df)
num_iter = (num_row + CHUNK_SIZE - 1) // CHUNK_SIZE


print(f"Total number of rows to process: {num_row}...")
print(f"Total number of necessary iterations: {num_iter}...")

# Open the CSV file in read mode using pandas
with pd.read_csv(
    # The path to the file you want to read
    INPUT_FILE,

    # Defines the separator used in the CSV.
    # Since your file uses ';', we must specify it, otherwise pandas looks for ','
    sep=';',

    # Activates the "chunking" mode.
    # Instead of reading the whole file into RAM, it reads X rows at a time (defined by CHUNK_SIZE).
    # This returns an iterator (TextFileReader) rather than a single DataFrame.
    chunksize=CHUNK_SIZE
) as reader:

    # Iterate through the file in chunks
    for i, chunk in enumerate(reader):

        # Convert the column to string and remove leading/trailing whitespace
        chunk['username'] = chunk['username'].astype(str).str.strip()

        # Apply the anonymization function to the column
        chunk['username'] = chunk['username'].map(anonimize_user)

        # Write the processed chunk to the output file
        chunk.to_csv(
            # The destination file path
            OUTPUT_FILE,

            # Use the same separator
            sep=';',

            # append
            mode='a',

            # No write index 
            index=False,

            # If it's the first chunk, write the header (True). 
            header=first_chunk
        )

        # Update the flag so next chunks don't write the header
        first_chunk = False
        print(f"Chunk {i+1} processed.")

print("Processing done")
