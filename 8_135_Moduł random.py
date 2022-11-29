#Moduły random przykład kart


print('----------zadanie nr 1----------')
print('-------------------------------------------------------')

import random

colors = ['Hearts','Diamonds','Clubs','Spades']

figures = ['Ace','King','Queen','Jack','10','9']

allCards = []

player1 = []

player2 = []

i=0

for color in colors:
    for figure in figures:
        allCards.append(color + ' ' +figure)  # - przypisywanie z dwóch liczb do jednej listy

print(allCards)
random.shuffle(allCards)
print(allCards)

max = len(allCards)
print(max)

while i <= (max-1):     # rozdzielanie i przypisywanie wartości listom 
    if (i % 2) == 0:
        player1.append(allCards[i]) 
    else:
        player2.append(allCards[i])
    i+=1
print(player1)
print(player2)

print('----------zadanie nr 2----------')
print('-------------------------------------------------------')

import random

colors = ['Hearts','Diamonds','Clubs','Spades']

figures = ['Ace','King','Queen','Jack','10','9']

allCards = []

player1 = []

player2 = []

i=0

for color in colors:
    for figure in figures:
        allCards.append(color + ' ' +figure)  # - przypisywanie z dwóch liczb do jednej listy

print(allCards)
random.shuffle(allCards)
print('-------------------------------------------------------')
print(allCards)

max = len(allCards)
print(max)

print(int(max/2-1))
print(allCards[0:int(max/2-1)])
print('-------------------------------------------------------')
player1=allCards[0:int(max/2+1)].copy() #- kopiowanie listy z zakresu
print(player1)
print(type(player1))
print(player1)
print('-------------------------------------------------------')
player2=allCards[int(max/2+1):int(max)].copy()
print(player2)
print(len(player2))

print('-------------------------------------------------------')
colors = ['Hearts','Diamonds','Clubs','Spades']
figures = ['Ace','King','Queen','Jack','10','9']
 
allCards = []
for c in colors:
    for f in figures:
        allCards.append("%s - %s" % (c, f))
 
print(allCards)
 
import random
 
random.shuffle(allCards)
print(allCards)
 
player1 = []
player2 = []
 
max = len(allCards)
for i in range(max):
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])
 
print('-------PLAYER 1--------')
print(player1)
 
print('-------PLAYER 2--------')
print(player2)              
 
player1 = allCards[:12]
player2 = allCards[12:]
 
 
print('-------PLAYER 1--------')
print(player1)
 
print('-------PLAYER 2--------')
print(player2)  

'''
#- deklaracja zmiennej 
#- wyświetlenie
#- wyniki
print('----------zadanie nr 1----------')
print('-------------------------------------------------------')
print('----------zadanie nr 2----------')
'''
                               #- 
                               #- 
                               #- 
                               #- 
                               #- 
                               #- 
                               #- 
                               #- 
                               #- 
                               #- 
