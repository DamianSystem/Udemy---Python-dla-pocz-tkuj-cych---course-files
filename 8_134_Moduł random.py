#Moduły random przykład kart

import random

myNumbers = [] #- będzie przechowywać wyloosowane numery

while len(myNumbers) < 7: # myNumbers ma być losowane do 7 elementów ( losowanie ilości elemntów

    newNumber = random.randint(1,49)


    if newNumber in myNumbers:
        print ("Eliminated: ",newNumber) # eliminacja elementów powtarzających się
        continue
    
    myNumbers.append(newNumber)

print("Those number will win:", myNumbers)





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
