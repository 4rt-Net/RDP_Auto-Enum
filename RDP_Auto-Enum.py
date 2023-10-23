import re
import subprocess

pattern = r'(\d+\.\d+\.\d+\.\d+)\s+.*?3389/tcp\s+open'

def extract_ip_addresses(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        input_data = input_file.read()
        
        matches = re.findall(pattern, input_data, re.DOTALL)
    
    with open(output_file_path, 'w') as output_file:
        for ip_address in matches:
            output_file.write(ip_address + '\n')
    return output_file_path

def run_nmap_scan(ip_addresses_file, output_scan_file):
    nmap_command = f'nmap --script "rdp-enum-encryption or rdp-vuln-ms12-020 or rdp-ntlm-info" -p 3389 -T4 -iL {ip_addresses_file} -oN {output_scan_file}'
    try:
        result = subprocess.run(nmap_command, shell=True, check=True, stdout=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f'Nmap scan failed: {e}')

input_file_path = 'nmap_file.txt' #Change the input file as needed
output_file_path = 'rdp_extraction_results.txt' #Change the output file as needed
output_scan_file = 'nmap_scan_results.txt' #Change the final RDP enumeration scan output file as needed

ip_addresses_file = extract_ip_addresses(input_file_path, output_file_path)
run_nmap_scan(ip_addresses_file, output_scan_file)
