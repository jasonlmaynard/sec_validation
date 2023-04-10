
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

varRISK = input ('You accept all responsibilty when using this script yes|no: ')
if varRISK == 'yes':
    print ('Continuing at your own risk')
else:
    exit()

def func_NMAP():
    print ('######################################################')
    print ('Please note: NMAP requires elevated privledges - sudo')
    print ('######################################################')
    varNMAP = input ('Do you want to test Port Scanning? yes|no: ')
    if varNMAP == 'yes':
        print ('NMAP continuing at your own risk')
        return exec(open('nmap_scan.py').read())
    elif varNMAP == 'no': 
        print ('Skipping NMAP Scanning') 
        
def func_BAD():
    print ('######################################################')
    print ('ISOLATE THE INSTANCE THIS IS REAL TESTING!')
    print ('######################################################')
    varBAD = input ('Do you want to test real world threats? yes|no: ')
    if varBAD == 'yes':
        print ('Bad could happen continuing at your own risk')
        return exec(open('bad_stuff.py').read())
    elif varBAD == 'no': 
        print ('Skipping BAD Stuff but why else are you here?') 

# Determine Operation System 
from sys import platform
if platform == "linux" or platform == "linux2":
    # linux
    print ('###############################################')
    print ('Linux Operating System Detected')
    print ()
    print ('###############################################')
    print ('Running the malicous connections in Linux')
    print ()
    print ('###############################################')
    func_NMAP()
    func_BAD()
    
elif platform == "darwin":
    # OS X
    print ('###############################################')
    print ('OSX Operating System Detected')
    print () 
    print ('###############################################')
    print ('Running the malicous connections in OSX')
    print ('###############################################')
    func_NMAP()
    func_BAD()
        
elif platform == "win32" or platform == "win64":
    # Windows 
    print ('###############################################')
    print ('Windows Operating System Detected')
    print ()
    print ('###############################################')
    print ('Running the malicous connections in Windows')
    print ('###############################################')
    func_NMAP()
    func_BAD()
        
else:
    print ('Foreign Operating System')
