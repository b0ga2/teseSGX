# Script Overview & Configuration Guide

This document explains the mechanics of the script for data anonimization and provides an overview of its configuration files.

## 1. System Preparation (Virtual Environment)

To ensure the script runs without affecting your computer's global settings, it operates inside an isolated folder called a Virtual Environment (`venv`).

**Step 1: Create the Virtual Environment (First Time Only)**
Open the command line, navigate to the folder containing the script, and run the following command to create the environment:
```bash
python -m venv venv
```

**Step 2: Activate the Virtual Environment**
To activate the environment every time before running the script. Run the appropriate command for the operating system used:

**Windows:**
```DOS
venv\Scripts\activate
```

**macOS / Linux:**
```Bash
source venv/bin/activate
```

(Note: You will know it is successfully activated when you see (venv) appear at the very beginning of your command line prompt).

**Step 3: Install Required Libraries (First Time Only)**
Once the environment is active, install the necessary dependencies from the included requirements file by running:

```Bash
pip install -r requirements.txt
```

## 2. Code Explanation & Core Logic

The script is designed to process datasets without running out of memory, it achieves this through the following sequence:

1. **Initialization:** The script automatically detects if the required configuration files (`.env` and `config.json`) exist. If they do not, it creates them with default values, to verify these open the script.

2. **Memory Management (Chunking & Filtering):** Instead of loading the entire input file to memory, the script uses chunking, it reads the file in blocks (e.g., 50,000 rows at a time). Additionally, it loads only the columns specified in the configuration, ignoring all irrelevant data right from the start.

3. **Cryptographic Hashing:** For each chunk, the script isolates the `username` column. It applies the **Argon2** hashing algorithm, combining the user's data with the "salt" defined in the `.env` file. A local caching dictionary is used to remember previously hashed usernames, speeding up the process for recurring users.

4. **Safe Output:** The processed chunk is appended to a new output file. If the designated output file name already exists, the script creates a new version (e.g., `output_data1.csv`, `output_data2.csv`) to prevent data loss.

---

## 3. Credentials (`.env` File)

The `.env` file acts as a vault for the cryptographic salt. **This file contains sensitive information and must strictly remain local. Do not share it or upload it to any shared repository.**

If you open the `.env` file, you will see the following structure:

```env
SALT_STATIC="CHANGE_TO_A_SECURE_PASSWORD"
```

**This is the default value and should be changed or shared.**

## 4. Operational Parameters (`config.json` File)

The `config.json` file serves as the control panel for the script. It uses standard JSON formatting. You can edit this file in any standard text editor to adjust how the script processes your data.

Here is the default structure of the configuration file:

```json
{
    "input_file": "input_data.csv",
    "output_file": "output_data.csv",
    "chunk_size": 50000,
    "separator": ";",
    "columns_to_keep": [
        "ts_iso",
        "username",
        "ap",
        "event"
    ],
    "argon2": {
        "time_cost": 4,
        "variant": "i",
        "encoding": "b64"
    }
}
```

* **`input_file`**: The exact filename of the source CSV file intended to process. It must reside in the same directory as the script. 
Example: `"input_data.csv"`

* **`output_file`**: The desired filename for the final, anonymized data. If this file already exists, the script will append an incremental number to the filename to avoid overwriting. 
Example: `"output_data.csv"`

* **`chunk_size`**: The number of rows processed per batch. Reduce this number if the host machine experiences memory constraints. 
Example: `50000`

* **`separator`**: The delimiter character used in the source CSV file. This is typically a semicolon (`;`) or a comma (`,`). 
The file given to the student was using `;` so that is the default value.

* **`columns_to_keep`**: Only the columns explicitly listed here will be loaded into system memory. 
The columns necessary for the development phase are `["ts_iso", "username", "ap", "event"]`.

* **`argon2`**: The cryptographic parameters for the hashing engine, more information about the used value and others availabe please verify https://pypi.org/project/pyargon2/ for the library used and for information on Argon2 check the RFC https://www.rfc-editor.org/rfc/rfc9106.html
