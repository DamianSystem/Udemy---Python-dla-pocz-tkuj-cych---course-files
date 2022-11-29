# moduł Błędy w Python

import os
import sys
#Uwaga ułożenie danych i obliczeń w jednym miejscu
input_user = input('Acceptable price of a new course idemy. Your price? ')
filepath = input('Wprowadż ścieżkę do pliku: ')
try:
    line = input_user
    value = int(line)
    file = open(filepath, 'w')
    file.write(line)
    file.close()
    print('The value saved in file is',value)
except FileNotFoundError as e:
    print("Error opening file in %s "% filepath, e)
except ValueError as e:
    print("The value entered cannot be converted to a number.",line, e)
except :
    print("SORRY - WE HAVE AN ERROR",sys.exc_info())
else:
    print("Actions completed successfully")

print('-------------------------------------------------------')  
# to samo co wyżej tylko pisane przez autora kursu

line = input('Enter accepted price: ')
filepath =input('Enter filename : ')
 
try:
    file = open(filepath,'w+')
    file.write(line)
    file.close()
    value = int(line)
    print('The value saved in file is',value)
except FileNotFoundError as e:
    print('Error opening file',filepath,e)
except ValueError as e:
    print('The value entered cannot be converted to a number',line,e)
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')
else:
    print('Actions completed successfully')

    
'''
#- deklaracja zmiennej 
#- wyświetlenie
#- wyniki
print('----------zadanie nr 1----------')
print('------------------------------------------')
print('----------zadanie nr 2----------')

print('-------------------------------------------------------')
print('to samo co wyżej jest wykonywane innym sposobem')

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
