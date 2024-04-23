import sys
import os
#from metasploit.msfrpc import MsfRpcClient
#from metasploit.msfconsole import MsfRpcConsole

#os.system('ping 192.168.154.128')
#os.system('nmap -p 10-100 192.168.154.128')
os.system('msfconsole')
os.system('nmap 192.168.154.128 -A')
#print(p)