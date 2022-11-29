# moduł odczyt z plliku

file = open("c:\\temp\\joke.txt","r")  # open(path, mode) - otwórz plik(ścieżka do pliku, r - read odczytaj
                                       # uwaga po otwarciu pliku trzeba go zamknąć


content = file.read()                  # .read() odczytanie zawartości całego pliku
print(content)                         # wyświetlenie zawartości pliku

file.close                             # zamykanie pliku

print('-------------------------------------------------------')
print('to samo co wyżej jest wykonywane innym sposobem')

with open("c:\\temp\\joke.txt","r") as file: # otwarcie pliku tylko w ramach polecenia with od razu plik jest zamkany( nie nadaje się do dużych plików ze względu na wydajność
    content = file.read() 
    print(content)

print('-------------------------------------------------------')
with open("c:\\temp\\joke.txt","r") as file:
    for line in file: # wczytywnie linijka po linijce pliku z powyższym otwarciem liku(bardzo duża wydajność) - nie trzymanie w pamięci komputera
        print(line)
print('-------------------------------------------------------')
print('to samo co wyżej jest wykonywane innym sposobem')
file = open("c:\\temp\\joke.txt","r") # musimy pamięać o zamknięcu pliku
for line in file:
    print(line)
file.close 

print('-------------------------------------------------------')
print('to samo co wyżej jest wykonywane innym sposobem')
file = open("c:\\temp\\joke.txt","r")
for line in file.readlines(): # odczytuje cały plik i ładuje go do pamięci (obciąża mocno system)
    print(line)
file.close 

print('-------------------------------------------------------')
print('to samo co wyżej jest wykonywane innym sposobem')
file = open("c:\\temp\\joke.txt","r")
fragment = file.read(10) # odczytanie 10 bajtów
file.close 
while fragment: # pętla z odczytywaniem po 10 bajtów pliku doputy nie zostanie on pusty, wtedy pętla się zakończy
    print(file.tell(), fragment) # wskaźnik gdzie python się znajduje (numerowanie)
    fragment = file.read(10)

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
