__author__ = 'Jason Maynard'

print ('     ____                               _____                                       .___')
print ('    |    |____    __________   ____     /     \ _____  ___.__. ____ _____ _______  __| _/')
print ('    |    \__  \  /  ___/  _ \ /    \   /  \ /  \\__  \<   |  |/    \\__  \\_  __ \/ __ |')
print ('/\__|    |/ __ \_\___ (  <_> )   |  \ /    Y    \/ __ \\___  |   |  \/ __ \|  | \/ /_/ |')
print ('\________(____  /____  >____/|___|  / \____|__  (____  / ____|___|  (____  /__|  \____ |')
print ('              \/     \/           \/          \/     \/\/         \/     \/           \/') 
print ()
print ('Please run "pip install -r requirements before running the script"')
print ()
print ()
#
import os.path
from sys import platform

#######################################################################################################################
#ICMP Gateway Test
#######################################################################################################################
print ('The IP used below will be used for ICMP and NMAP')
varGW = input ('Enter IP address of upstream device beyond the Firepower: ')

if platform == "linux" or platform == "linux2":
    varPING = os.system ('ping -c 1 ' + varGW)
elif platform == "win32" or platform == "win64":
    varPING = os.system ('ping -n 1 ' + varGW)

if varPING == 0:
    print ()
    print ('################################################################')
    print (varGW, 'is up  !!!!!!!!!!!!')
    print ('################################################################')
else:
    print ()
    print ('################################################################')
    print (varGW, 'is down  ..........')
    print ('################################################################')
#######################################################################################################################
#NMAP Portscan
#######################################################################################################################
print ()
print ('################################################################')
print ('NMAP Scans XMAS, FIN, NULL, and UDP will run!')
print ('################################################################')

#varNMAPPATH = ('"c:\\Program Files (x86)\\Nmap\\nmap.exe"')
varNMAPPATH = ('nmap')

print ('Performing XMAS ...................')
varXMAS = os.system (varNMAPPATH + ' -sX ' + varGW)
if varXMAS == 0:
    print ('################################################################')
    print (varGW, 'XMAS Scan Complete. Check for IPS for PSNG Alert!')
    print ('################################################################')
else:
    print ('Please ensure that nmap is installed')

print ('Performing TCP FIN Scan ...................')
varFIN = os.system (varNMAPPATH + ' -sF ' + varGW)
if varFIN == 0:
    print ('################################################################')
    print (varGW, 'TCP FIN Scan Complete. Check for IPS for PSNG Alert!')
    print ('################################################################')
else:
    print ('Please ensure that nmap is installed')

print ('Performing TCP NULL Scan ...................')
varNULL = os.system (varNMAPPATH + ' -sN ' + varGW)
if varNULL == 0:
    print ('################################################################')
    print (varGW, 'TCP NULL Scan Complete. Check for IPS for PSNG Alert!')
    print ('################################################################')
else:
    print ('Please ensure that nmap is installed')

print ('Performing UDP Scan ...................')
varUDP = os.system (varNMAPPATH + ' -sU ' + varGW)
if varUDP == 0:
    print ('################################################################')
    print (varGW, 'UDP Scan Complete. Check for IPS for PSNG Alert!')
    print ('################################################################')

else:
    print ('Please ensure that nmap is installed')

print ()
print ('################################################################')
print ('All NMAP Scans Complete')
print ()
print ('As of 7.x you can enabled portscan from the policy "advanced" tab.') 
print ('Enable detection or  prevention of portscan mode and deploy')
print ()
print ('Details below on what IPS signatures need to be enabled')
print ('Enable all GID:122 IPS and set to drop and generate events')
print ('################################################################')