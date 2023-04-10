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

import os
import os.path
import urllib.request
import socket
from colorama import init
from termcolor import colored

#'pip install colorama'
#'pip install termcolor'

#######################################################################################################################
#Download EICAR
#######################################################################################################################

print ()
print (colored('################################################################', 'green'))
print (colored('Pulling Eicar', 'red'))
print (colored('################################################################', 'green'))

try:
    urllib.request.urlretrieve('http://www.eicar.org/download/eicar.com.txt', 'eircar.com.txt')
except (ConnectionResetError) as e:
    print ('Connection reset!')
except (urllib.request.URLError) as e:
    print ('URL Error. Perhaps URL has been changed')
else:
    print ('Downloaded Eicar!  Check Firepower Unified Events!')
    print ()
    print ('################################################################')

#######################################################################################################################
#PULL MALWARE - Malware Zombies (marked as Malware in AMP Cloud for testing)
#######################################################################################################################
print ()
print (colored('################################################################', 'green'))
print (colored('Pulling Zombies.pdf', 'red'))
print (colored('################################################################', 'green'))

try:
    urllib.request.urlretrieve('http://www.cloudyip.net/AMP/Zombies.pdf', 'Zombies.pdf')
except ConnectionResetError as e:
    print ('Connection reset!')
except urllib.request.URLError as e:
    print ('URL Error. Perhaps URL has been changed')
    
#Finished Print Details    
print ('Downloaded Zombies!  Check Firepower Unified Events!')
print ()
print ('################################################################')

#######################################################################################################################
#Connect to Adult URL Category - this is to check that content filtering is enabled. 
#######################################################################################################################
print ()
print (colored('################################################################', 'green'))
print (colored('Connect to Adult URL Category', 'red'))
print (colored('################################################################', 'green'))

try:
    urllib.request.urlretrieve ('http://www.playboy.com')
except urllib.request.URLError as e:
    print ('DNS Lookup Failed!')
except NameError as e:
    print ('Name Error but keep going!!!')
except ConnectionResetError as e:
    print ('Connection Reset Error')
except TimeoutError as e:
    print ('Timed out but keep going in the name of security')

#Finished Print Details 
print ('Connected to an Adult Site - Check URL Cateogries!!!')
print ('Check for look for playboy.com to validate this test')
print ('################################################################')

#######################################################################################################################
#Connecting to BAD IPs Classified by Cisco Talos 
#######################################################################################################################
print ()
print (colored('################################################################', 'green'))
print (colored('Starting Connections to BAD IPs Classified by Cisco Talos', 'red'))
print (colored('################################################################', 'green'))

urllib.request.urlretrieve ('https://www.talosintelligence.com/documents/ip-blacklist', 'ip-blacklist.txt')
f = open('ip-blacklist.txt','r')
for line in f:
    try:
        print (line)
        urllib.request.urlopen ('http://' + (line), timeout=1)
    except urllib.error.URLError as e: 
        print('http://' + (line))
        print('Most likely blocked!')
    except socket.timeout as e:
        print ('Socket Timeout - Could be Blocked!.')
    except Exception as e:
        print (e)
f.close()

#######################################################################################################################
#PULL VX_Vault Sites
#######################################################################################################################
print ()
print (colored('################################################################', 'green'))
print (colored('Pulling VX Vault - Ugly Sites', 'red'))
print (colored('################################################################', 'green'))

varVXVault = urllib.request.urlretrieve ('http://vxvault.net//URL_List.php', 'VXVault.txt')
with open("VXVault.txt", "r") as input_file:
    with open("VXVault_JM.txt", "w") as output_file:
        for line in input_file:
            if "http" in line:
                output_file.write(line)

f = open('VXVault_JM.txt','r')
for line in f:
    try:
        print (line)
        urllib.request.urlopen ((line), timeout=1)
    except urllib.request.URLError as e:
        print ('DNS Lookup Failed! Perhaps domain pulled')
    except NameError as e:
        print ('Name Error! To infinity an beyond!')
    except ConnectionResetError as e:
        print ('Connection Reset Error! Blocking')
    except TimeoutError as e:
        print ('Timed out but keep going in the name of security')
    except socket.timeout as e:
        print ('Socket Timeout - Moving on........')
    except Exception as e:
        print (e)
f.close()

#######################################################################################################################
#PULL PHISHING DOMAINS
#######################################################################################################################
print ()
print (colored('################################################################', 'green'))
print (colored('Pulling SPAM and Other sites from OpenPhish', 'red'))
print (colored('################################################################', 'green'))

varPULLPHISH = urllib.request.urlretrieve ('https://openphish.com/feed.txt', 'phish.txt')

f = open('phish.txt','r')
for line in f:
    try:
        print (line)
        urllib.request.urlopen ((line), timeout=1)
    except urllib.request.URLError as e:
        print ('DNS Lookup Failed! Perhaps domain pulled')
    except NameError as e:
        print ('Name Error! To infinity an beyond!')
    except ConnectionResetError as e:
        print ('Connection Reset Error! Blocking')
    except TimeoutError as e:
        print ('Timed out but keep going in the name of security')
    except socket.timeout as e:
        print ('Socket Timeout - Moving on........')
    except Exception as e:
        print (e)
f.close()

print (colored('################################################################', 'green'))
print (colored('################################################################', 'green'))
print (colored('################################################################', 'green'))
print ()
print (colored('Connected to Dirty Sites', 'green'))
print (colored('Consider wipping or reverting snap of this dirty box!!!', 'green'))
print ()
print (colored('################################################################', 'green'))
print (colored('################################################################', 'green'))
print (colored('################################################################', 'green'))

#####################################
#Cleaning up
####################################
try:
    os.remove ('eicar.com.txt')
except FileNotFoundError:
    print("File is not present in the system.")
try: 
    os.remove('Zombies.pdf')
except FileNotFoundError:
    print("File is not present in the system.")
try:
    os.remove('ip-blacklist.txt')
except FileNotFoundError:
    print("File is not present in the system.")
try:
    os.remove('VXVault.txt')
except FileNotFoundError:
    print("File is not present in the system.")
try:
    os.remove('VXVault_JM.txt')
except FileNotFoundError:
    print("File is not present in the system.")
try:
    os.remove('phish.txt')
except FileNotFoundError:
    print("File is not present in the system.")

print ()
print ('################################################################')
print ('Removing eicar.com.txt')
print ('Removing Zombies.pdf!')
print ('Removing ip-blacklist.txt temp file!')
print ('Removing VXVault.txt temp file!')
print ('Removing VXVault_JM.txt temp file!')
print ('Removing phish.txt temp file!')
print ('Thats it. Check Firepower for events and have fun!')
print ('################################################################')

exit()