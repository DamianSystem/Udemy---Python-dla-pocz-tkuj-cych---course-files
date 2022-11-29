#generowanie hasła

print('----------zadanie nr 1A----------')

print('-------------------------------------------------------')
# rzut kostką
import random

min = 1
max = 6

dice = random.randint(min,max)
if dice == 1:
    print('   \n o \n   ')
elif dice == 2:
    print('  o  \n     \no')
elif dice == 3:
    print('  o  \n o\no')
elif dice == 4:
    print('o o  \n \no o')
elif dice == 5:
    print('o o  \n o\no o')
elif dice == 6:
    print('o o  \no o\no o')


print('----------zadanie nr 1B----------')

print('-------------------------------------------------------')

import random
 
min = 1
max = 6
 
dice = random.randint(min,max)
 
if dice == 1:
    print('   ')
    print(' o ')
    print('   ')
elif dice == 2:
    print('  o')
    print('   ')
    print('o  ')
elif dice == 3:
    print('  o')
    print(' o ')
    print('o  ')
elif dice == 4:
    print('o o')
    print('   ')
    print('o o')
elif dice == 5:
    print('o o')
    print(' o ')
    print('o o')
else:
    print('o o')
    print('o o')
    print('o o')


print('----------zadanie nr 2----------')

print('-------------------------------------------------------')
# rzut 5 kostkami


import random

min = 1
max = 6
dices=[]
for i in range(1,6):
    dices.append(random.randint(min,max))
print(dices)
dices.sort()
print(dices)


for item in dices:
    if item == 1:
        print('   \n o \n   ')
    elif item == 2:
        print('  o  \n     \no')
    elif item == 3:
        print('  o  \n o\no')
    elif item == 4:
        print('o o  \n \no o')
    elif item == 5:
        print('o o  \n o\no o')
    else: #item == 6
        print('o o  \no o\no o')






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
