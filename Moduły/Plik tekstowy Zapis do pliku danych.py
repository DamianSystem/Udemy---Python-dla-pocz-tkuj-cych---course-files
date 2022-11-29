# moduł zapis do pliku .txt
# wyspecjalizowane formaty plików będą obsługiwane przez odpowiednie moduły

filename = 'c:\\temp\\output.txt'

line = 'Europe'

cities = ['London','Berlin','Paris','Warsaw','Madrid','Rome']

#file = open(filename, 'w') # otwieramy plik (open), daje ścieżkę pliku (filename) i precyzuje sposób zapisu('w') - plik jest czyszczony z danych

#file = open(filename, 'w+') # otwieramy plik (open), daje ścieżkę pliku (filename) i precyzuje sposób zapisu('w+') - plik jest czyszczony z danych, zapisywane są nowe dane i można odczytać plik

#file = open(filename, 'a') # otwieramy plik (open), daje ścieżkę pliku (filename) i precyzuje sposób zapisu('a') - plik jest aktualizowany danymi

file = open(filename, 'a+') # otwieramy plik (open), daje ścieżkę pliku (filename) i precyzuje sposób zapisu('a') - plik jest aktualizowany danymi i można odczytać plik


file.write(line) # file.write - polecenie do zapisywania informacji (line) do pliku (tu filename)
file.write("\n")
#file.writelines(cities) # dopisywanie całej linijki danych

for city in cities:
    file.write(city+'\n') # sposób na dopisywanie linijek osobnych z nazwami miast


file.close() # zamykanie otwatego pliku





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
