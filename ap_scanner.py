import subprocess  # Used to run external commands (like nmcli)
import sys         # Used to access system-specific parameters and functions (like stderr for errors)
import pandas as pd
from datetime import datetime
import os


def find_all_aps():

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
        print("No data to save!")
        return False

    try:
        # Add room and position information to each AP entry
        for ap in aps:
            ap['ROOM'] = room
            ap['POSITION'] = position
            ap['TIMESTAMP'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Sort the data
        aps.sort(key=lambda x: (x['BAND'], -int(x['SIGNAL'])))
        
        # Create DataFrame
        df = pd.DataFrame(aps)
        
        # Reorder columns for better readability
        #column_order = ['TIMESTAMP', 'ROOM', 'POSITION', 'SSID', 'BSSID', 'SIGNAL', 'CHANNEL', 'BAND']
        column_order = ['TIMESTAMP', 'ROOM', 'POSITION', 'SSID', 'BSSID', 'SIGNAL', 'SIGNAL VALUE' , 'CHANNEL', 'BAND']
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
    print(f"{'SSID':<25} {'BSSID':<20} {'SIGNAL (%)':<10} {'SIGNAL VALUE':<15} {'CHANNEL':<7} {'BAND':<10}")
    print("-" * 80)
    
    # Loop through the sorted list and print the details of each AP
    for ap in aps:
        print(f"{ap['SSID']:<25} {ap['BSSID']:<20} {ap['SIGNAL']:<10} {ap['SIGNAL VALUE']:<15} {ap['CHANNEL']:<7} {ap['BAND']:<10}")

def main():

    position = ""
    while position != "Bottom Right":
        # Get room and position information
        room, position = get_room_and_position()
        
        print(type(position))
        print(position)

        # Scan for APs
        aps = find_all_aps()
        
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