

previousNumber = 0
number = 1
max_number = 50

while number<=max_number:
    
    print(number,' ',previousNumber,'+',number,' ',previousNumber+number) 


    previousNumber=number
    number+=1

#- gra w zgadywanie liczb

import random # import modułu random
my_number = random.randint(0,20) # przypisanie wartości za pomocą modułu random w zakresie od 0-20
guess = -1 # wartość z poza zakresu losowania
trials = 0


#print(my_number)
print("Guess my number!",sep="\n")
while  my_number != guess:
    trials+=1
    guess= int(input()) # wczytanie odpowiedzi użytkownika
    if my_number == guess:
        print("Gratulation my number is",my_number,"You needed",trials," trials")
    elif my_number < guess:
        print("Sorry- my number is smaller than your guess, Try again!")
    else:
        print("Sorry- my number is greater than your guess, Try again!")
   





'''
#- deklaracja zmiennej 
#- wyświetlenie
#- wyniki
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
