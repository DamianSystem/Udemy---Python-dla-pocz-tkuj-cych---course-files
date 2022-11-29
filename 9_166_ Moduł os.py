# moduł os - śceżka do pliku

import os # moduł os paw który pozwala na wykonywanie pewnych czynności ze ścieżkami dostępu do pliku
import time


print("Current directory is: ", os.getcwd())    # os.getcwd - funkcja zwrca informacje o bierzącym katalogu

currentDir = os.getcwd()                        #zapis wyników ścieżki dostępu do pliku
filename = 'results.txt'                        # wymyślona nazwa pliku
fullpath = os.path.join(currentDir,filename)    # os.path.join - połączenie ścieżki z nazwą pliku
print("\nThe constructed file path is: ",fullpath)
                                                                 # względna ścieżka położenia pliku jest względem np. katalogu
relativePath = 'output.txt'
print ("\nThe absolute path is: ",os.path.abspath(relativePath)) #* ścieżka bezwzględna ścieżka położenie pliku 
                                                                #*  ścieżka bezwzględna nazwa dysku , folderów i nazwa plików
filepath = r'c:\temp\result.txt'                                # pisanie ścieżki jaka jest (na surowo) komputer sam praetłumaczy ją sobie na język maszynowy
print("\nThe file name part is: ", os.path.basename(filepath)) # os.path.basename(filepath) - wyodrębnienie części nazwy odpowiadającej za nazwę pliku
print("The directory part is: ", os.path.dirname(filepath))     # os.path.dirname(filepath) - wyodrębnienie części nazwy odpowiadającej za ścieżkę dostępu do katalogu gdzie znajduje się plik

print("\nIs file existing? ",os.path.exists(filepath)) # parametr spradza czy dany plik istnieje

if os.path.exists (filepath):           # mając istniejący plik możemy z niego wydobyć oniższe informację
    print("\nLast modify date is: ",os.path.getmtime(filepath))  # os.path.getmtime(filepath) - zapytanie o datę modyfikacji pliku ( zwraca wartość w sekundach od 2017 roku)
                                                                 # os.path.getctime(filepath) - zapytanie o datę utworzenia pliku
                                                                 # os.path.getatime(filepath) - zapytanie o datę ostatniego dostępu
    print("Last modify date is: ",time.localtime(os.path.getmtime(filepath))) # zwrca czas w bardziej przyjazny sposób

    print("\nFile size is: ",os.path.getsize(filepath)) # zwraca rozmiar pliku w bajtach

    print("\nIs it a file? ", os.path.isfile(filepath)) # sprawdza czy dana ścieżka jest do pliku
    print("Is it a dir? ", os.path.isdir(filepath))     # sprawdza czy dana ścieżka jest do folderu

    print("\nPath splitted:", os.path.split(filepath)) # odrywa ostatni fragment ścieżki pliku lub katalogu
    print("Only file name part: ", os.path.split(filepath)[1]) # odwołanie do pierwszej wartości zwracanego obiektu tapple
    
    print("\nPath splitted into driver: ",os.path.splitdrive(filepath)) # analizuje i zwraca elementy: nszwę dysku i ścieżkę dostępu do pliku
    print("Only drive:",os.path.splitdrive(filepath)[0]) # możliwość oderwania samej nazwy dysku ze ścieżki do pliku







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
