# moduł . Kontrola ścieżki do plliku
# sprawdzenie czy plik jest w danej ścieżce

import os

fileIsOk = False # potrzebne do sprawdzenia czy dany plik istnieje


while not fileIsOk:
    filename = input('Enter path to results file: ') # będziemy chcieli ay użytkownik wprowadził nazwę już istniejącegoo pliku

    if os.path.isfile(filename): # sprawdzenie czy dany plik istnieje
        fileIsOk = True
    else:
        print('File name is not correct, try again!')
        
print("The results file is %s" % (filename))


print('------------------------------------------')
print('----------inna opcja tego samego rozwiązania----------')
import os

while True:
    filename = input('Enter path to results file: ') # będziemy chcieli ay użytkownik wprowadził nazwę już istniejącegoo pliku

    if os.path.isfile(filename): # sprawdzenie czy dany plik istnieje
        break
    else:
        print('File name is not correct, try again!')
        
print("The results file is %s" % (filename))

'''
#- deklaracja zmiennej 
#- wyświetlenie
#- wyniki
print('----------zadanie nr 1----------')
print('------------------------------------------')
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
