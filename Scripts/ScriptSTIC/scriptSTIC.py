import pandas as pd # for pandas information https://www.w3schools.com/python/pandas/default.asp
from pyargon2 import hash # for more info https://pypi.org/project/pyargon2/
import sys
import os
import json
from dotenv import load_dotenv # for more info https://pypi.org/project/python-dotenv/
 
DEFAULT_CONFIG = {
    "input_file": "input_data_altered.csv",
    "output_file": "output_data.csv",
    "chunk_size": 50000,
    "separator": ";",
    "columns_to_keep": ["ts_iso", "username", "ap", "event"],
    "argon2": {
        "time_cost": 4,
        "variant": "i",
        "encoding": "b64"
    }
}
CONFIG_FILE = 'config.json'
ENV_FILE = '.env'
DEFAULT_ENV_CONTENT = 'SALT_STATIC="CHANGE_TO_A_SECURE_PASSWORD"\n'

# Dictionary used to keep hashes to aviod the process of the same data twice
user_hash_cache = {}

SALT_STATIC = None 
ARGON_CONF = None

def setup_files():
    # Creates config if it doesnt exist
    if not os.path.exists(CONFIG_FILE):
        print(f"Warning: {CONFIG_FILE} not found. Creating a default configuration file...")
        with open(CONFIG_FILE, 'w') as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)

    # Creates env if it doesnt exist
    if not os.path.exists(ENV_FILE):
        print(f"Warning: {ENV_FILE} not found. Creating a default secrets file...")
        with open(ENV_FILE, 'w') as f:
            f.write(DEFAULT_ENV_CONTENT)

def anonimize_user(username):
    # Verify if the value is null
    if pd.isna(username):
        return username
        
    # Convert to string
    username_str = str(username)
    
    # Verify if the name is in the dictionary
    if username_str in user_hash_cache:
        print(f"The user {username_str} is already in the dictionary")
        return user_hash_cache[username_str]
    
    # Argon2 config
    hashed_value = hash(
        password = username_str,
        salt = SALT_STATIC,
        time_cost = ARGON_CONF['time_cost'],          
        variant = ARGON_CONF['variant'],            
        encoding = ARGON_CONF['encoding']     
    )
    
    # Saves the hash and username to the dictionary
    user_hash_cache[username_str] = hashed_value
    return hashed_value

def main():
    # Declare as global so the functions can read the updated value
    global SALT_STATIC, ARGON_CONF
    
    setup_files()

    # Load the conf file and env
    load_dotenv()
    SALT_STATIC = os.getenv("SALT_STATIC")

    # Load settings from conf file
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        
    INPUT_FILE = config['input_file']
    OUTPUT_FILE = config['output_file']
    CHUNK_SIZE = config['chunk_size']
    SEP = config['separator']
    ARGON_CONF = config['argon2']
    COLUMNS_TO_KEEP = config['columns_to_keep']

    print("===================================\n")
    print(f"INPUT_FILE:  {INPUT_FILE}")
    print(f"OUTPUT_FILE: {OUTPUT_FILE}")
    print(f"CHUNK_SIZE:  {CHUNK_SIZE}")
    print(f"SEPARATOR:   '{SEP}'")
    print(f"ARGON_CONF:  {ARGON_CONF}")
    print(f"SALT_STATIC: {SALT_STATIC}") 
    print(f"COLUMNS_TO_KEEP: {COLUMNS_TO_KEEP}") 
    print("===================================\n")

    print(f"Processing the file {INPUT_FILE}...")

    # Generate a new output filename if it already exists
    original_output = OUTPUT_FILE
    file_counter = 1
    while os.path.exists(OUTPUT_FILE):
        # Splits 'data.csv' into 'data' and '.csv'
        base_name, extension = os.path.splitext(original_output)
        # Creates the next file
        OUTPUT_FILE = f"{base_name}{file_counter}{extension}"
        file_counter += 1
        
    print(f"Output will be saved to: {OUTPUT_FILE}")

    first_chunk = True
    counter = 0

    df = pd.read_csv(INPUT_FILE)
    num_row = len(df)
    num_iter = (num_row + CHUNK_SIZE - 1) // CHUNK_SIZE

    print(f"Total number of rows to process: {num_row}...")
    print(f"Total number of necessary iterations: {num_iter}...")

    # Open the CSV file in read mode using pandas
    with pd.read_csv(
        # Path to file to read
        INPUT_FILE,

        # Defines the separator used in the CSV.
        sep=SEP,

        # This tells pandas to ONLY load these specific columns into memory.
        # No need to drop anything later!
        usecols=COLUMNS_TO_KEEP,

        # Instead of reading the whole file into RAM, it reads X rows at a time, defined by CHUNK_SIZE.
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

                # If it's the first chunk, write the header. 
                header=first_chunk
            )

            # Update the flag so next chunks don't write the header
            first_chunk = False
            print(f"Chunk {i+1} processed.")

    print("Processing done")

if __name__ == "__main__":
    main()