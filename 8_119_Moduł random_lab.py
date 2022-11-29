#moduł random
# generowanie wartości losowych
print('----------zadanie nr 1A----------')
import random # import funkcji random

for i in range(0,10):
    print("One random number:",random.randint(1,100)) #funkcja losuje liczbę całkowitą z zakresu 1 <= N <= 100
    print("\n")

counter = 1
number1 = random.randint(1,100)

number2 = random.randint(1,100)
print('próba nr ',counter,'wylosowana liczba',number2)
while number1 >number2 or number1 <number2:
     number2 = random.randint(1,100)
     counter += 1
     print('próba nr ',counter,'wylosowana liczba',number2)

print('Szukana liczba zostałą wylosowana za ',counter,'razem')

#losowanie grup z listy
countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]
random.shuffle(countries) 

groupNumber = 0

print(len(countries))
for i in range(1,len(countries)+1):
    print(i,'grupa',groupNumber, 'państwo ',countries.pop(0))
    if i%4 ==0:
        groupNumber+=1


print('----------zadanie nr 1B----------')
import random
 
for i in range(10):
    print(random.randint(1,100))
    
print('----------')
 
number1 = random.randint(1,100)
print("The first generated number is %d" %(number1))
 
counter = 1
number2 = random.randint(1,100)
 
while number1 != number2:
    counter+=1
    number2=random.randint(1,100)
    print(counter, number2)
    
print("I needed %d attempts to generate %d again" % (counter, number1))
 
print('----------')
 
countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]
 
random.shuffle(countries)
 
groupNumber = 0
 
for i in range(len(countries)):
    if i % 4 == 0:
        groupNumber += 1
        print("========== Group %d ==========" % (groupNumber))
    print(countries[i])






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
