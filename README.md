# RDP_Auto-Enum
script to automatically extract addresses with open RDP ports from nmap results and enumerate them using the nmap NSE.

No editing of initial nmap scan results are needed, simply throw the whole nmap results .txt file into the script and it will search for hosts that has an RDP port open, once all these hosts are found they will be written to a file and ingested again to start NSE scans against the rdp ports. 
