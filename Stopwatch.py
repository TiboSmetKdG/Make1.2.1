# !/usr/bin/env python

"""
            ／￣￣￣￣￣￣￣￣
　　　　　　  |　Een python script dat de functie van een stopwatch heeft.
　　　　　　  |　Gebruik hiervoor de functie 'time'.
　　　　　　  ＼＿＿　＿＿＿＿＿＿＿
　　　　　　　　　  ∨
            ██████████  ████
        ████▒▒░░░░░░░░██▒▒░░██
      ██▒▒░░░░██░░██░░░░██░░░░██
    ██▒▒░░░░░░██░░██░░░░░░▒▒░░██
    ██░░░░░░░░██░░██░░░░░░▒▒▒▒██
  ██░░░░░░▒▒▒▒░░░░░░▒▒▒▒░░░░▒▒██
██▒▒░░░░░░░░░░░░██░░░░░░░░░░░░██
██░░░░▒▒░░░░░░░░██░░░░░░░░░░▒▒██
██░░░░▒▒░░░░░░░░░░░░░░░░░░░░██
  ██████░░░░░░░░░░░░░░░░░░▒▒██
██▒▒▒▒▒▒██░░░░░░░░░░░░░░░░▒▒██
██▒▒▒▒▒▒▒▒██░░░░░░░░░░░░▒▒██
██▒▒▒▒▒▒▒▒██░░░░░░░░░░▒▒████
  ██▒▒▒▒▒▒▒▒██▒▒▒▒▒▒████▒▒▒▒██
    ██▒▒▒▒██████████▒▒▒▒▒▒▒▒▒▒██
      ██████      ████████████
"""

# IMPORTS
import time

# CONFIG
vorige_seconde = 0

# AUTHOR INFORMATION
__author__ = "Tibo Smet"
__email__ = "tibo.smet@student.kdg.be"
__status__ = "Development"

print("geef het te timen aantal seconden in")
duur = input()
start_tijd = time.time()
eind_tijd = int(start_tijd) + int(duur)

while True:
    while time.time() < eind_tijd:
        seconde = round(time.time() - start_tijd)
        if vorige_seconde < seconde:
            print(seconde)
            vorige_seconde == seconde
        pass
