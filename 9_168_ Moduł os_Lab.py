# moduł os Lab - śceżka do pliku

import os
import time



dir = input('Please enter the path to the file: ')

print("Is it a dir? ", os.path.isdir(dir))

if not os.path.isdir(dir):
    print ('niepoprawny adres folderu')
else:
    print ('poprawny adres folderu')
    file = input('\nWhat is the file name? ')
    path =  os.path.join(dir, file)
    print(path)
    if os.path.exists (path):
        print('displaying properties of file %s' % path)
        print("Last modify date is: ",time.localtime(os.path.getmtime(path)))
        print("\nFile size is: ",os.path.getsize(path),' Byte')
        print("The directory part is: ", os.path.dirname(path))
        print("Current directory is: ", os.getcwd())
        print ("\nThe absolute path is: ",os.path.abspath(path))
        print('Relative path to the file is', os.path.relpath(path)) # ścieżka względna do pliku
    else:
        print('The file %s is not exist' %path)
        
 print('-------------------------------------------------------')  
 # to samo co wyżej tylko pisane przez autora kursu  

import os
import time
 
dir = input('enter directory name: ')
 
if not os.path.isdir(dir):
    print("%s must be a directory" % dir)
else:
 
    file = input('enter filename saved in directory %s: ' % dir)
 
    path = os.path.join(dir, file)
 
    if not os.path.isfile(path):
        print('File %s does not exist!' % path)
 
    else:
    
        print('displaying properties of file %s' % path)
 
        print('Last modified date', time.localtime(os.path.getmtime(path)))
        print('Size in bytes', os.path.getsize(path))
 
        print('Current directory is: ', os.getcwd())
        print('Relative path to the file is', os.path.relpath(path))



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
