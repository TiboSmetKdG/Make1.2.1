# !/usr/bin/env python

"""
            ／￣￣￣￣￣￣￣￣
　　　　　　  |　Maak een python rekenmachine script dat het volgende omvat:
　　　　　　  |　1. Een zelf gemaakte python header
　　　　　　  |　2. het script vraagt de gebruiker om 2 natuurlijke getallen in te geven
　　　　　　  |　3. Deze 2 natuurlijke getallen vermeerderen, verminderen, vermenigvuldigen of delen
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


# CONFIG


# AUTHOR INFORMATION
__author__ = "Tibo Smet"
__email__ = "tibo.smet@student.kdg.be"
__status__ = "Development"


print('Geef een eerste getal op:')                          # Vraagt het eerste getal voor de bewerking
getal1 = int(input())                                       # Geeft variabele getal1 de waarde van de input
print('Geef een tweede getal op:')                          # Vraagt het tweede getal voor de bewerking
getal2 = int(input())                                       # Geeft variabele getal2 de waarde van de input

som = getal1 + getal2                                       # Berekent de som van getal1 en getal2
verschil = getal1 - getal2                                  # Berekent het verschil van getal1 en getal2
product = getal1 * getal2                                   # Berekent het product van getal1 en getal2
quotient = getal1 / getal2                                  # Berekent het quotient van getal1 en getal2

print('Som van de 2 getallen: ' + str(som))                 # Geeft de som weer in de console
print('Verschil van de 2 getallen: ' + str(verschil))       # Geeft het verschil weer in de console
print('Product van de 2 getallen: ' + str(product))         # Geeft het product weer in de console
print('Quotient van de 2 getallen: ' + str(quotient))       # Geeft het quotient weer in de console
