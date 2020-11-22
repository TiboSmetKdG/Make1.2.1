# !/usr/bin/env python

"""
            ／￣￣￣￣￣￣￣￣
　　　　　　  |　Een python script dat het volgende doet:
　　　　　　  |　1. vraagt achter je leeftijd
　　　　　　  |　2. berekent in welk jaar je geboren bent en dat ook als output meegeeft
　　　　　　  |　3. berekent in welk jaar je 50 jaar zal zijn en dat ook als output meegeeft
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
import datetime

# CONFIG
huidigJaar = datetime.datetime.now().year

# AUTHOR INFORMATION
__author__ = "Tibo Smet"
__email__ = "tibo.smet@student.kdg.be"
__status__ = "Development"


print('Geef je leeftijd in:')
leeftijd = int(input())

geboortejaar = huidigJaar - leeftijd

jaar50 = geboortejaar + 50

print('Je bent geboren in ' + str(geboortejaar))
print('Je zal 50 zijn in ' + str(jaar50))
