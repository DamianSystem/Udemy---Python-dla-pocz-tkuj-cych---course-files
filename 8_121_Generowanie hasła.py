#generowanie hasła

# Tabela ASCI (przypisanie numerycznej wartości literkom z klawiatury (256 znaków)

print('Wyświetlenie Tabeli ASCI')
print('-------------------------------------------------------')

for i in range (32,127): #(32,127) klawisze z poza zakresu mogą mieć symbol np. delete lub strałki
    print(i,chr(i))


# budowanie hasła

import random

ints = range (33,127)# pomijamy spacje na 32 pozycji i do znaku ~(tyldy) na 126 pozycji - tworzymy tabele
password =''

for ir in range(16): # hasło będzie miało 16 znaków
    password += chr(random.choice(ints))

print("Password is:",password)






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
