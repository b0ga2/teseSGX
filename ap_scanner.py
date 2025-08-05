import subprocess
import sys

def find_aps_eduroam():
 
    print("Searching for APs 'eduroam'...")

    try:
        ## runs the command
        subprocess.run(['nmcli', 'device', 'wifi', 'rescan'], 
                       check=True, #Throws an exception if a error is found
                       capture_output=True, #Allowa to capture the output with stoud
                       text=True)

        # Lists all available Aps, with the command nmcli --terse --fieds
        processo = subprocess.run(
            ['nmcli', '--terse', '--fields', 'SSID,BSSID,SIGNAL,CHAN', 'device', 'wifi', 'list'],
            check=True,
            capture_output=True,
            text=True
        )

        output = processo.stdout
        found_aps = output.strip().split('\n')

        aps_eduroam = []
        for rede in found_aps:
            # O formato terse separa os campos com ':'
            campos = rede.split(':')
            if len(campos) >= 4 and campos[0] == 'eduroam':
                ap_info = {
                    'SSID': campos[0],
                    'BSSID': ':'.join(campos[1:-2]), # O BSSID pode conter ':'
                    'SIGNAL': campos[-2],
                    'CHANNEL': campos[-1]
                }
                aps_eduroam.append(ap_info)

        return aps_eduroam

    except FileNotFoundError:
        print("Error: nmcli gave an error, install NetworkManager ", file=sys.stderr)
        return None
    except subprocess.CalledProcessError as e:
        print(f"nmcli error: {e.stderr}", file=sys.stderr)
        return None

def main():
    aps = find_aps_eduroam()

    if aps is not None:
        if aps:
            print(f"\nFound {len(aps)} Access Points 'eduroam':\n")
            print(f"{'SSID':<15} {'BSSID':<20} {'SIGNAL (%)':<10} {'CHANNEL':<5}")
            print("-" * 60)
            for ap in aps:
                print(f"{ap['SSID']:<15} {ap['BSSID']:<20} {ap['SIGNAL']:<10} {ap['CHANNEL']:<5}")
        else:
            print("\nNo AP found")

if __name__ == "__main__":
    main()