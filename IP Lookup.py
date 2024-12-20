import requests
import os

def get_ip_location(ip_address):
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Could not retrieve data for {ip_address}."}
    except Exception as e:
        return {"error": str(e)}

def read_ips_from_file(filename):
    try:
        with open(filename, 'r') as file:
            ips = file.read().splitlines()
            return [ip.strip() for ip in ips if ip.strip()]  
    except FileNotFoundError:
        return None  #
    except Exception as e:
        return {"error": str(e)}
      
def main():
    while True:  #
        ip_file = 'ip.txt'
        
        
        ip_list = read_ips_from_file(ip_file)
        
        if ip_list is None:
            print("ip.txt not found. Please enter IP addresses manually.")
            ip_addresses = input("Enter IP addresses (comma separated): ")
            ip_list = [ip.strip() for ip in ip_addresses.split(',')]
        
        # ANSI escape codes for colors
        green_color = "\033[92m"    # Green
        blue_color = "\033[94m"     # Blue
        yellow_color = "\033[93m"   # Yellow
        pink_color = "\033[95m"     # Pink
        red_color = "\033[91m"      # Red
        reset_color = "\033[0m"     # Reset to default

        for ip in ip_list:
            location_info = get_ip_location(ip)
            
            if "error" in location_info:
                print(red_color + location_info["error"] + reset_color)
            else:
                print(f"\n{green_color}IP Address:{reset_color} {location_info.get('ip')}")
                print(f"{blue_color}City:{reset_color} {location_info.get('city')}")
                print(f"{red_color}Region:{reset_color} {location_info.get('region')}")
                print(f"{pink_color}Country:{reset_color} {location_info.get('country')}")
                print(f"{yellow_color}Location:{reset_color} {location_info.get('loc')}")
                print(f"{blue_color}Organization:{reset_color} {location_info.get('org')}")

        restart = input("\nPress Enter to continue, type 'q' to exit: ")
        if restart.lower() == 'q':
            print("")
            break  

if __name__ == "__main__":
    main()
