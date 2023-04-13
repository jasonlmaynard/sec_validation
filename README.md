This script is meant to test Firepower NGFW (but it can test any security device) using real world threats. The goal is to populate Firepower with events and tune signatures as required - this can be used as a learning tool. NOTE: these are real threats that may compromise your system or systems. 

# sec_validation

#####################
Use at YOUR OWN RISK!
#####################

Restrict the assets used to test and ideally snapshot it. Then revert snap or delete the instance.

Script works on Linux and Windows 

The script performs the following: 
- Pulls Malware EIRCAR and ZOMBIES.PDF (note: ZOMBIES.PDF is marked as bad in Cisco secruity tools for testing) 
- Pings an upstream device to ensure the firewall is passing ICMP
- Performs 4 NMAP scans (XMAS, FIN, NULL and UDP) on an upstream device 
- Performs 1 URL check for Adult Sites - pornhub.com 
- Connects to multiple bad sites by pulling intelligence feeds, parsing the data, removes duplicates
- Pulls bad IPs from Talos 
- Pulls URLS from VXVault 
- Pulls Phishing from OPENPhish

#####################
Use at YOUR OWN RISK!
#####################

Video Example: https://youtu.be/4E5haA-6KUQ 


Screen shots from Firepower 

<img width="949" alt="image" src="https://user-images.githubusercontent.com/45973544/230999368-7cc8f784-868d-4151-ae19-188bdb95ec68.png">

<img width="951" alt="image" src="https://user-images.githubusercontent.com/45973544/230999121-ad23d1e2-b0ac-40f9-a67a-3f44f1711410.png">

<img width="335" alt="image" src="https://user-images.githubusercontent.com/45973544/230999194-c6336927-2d9c-42db-ae45-c344103d02f8.png">

<img width="629" alt="image" src="https://user-images.githubusercontent.com/45973544/230999017-736d9e46-748a-462c-880d-8e31f5dd8b47.png">

<img width="916" alt="image" src="https://user-images.githubusercontent.com/45973544/230998916-0a14ef55-0740-485b-973b-14abb07acedc.png">
