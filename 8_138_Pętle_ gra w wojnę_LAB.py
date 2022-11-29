#Pętle_gra w wojnę


'''
#przypomnienie oo słowniku
aCard = {"Figure":"King", "Power":12} # słownik
print(aCard)
print(aCard['Figure']) 
print(aCard['Power'])

aCard['Color'] = 'Heart'# dodanie nowej wartości do słownika
print(aCard['Color'])
print(aCard)
'''

import random

colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]


allCards = []
aCard = {}

player1 = []
player2 = []



#print(len(figures))
#print(type(figures))
#print(type(figures[0]))
for color in colors:
    #print(color)
    i = 0
    while i < len(figures):
        aCard.update(figures[i])
        aCard['color'] = color 
        allCards.append(aCard)
        #print(aCard)
        aCard = {}
        i+=1

#print(allCards)
random.shuffle(allCards)
#print(allCards)

max = len(allCards)
print(max)
i=0
while i <= (max-1):     # rozdzielanie i przypisywanie wartości listom 
    if (i % 2) == 0:
        player1.append(allCards[i]) 
    else:
        player2.append(allCards[i])
    i+=1
print(player1)
print(len(player1))
print(player2)
print(len(player2))
i=0
brake=0
while (len(player1) > 0) and (len(player1) > 0) and brake<5:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    #print(card1)
    #print(card2)
    #print(card1['Power'], card2['Power'])
    
    if card1['Power'] > card2['Power']:
        player1.append(card1)
        brake = 0
        print('PLAY-1  \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player2)*'*')
    elif card1['Power'] < card2['Power']:
        player2.append(card2)
        brake = 0
        print('PLAY-2  \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
    else:
        player1.append(card1)
        player2.append(card2)
        print('=EQUAL  \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
        brake+=1

print(len(player1))
print(len(player2))
if len(player1)>len(player2):
    print('win player 1')
elif len(player1)<len(player2):
    print('win player 2')
else:
    print('draw')

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
