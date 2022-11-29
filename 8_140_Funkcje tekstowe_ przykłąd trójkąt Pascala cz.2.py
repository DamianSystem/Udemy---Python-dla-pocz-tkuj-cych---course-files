#Pętle_ przykład trójkąt Pascala cz.2
width = 60
height = 7 
numbers = [1]

line = ''
for n in numbers:
     line+="%3d " % (n)
     
print(line.center(width)) # linia ma być wycentrowana na 50 znakach

for i in range (height-1): # tworzymy ilość lini w trójkącie

    newNumbers = [1]

    position = 0

    while position< len(numbers) -1: # ograniczenie w ilości dodawanych elementów w lini
        newNumbers.append(numbers[position] + numbers[position +1]) # zabespieczenie aby nie wyjść poza zakres linijka wyżej w zakresie pętli
        position+=1

    newNumbers.append(1)

    numbers = newNumbers.copy()

    line = ''
    for n in numbers:
         line+="%3d " % (n)
         
    print(line.center(width))




    
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
