#Pętle_gra w wojnę wersja poprawiona


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
'''
i=0
 
while i < 10:
    print(i)
    #if i == 3:
    #    break
    i+=1
else:
    print('else')
 
print('end')
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
stock = []
break_0 = 0
while (len(player1) > 0) and (len(player2) > 0) and break_0 <= (len(allCards)/2+1):
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    
    #print(card1)
    #print(card2)
    #print(card1['Power'], card2['Power'])
    
    if card1['Power'] > card2['Power']:
        player1.extend(stock)
        player1.append(card1)
        player1.append(card2)
        stock = []
        print('PLAY-1  \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player2)*'*')
        
    elif card1['Power'] < card2['Power']:
        player2.extend(stock)
        player2.append(card1)
        player2.append(card2)
        stock = []
        print('PLAY-2  \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
        
    else:
        while card1['Power'] == card2['Power']:
            print('=EQUAL  \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
            stock.append(card1)
            stock.append(card2)
            if len(player1)<2:
                player2.extend(stock)
                print(player1)
                player2.append(player1.pop(0))
                print('zawarosc player1:',player1)
                player1 = []
                print('PLAY-2  \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player2)*'*')
                break
            elif len(player2)<2:
                player1.extend(stock)
                print(player2)
                player1.append(player2.pop(0))
                print('zawarosc player2:',player2)
                player2 = []
                print('PLAY-1  \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
                break
            elif len(player1)>=2 and len(player2)>=2:
                card1 = player1.pop(0)
                card2 = player2.pop(0)
                print('=EQUAL_2  \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
                stock.append(card1)
                stock.append(card2)
                card1 = player1[0]
                card2 = player2[0]


print(len(player1))
print(len(player2))
if len(player1)>len(player2):
    print('win player 1')
elif len(player1)<len(player2):
    print('win player 2')

 print('-------------------------------------------------------')  
 # to samo co wyżej tylko pisane przez autora kursu  

colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]
 
allCards = []
for c in colors:
    for f in figures:
        aCard = f.copy()
        aCard['Color'] = c
        allCards.append(aCard)
 
import random
 
random.shuffle(allCards)
print(allCards)
 
player1 = []
player2 = []
 
player1 = allCards[:12]
player2 = allCards[12:]
 
 
print('-------PLAYER 1--------')
print(player1)
 
print('-------PLAYER 1--------')
print(player2)    
 
while len(player1) > 0 and len(player2) > 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
 
    stack = []  
 
    if card1["Power"] == card2["Power"]:
        while card1["Power"] == card2["Power"]:
 
            print('WAR',card1['Power'],card2['Power'])
            stack.append(card1)
            stack.append(card2)
 
            if len(player1)<2:
                player2.extend(stack)    
                player2.extend(player1)
                player1 = []
                print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player2)*'*')
                break
            elif len(player2)<2:
                player1.extend(stack)    
                player1.extend(player2)
                player2 = []
                print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
                break
            else:
                card1 = player1.pop(0)
                card2 = player2.pop(0)
                stack.append(card1)
                stack.append(card2)
                card1 = player1.pop(0)
                card2 = player2.pop(0)
        else:
            if card1["Power"] > card2["Power"]:
                stack.append(card1)
                stack.append(card2)
                player1.extend(stack)
                print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
            else:
                stack.append(card1)
                stack.append(card2)
                player2.extend(stack)
                print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player2)*'*')
            
 
    elif card1["Power"] > card2["Power"]:
        player1.append(card1)
        player1.append(card2)
        #print('PLAY-1 \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
    else:
        player2.append(card2)
        player2.append(card1)
        #print('PLAY-2 \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player2)*'*')
 
if len(player1) > 0:
    print('PLAYER 1 WON!!!!')
else:
    print('PLAYER 2 WON!!!!')

'''
#- deklaracja zmiennej 
#- wyświetlenie
#- wyniki
print('----------zadanie nr 1----------')
print('-------------------------------------------------------')
print('----------zadanie nr 2----------')

 print('-------------------------------------------------------')  
 # to samo co wyżej tylko pisane przez autora kursu  

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
