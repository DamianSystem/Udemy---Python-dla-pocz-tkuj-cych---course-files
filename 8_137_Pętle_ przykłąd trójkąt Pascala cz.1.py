#Pętle_ przykład trójkąt Pascala cz.1

numbers = [1]

print(numbers)

for i in range (5): # tworzymy ilość lini w trójkącie

    newNumbers = [1]

    position = 0

    while position< len(numbers) -1: # ograniczenie w ilości dodawanych elementów w lini
        newNumbers.append(numbers[position] + numbers[position +1]) # zabespieczenie aby nie wyjść poza zakres linijka wyżej w zakresie pętli
        position+=1

    newNumbers.append(1)

    numbers = newNumbers.copy()

    print(numbers)


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
