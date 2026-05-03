#!/usr/bin/python
# @nu11secur1ty
# run as administrator in Windows 11
import subprocess
import re

def get_wifi_passwords():
    try:
        # Get all saved profiles
        raw_profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], stderr=subprocess.STDOUT)
        profiles_data = raw_profiles.decode('cp1251', errors='replace')
        profile_names = re.findall(r":\s(.*)", profiles_data)
        
        wifi_results = []

        for name in profile_names:
            name = name.strip()
            if not name:
                continue
            
            try:
                # Get detailed info for each profile, including the password (key=clear)
                profile_info_raw = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear'], stderr=subprocess.STDOUT)
                profile_info = profile_info_raw.decode('cp1251', errors='replace')
                
                # Look for the password field (Key Content)
                password_match = re.search(r"(?:Key Content|Съдържание на ключа)\s*:\s(.*)", profile_info)
                
                password = password_match.group(1).strip() if password_match else "-- No Password / Open --"
                wifi_results.append({"ssid": name, "password": password})
                
            except subprocess.CalledProcessError:
                wifi_results.append({"ssid": name, "password": "ERROR: Could not retrieve"})

        return wifi_results

    except Exception as e:
        return f"System Error: {e}"

def main():
    print("--- nu11secur1tyAI WiFi & Password Recovery ---")
    print("Running on Windows 11...\n")
    
    results = get_wifi_passwords()

    if isinstance(results, list):
        # Create a simple table-like output
        header = f"{'#':<3} | {'SSID (Network Name)':<25} | {'Password':<20}"
        print(header)
        print("-" * len(header))
        
        for i, data in enumerate(results, 1):
            print(f"{i:<3} | {data['ssid']:<25} | {data['password']:<20}")
    else:
        print(results)

if __name__ == "__main__":
    main()
