# sec_validation

#####################
Use at YOUR OWN RISK!
#####################

This script is meant to test Firepower NGFW (but it can test any security device) using real world threats. 
The goal is to populate Firepower with events and tune signatures as required - this can be used as a learning tool. 

NOTE: these are real threats that may compromise your system or systems. 

Restrict the assets used to test and ideally snapshot it. Then revert snap or delete the instance.

Script works on Linux and Windows 

The script performs the following: 
- Pulls Malware EIRCAR and ZOMBIES.PDF (note: ZOMBIES.PDF is marked as bad in Cisco secruity tools for testing) 
- Pings an upstream device to ensure the firewall is passing ICMP
- Performs 4 NMAP scans (XMAS, FIN, NULL and UDP) on an upstream device 
- Performs 1 URL check for Adult Sites - playboy.com 
- Connects to multiple bad sites by pulling intelligence feeds, parsing the data, removes duplicates
- Pulls bad IPs from Talos 
- Pulls URLS from VXVault 
- Pulls Phishing from OPENPhish

#####################
Use at YOUR OWN RISK!
#####################
