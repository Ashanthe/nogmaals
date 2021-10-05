# name of student: Ashanthe
# number of student: 99069097 
# purpose of program: Giving back the right amount of change money, while using a specific type of money
# function of program: Calculating your change and showing wich kind of coins it's using for it.
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) # Vraagt hoeveel je moet betalen
paid = int(float(input('Paid amount: ')) * 100) # Laat zien hoeveel je hebt betaald
change = paid - toPay # Verandert de variabele naar change. Hoeveel je hebt betaald min de hoeveelheid die je moet betalen



if change > 0: # Wanneeer change groter is dan 0 dan is de coinvalue:
  coinValue = 500 # Bepaald coinValue
  
  while change > 0 and coinValue > 0: # Terwijl de change groter is dan 0 en de coinvalue is groter dan 0 dan doet hij het volgende totdat het niet meer zo is. 
    nrCoins = change // coinValue # Deze functie deelt twee getallen en rond de getallen achter de komma af naar beneden.

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #

# comment on code below: Deze if statement word uitgevoerd totdat hij op nul springt, zit in de "while" lus 
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinvalue = 5
    elif coinvalue == 5:
      coinvalue = 2
    elif coinvalue == 2:
      coinvalue = 1
    else:
      coinValue = 0

if change > 0: # Als de change groter is dan 0
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')