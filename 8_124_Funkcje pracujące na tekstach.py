#Funkcje pracy na tekscie

line = 'this IS a very STRANGE text'
line.capitalize() #- konwertowanie tekstu na zdanie zaczynające się dużą literą z pozostałymi młymi literami ('This is avery strange text')
line.title() #- (tytuł) każde słowo rozpoczyna się z wielkiej litery ('This Is Avery Strange Text')
line.upper() #- konertowanie tekstu do dużych liter ('THIS IS AVERY STRANGE TEXT')
line.lower() #- konertowanie tekstu do małych liter ('this is avery strange text')
line.swapcase() #- zamiana dużych na małe litery i odwrotnie - małe na duże litery('THIS is AVERY strange TEXT')
line.casefold() #- zamienia np. w języku niemieckim 'ß' na 'ss' i zmienia tekst na male litery

line = 'der Fluß'
line.lower()
line.casefold()

line = 'ŻÓŁĆ'
line.lower()
line.casefold()
line.replace('Ż','Z').replace('Ó','O').replace('Ł','L').replace('Ć','C').lower() #- line.replace('Ż','Z') zamiana litery 'Ż' na 'Ż' w wartości zmiennej line

line = 'this IS a very STRANGE text'
line.count('e') #- policzenie ilości wystąpień litrki 'e' w tekście
line.find('e') #- sprawdzenie pozycji litery 'e' od lewej strony domyślnie
line.rfind('e') #- sprawdzenie pozycji litery 'e' od prawej strony
line.index('e') #- sprawdzenie pozycji litery 'e' od lewej strony domyślnie
line.rindex('e') #- sprawdzenie pozycji litery 'e' od prawej strony

line.find('p') #- gdy brak literki p w szykanym tekscie funkcja zwraca '-1'
line.index('p') #- gdy brak literki p w szykanym tekscie funkcja zwraca błąd

# tworzenie wyrażenia logicznego
'e' in line # zwróci wartość True gdy wystąpi litera
'p' in line # zwróci wartość False gdy nie wystąpi litera
----------------------------dokończyć notepad++
line.startswith('this') #- sprawdzenie czy ciąg znaków zaczyna się okkreślonym ciągiem znaków, czułość na wielkość liter. (wartości wynikowe true i false)
line.startswith('This')
line.endswith('text') #- sprawdzenie czy ciąg znaków kończy się okkreślonym ciągiem znaków, czułość na wielkość liter. (wartości wynikowe true i false)

line = """this is a long text
tha spans multiple lines
but should be somehow presented in python""" #- zamknięcie długiego tekstu w potrójnym cudzysłowiu (""")
line # - wyświetlenie tekstu w konsoli pokazuje enter jako \n
line.count('\n') #- rozpoznaje nam w napisie


#dodatkoy moduł

import string
string.ascii_letters    #- stała która wyświetla duże i małe litery
string.digits           #- stała która wyświetla cyfry od 0 - 9


line = 'this is the end of this lesson'
line.split(' ') #- funkcja .split(' ') rozbije napis na liste ze względu na spację.
list = line.split(' ') #- zapamiętanie wyniku w innej zmiennej
list
' '.join(list) # - połączenie listy za pomocą spacji w ciąg znaków


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
