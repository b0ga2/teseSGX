import subprocess  # Used to run external commands (like nmcli)
import sys         # Used to access system-specific parameters and functions (like stderr for errors)
import pandas as pd
from datetime import datetime
import os
import re

# p1 - .18
# p2 - .20
# p3 - 32,20, 19, 17, 

def parse_iw_scan(interface='wlp4s0'):

    try:
        # We use 'sudo' to ensure proper permissions
        # capture_output=True to capture the stdout
        # text=True to decode the output as text (UTF-8)
        # check=True to raise an error if the command fails
        result = subprocess.run(
            ['sudo', 'iw', 'dev', interface, 'scan'],
            capture_output=True,
            text=True,
            check=True,
            encoding='utf-8'
        )
        stdout = result.stdout
    except FileNotFoundError:
        print(f"Erro: Comando 'iw' ou 'sudo' não encontrado.")
        print("Por favor, instale o 'iw' (package 'iw') e 'sudo'.")
        return []
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar 'iw scan' na interface {interface}:")
        print(e.stderr)
        print("\nCertifique-se que a interface está correta e que tem permissões (sudo).")
        return []

    all_aps_info = []
    
    # The output of 'iw' lists multiple APs.
    # Each one starts with "BSS ". We use this to split the text.
    # We ignore the first element (split[0]) which comes before the first "BSS ".
    ap_chunks = stdout.split('BSS ')[1:]

    if not ap_chunks:
        print(f"Nenhum AP encontrado na interface {interface}.")
        return []

    for chunk in ap_chunks:
        ap_info = {}

        # 1. BSS (MAC Address)
        # The BSS is the first thing in the chunk.
        bss_match = re.match(r'([\da-fA-F:]{17})', chunk)
        if not bss_match:
            continue  # Chunk inválido
        ap_info['BSSID'] = bss_match.group(1)

        # 2. Freq
        freq_match = re.search(r'freq: ([\d\.]+)', chunk)
        if freq_match:
            ap_info['FREQ'] = float(freq_match.group(1))

        # 3. Signal
        signal_match = re.search(r'signal: ([\-\d\.]+) dBm', chunk)
        if signal_match:
            ap_info['SIGNAL'] = float(signal_match.group(1))

        # 4. SSID
        ssid_match = re.search(r'SSID: (.*)', chunk)
        if ssid_match:
            ssid = ssid_match.group(1).strip()
            # Handles hidden SSIDs that appear as \x00
            if r'\x00' in ssid:
                ap_info['SSID'] = '[SSID Oculto]'
            else:
                ap_info['SSID'] = ssid
        else:
            ap_info['SSID'] = '[Sem SSID]'

        if ap_info['SSID'] == "eduroam":
            all_aps_info.append(ap_info)

    return all_aps_info

def find_all_aps_with_nmcli():

    print("Searching for Access Points (APs)...")

    try:
        # Use NetworkManager to perform a new scan, to garantee the most recent APs
        # This command ensures the list of networks is up-to-date.
        # Its necessary to have the Wifi turned on
        subprocess.run(
            ['nmcli', 'device', 'wifi', 'rescan'], 
            check=True,          # If the command returns an error, it will raise an exception
            capture_output=True, # Prevents the command's output from being printed to the console
            text=True,           # Ensures the output is decoded as a string
            timeout=15           # Sets a 15-second timeout to prevent the script from hanging
        )

        # Get the list of available Wi-Fi networks 
        # This command lists all found networks with specific fields in a colon-separated format.
        process = subprocess.run(
            ['nmcli', '--terse', '--fields', 'SSID,BSSID,SIGNAL,CHAN', 'device', 'wifi', 'list'],
            check=True,
            capture_output=True, # Captures the output
            text=True
        )

        # This command is used to obtain the signal field (example: signal: -74 dBm)
        processSignal = subprocess.run(['iw', 'dev','wlp4s0', 'link'],
                                       check = True,
                                       capture_output= True,
                                       text=True)
        


        # Process the output from the first command
        output = process.stdout                     # Get the raw string output from the command
        found_aps = output.strip().split('\n')      # Clean whitespace and split the string into a list, where each item is a network

        # Process the output from the second command
        outputSignal = processSignal.stdout
        signalAP = outputSignal.replace("\t","").strip().split('\n')

        signalSSID = signalAP[0].replace("Connected to ","").replace(":","\\:").upper()
        signalSSID = signalSSID[:23].strip()

        signalValue = signalAP[5].replace("signal: ","")
        
        # Create an empty list to store the entries
        all_aps = []

        # Loop through each line of network data returned by nmcliW
        for network_line in found_aps:
            # The 'terse' format separates fields with a colon ':'
            fields = network_line.split(':')
            
            # A basic check to ensure the line has at least the 4 fields we requested
            if len(fields) >= 4 and fields[0] == 'eduroam':

                # The last field is the channel number   
                channel_str = fields[-1]
                
                # Determine the frequency band based on the channel number
                try:
                    # Convert the channel from a string to an integer for comparison
                    channel_num = int(channel_str)
                    
                    # Ref: https://en.wikipedia.org/wiki/List_of_WLAN_channels

                    # Wi-Fi channels 1-14 are in the 2.4 GHz band. Higher channels are 5 GHz and 6 GHz.
                    if 1 <= channel_num <= 14:
                        band = "2.4 GHz"
                    elif 36 <= channel_num <= 165:
                        band = "5 GHz"
                    elif 1 <= channel_num <= 233 and channel_num > 165:
                        band = "6 GHz"
                    else:
                        band = "Unknown"
                except ValueError:
                    # If the channel is not a valid number, mark it as unknown
                    band = "Unknown"
                             
                bbsid = fields[1:-2]
                bssid_string = ":".join(bbsid)
                signal = ""

                if bssid_string == signalSSID:
                    signal = signalValue
                else:
                    signal = "-"

                # Create a dictionary to hold the structured data for the current AP
                ap_info = {
                    'SSID': fields[0],                            # The name of the network
                    'BSSID': ':'.join(fields[1:-2]),              # The hardware address of the AP
                    'SIGNAL': fields[-2],                 # The signal strength (0-100)
                    'CHANNEL': channel_str,                       # The channel number
                    'BAND': band,                                 # The calculated frequency band
                    'SIGNAL VALUE': signal
                }

                # Add the dictionary for this AP to our main list
                all_aps.append(ap_info)

        return all_aps
    except FileNotFoundError:
        # This error occurs if the 'nmcli' command itself is not found
        print("Error: 'nmcli' command not found. Please ensure NetworkManager is installed.", file=sys.stderr)
        return None
    
    except subprocess.CalledProcessError as e:
        # This error occurs if the nmcli command returns a non-zero exit code (an error)
        print(f"Error executing nmcli: {e.stderr}", file=sys.stderr)
        return None
        
    except subprocess.TimeoutExpired:
        # This error occurs if the 'rescan' command takes longer than the timeout value
        print("Error: The network scan took too long to respond.", file=sys.stderr)
        return None

def get_room_and_position():

    if len(sys.argv) < 2:
        print("Room wasnt passed as a argument")
        exit(1)

    print("\n=== Room and Position Information ===")
    
    # Get room name
    room = sys.argv[1]
    
    # Get position
    print("\nAvailable positions:")
    print("1. Center")
    print("2. Top Left")
    print("3. Top Right")
    print("4. Bottom Left")
    print("5. Bottom Right")

    position_choice = input("Select position (1-5): ").strip()
    position_map = {
        '1': 'Center',
        '2': 'Top Left',
        '3': 'Top Right',
        '4': 'Bottom Left',
        '5': 'Bottom Right'
    }
    
    while position_choice not in position_map:
        print("Invalid choice! Please select 1-5.")
        position_choice = input("Select position (1-5): ").strip()
    
    return room, position_map[position_choice]

def save_to_excel(aps, room, position, filename):
    if not aps:
        print("No data to save :(")
        return False

    try:
        # Add room and position information to each AP entry
        for ap in aps:
            ap['ROOM'] = room
            ap['POSITION'] = position
            ap['TIMESTAMP'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Create DataFrame
        df = pd.DataFrame(aps)
        
        # TODO: Reorder columns for better readability
        column_order = ['TIMESTAMP', 'ROOM', 'POSITION', 'SSID', 'BSSID','SIGNAL' , 'FREQ']
        df = df[column_order]
        
        # Check if file already exists
        if os.path.exists(filename):
            # Load existing data and append new data
            existing_df = pd.read_excel(filename)
            combined_df = pd.concat([existing_df, df], ignore_index=True)
        else:
            # Create new file
            combined_df = df
        
        # Save to Excel
        combined_df.to_excel(filename, index=False)
        
        print(f"\nData successfully saved to {filename}")
        print(f"Room: {room}")
        print(f"Position: {position}")
        print(f"Total APs found: {len(aps)}")
        print(f"Total records in file: {len(combined_df)}")
        
        return True
        
    except Exception as e:
        print(f"Error saving to Excel: {e}", file=sys.stderr)
        return False
    
def display_current_data(aps, room, position):
    if not aps:
        print("\nNo Access Points found.")
        return
    
    print(f"\n=== Scan Results - Room: {room}, Position: {position} ===")
    print(f"Found {len(aps)} Access Points:\n")
    
    # Print a formatted table header
    print(f"{'SSID':<25} {'BSSID':<20} {'SIGNAL':<10} {'FREQ':<10}")
    print("-" * 80)
    
    # Loop through the sorted list and print the details of each AP
    for ap in aps:
        print(f"{ap['SSID']:<25} {ap['BSSID']:<20} {ap['SIGNAL']:<10} {ap['FREQ']:<10}")

def main():

    INTERFACE_WIRELESS = "wlp4s0"
    position = ""
    while position != "Bottom Right":
        # Get room and position information
        room, position = get_room_and_position()

        # Scan for APs
        aps = parse_iw_scan(INTERFACE_WIRELESS)
        
        if aps is not None:
            # Display results
            display_current_data(aps, room, position)
            
            save_choice = input("\nSave results to Excel? (y/n): ").strip().lower()
            
            if save_choice in ['y', 'yes']:

                filename = "Rooms/wifi_scan_results_"+room+".xlsx"

                # Save to Excel
                save_to_excel(aps, room, position, filename)
            else:
                print("Results not saved.")  
if __name__ == "__main__":
    main()