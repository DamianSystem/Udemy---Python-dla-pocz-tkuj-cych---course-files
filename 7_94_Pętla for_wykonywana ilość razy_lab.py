#pętla for wykonywana ilość razy

print('----------zadanie nr 1----------')
string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for number in range(1,11):
    print('%2d | %s'  % (number, string_A))

print('----------zadanie nr 2----------')
    
for number in range (1,10): 
    if number %2 ==0:  
         print('%2d | %s'  % (number, string_A)) 
    else:
         print('%2d | %s'  % (number, string_B))
         
print('----------zadanie nr 3----------')
    
for number in range (1,10): 
    print('%2d | %s'  % (number, 'x'*number)) 
    
print('----------zadanie nr 4----------')
    
for number in range (1,10): 
    if number %2 ==0:  
         print('%2d | %s'  % (number, 'x'*number)) 
    else:
         print('%2d | %s'  % (number, 'o'*number))   
   


'''
a=range(20)
print(type(a))

for number in range (20): # wygenerowanie liczb od0-19 range(20), liczenie Python
    print(number)

for number in range (1,21): # wygenerowanie liczb od1-20 range(1,21) liczenie Python
    print(number)

for number in range (1,21,2): # pierwszy parametr (1, Python liczenie)mówi od jakiej wartości zaczynamy liczyć
        # drugi parametr (,21, Python liczenie) do jakiej wartości liczymy, trzeci parametr (,2 Python liczenie) co ile liczymy
    print(number) # zakres liczb nieparzystych od 1 do 20

for number in range (0,21,2): # pierwszy parametr (1, Python liczenie)mówi od jakiej wartości zaczynamy liczyć
        # drugi parametr (,21, Python liczenie) do jakiej wartości liczymy, trzeci parametr (,2 Python liczenie) co ile liczymy
    print(number) # zakres liczb parzystych od 0 do 20

for number in range (1,21): # wygenerowanie liczb od1-20 range(1,21) liczenie Python
    if number %2 ==0: # jeżeli reszta z dzielenia przez(modulo) 2 jest równa zero 
        print('number %2d is %s' % (number,'even')) # even (parzysty)- numer jest pażysty
    else:
        print('number %2d is %s' % (number,'odd')) # odd (nieparzysty)- numer jest niepażysty
   ''' 
'''
#- deklaracja zmiennej 
#- wyświetlenie
#- wyniki
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
