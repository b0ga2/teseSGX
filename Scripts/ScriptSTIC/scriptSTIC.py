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
        #print(f"The user {username_str} is already in the dictionary")
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

    # Verify if the value was altered
    if not SALT_STATIC or SALT_STATIC == "CHANGE_TO_A_SECURE_PASSWORD":
        print("Error: You are using the default password in the .env file.")
        print("Please open the .env file and change the SALT_STATIC value to the official secure password.")
        sys.exit(1)

    # Load settings from conf file and validate the json fields
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        print("Error: 'config.json' file not found. Please run the script once to generate it.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Your config.json file has a formatting mistake (maybe a missing comma or quote?).")
        print(f"Technical details: {e}")
        sys.exit(1)
        
    INPUT_FILE = config.get('input_file')
    if not isinstance(INPUT_FILE, str) or not os.path.exists(INPUT_FILE):
        print(f"Error: The input file '{INPUT_FILE}' is invalid or was not found in this folder.")
        sys.exit(1)

    OUTPUT_FILE = config.get('output_file')
    if not isinstance(OUTPUT_FILE, str) or len(OUTPUT_FILE) == 0:
        print("Error: 'output_file' in config.json must be a valid text string (e.g., \"output.csv\").")
        sys.exit(1)

    CHUNK_SIZE = config.get('chunk_size')
    if not isinstance(CHUNK_SIZE, int) or CHUNK_SIZE <= 0:
        print("Error: 'chunk_size' in config.json must be a positive number (e.g., 50000).")
        sys.exit(1)

    SEP = config.get('separator')
    allowed_separators = [';', ',', '.', '/']
    if SEP not in allowed_separators:
        print(f"Error: The 'separator' in config.json is invalid. You provided: '{SEP}'")
        print(f"It must be exactly one of the following characters: {allowed_separators}")
        sys.exit(1)
    if not isinstance(SEP, str) or len(SEP) == 0:
        print("Error: 'separator' in config.json must be a valid text string (e.g., \";\").")
        sys.exit(1)

    COLUMNS_TO_KEEP = config.get('columns_to_keep')
    if not isinstance(COLUMNS_TO_KEEP, list):
        print("Error: 'columns_to_keep' must be a list with brackets, e.g., [\"username\", \"event\"].")
        sys.exit(1)     
    if not all(isinstance(item, str) for item in COLUMNS_TO_KEEP):
        print("Error: Every item in 'columns_to_keep' must be text wrapped in quotes.")
        print("You cannot mix numbers and text or use unquoted numbers.")
        sys.exit(1)
    if "username" not in COLUMNS_TO_KEEP:
        print("Error: The 'username' column is missing from the 'columns_to_keep' list.")
        print("The script needs this column to perform the anonymization. Please add it back.")
        sys.exit(1)

    ARGON_CONF = config.get('argon2')
    valid_variants = ['i', 'd', 'id']
    if ARGON_CONF.get('variant') not in valid_variants:
        print(f"Error: Invalid Argon2 'variant' in config.json.")
        print(f"Available options are: {valid_variants}")
        print(" - 'i'")
        print(" - 'd'")
        print(" - 'id'")
        sys.exit(1)
    valid_encodings = ['raw', 'hex', 'b64']
    if ARGON_CONF.get('encoding') not in valid_encodings:
        print(f"Error: Invalid Argon2 'encoding' in config.json.")
        print(f"Available options are: {valid_encodings}")
        print(" - 'raw': Binary output")
        print(" - 'hex': Hexadecimal string")
        print(" - 'b64': Base64 string")
        sys.exit(1)
    if not isinstance(ARGON_CONF, dict):
        print("Error: 'argon2' in config.json is missing or formatted incorrectly.")
        sys.exit(1)
    if not isinstance(ARGON_CONF.get('time_cost'), int) or ARGON_CONF.get('time_cost') <= 0:
        print("Error: 'time_cost' inside 'argon2' must be a positive integer (e.g., 4).")
        sys.exit(1)
    if not isinstance(ARGON_CONF.get('variant'), str) or not isinstance(ARGON_CONF.get('encoding'), str):
        print("Error: 'variant' and 'encoding' inside 'argon2' must be text strings.")
        sys.exit(1)

    print("\n===================================")
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

    try:
        # Read the header using the separator from config
        df_header = pd.read_csv(INPUT_FILE, sep=SEP, nrows=0)
        actual_columns = df_header.columns.tolist()

        # Check if the requested columns actually exist in the file
        missing_cols = [col for col in COLUMNS_TO_KEEP if col not in actual_columns]
        if missing_cols:
            print(f"\nError: Some columns specified in 'columns_to_keep' DO NOT exist in '{INPUT_FILE}'.")
            print(f"Missing columns: {missing_cols}")
            print(f"Available columns found (using '{SEP}'): {actual_columns}")
            print("Hint: If the available columns look merged together, check the 'separator' in config.json.")
            sys.exit(1)

        print("Calculating total rows...")
        df_count = pd.read_csv(INPUT_FILE, sep=SEP, usecols=[actual_columns[0]])
        num_row = len(df_count)
        del df_count # Clean up memory immediately
        
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        sys.exit(1)

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