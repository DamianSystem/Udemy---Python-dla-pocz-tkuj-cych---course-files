# moduł zapis do pliku .txt Lab

print('----------zadanie nr 1A----------')
# zapis do dowolnie nazwanego pliku pliku (bez podanego rozszerzenia) adresów www

import os

webaddresses = []

line = input('Wprowadź adres strony www, enter kończy wprowadzanie danych:  ')

#print (line)
#print(type(line))
while line:             # dopisywanie do listy stron www
    webaddresses.append(line)
    line = input('Wprowadź adres strony www, enter kończy wprowadzanie danych: ')

print(webaddresses)
dirname = os.getcwd()
filename = input('Wprowadż nazwę pliku: ')
filepath = os.path.join(dirname,filename)

print(filepath)
 
file = open(filepath, 'w+')
print(file)
for webaddresse in webaddresses:
    file.write(webaddresse + '\n') # zapisywanie osobno linijek adresu www w osobnych wierszach

file.close() # zamykanie otwatego pliku

print('------------------------------------------')
print('----------zadanie nr 1B----------')

import os
  
webaddresses=[]
line = input('Enter web address like "www.python.org" or press ENTER to stop: ')
while line != '':
    webaddresses.append(line)
    line = input('Enter web address like "www.python.org" or press ENTER to stop: ')
    
print(webaddresses)
dirname = os.getcwd()
filename = input("Enter the file name (without directory): ")
filepath = os.path.join(dirname,filename)
file = open(filepath,'w+')
for webaddress in webaddresses:
    file.write(webaddress+"\n")
file.close()

print('------------------------------------------')
print('----------zadanie nr 2A----------')
# odczyt pliku, sprawdzanie czy dany plik istnieje, wyświetlanie adresów www z polski i nie z polski
import os

while True:
#    filepath = input('Enter path to results file: ') # będziemy chcieli ay użytkownik wprowadził nazwę już istniejącegoo pliku
    filepath = 'D:\Python\Kurs Udemy\dane' # testowo adres
    if os.path.isfile(filepath): # sprawdzenie czy dany plik istnieje
        break
    else:
        print('File name is not correct, try again!')

webaddresses = []

file = open(filepath,"r")
for line in file:
    
    line = line.replace('\n','')
    print(line)
    webaddresses.append(line)
file.close

for webaddresse in webaddresses:
    #print(type(webaddresse))
    #print(webaddresse.endswith('.pl'))
    if webaddresse.endswith('.pl'):
        print("adres %s jest adresem z Polski" % (webaddresse))
    else:
        print("adres %s nie jest adresem z Polski" % (webaddresse))
    print(  f"Address {webaddresse} is from Poland" if webaddresse.endswith('.pl') else f"Address {webaddresse} is NOT from Poland") # alternatywne rozwiązanie

print('------------------------------------------')
print('----------zadanie nr 2B----------')

import os
filename =input('Enter filename with web addresses to read: ')
while not os.path.isfile(filename):
    print("File does not exist. Try again: ")
    filename =input('Enter filename to read: ')
webaddresses=[]
with open(filename,'r') as file:
    for line in file:
        webaddresses.append(line.replace("\n",''))
for line in webaddresses:
    if line.endswith('.pl'):
        print(line,'is a polish web page')
    else:
        print(line, 'is not a polish web page')

print('------------------------------------------')
print('----------zadanie nr 3A----------')
# rozdzielanie danych z pliku na dwa pliki
import os

webaddresses = []

while True:
#    filepath = input('Enter path to results file: ') # będziemy chcieli ay użytkownik wprowadził nazwę już istniejącegoo pliku
    filepath = 'D:\Python\Kurs Udemy\dane' # testowo adres
    if os.path.isfile(filepath): # sprawdzenie czy dany plik istnieje
        break
    else:
        print('File name is not correct, try again!')

file = open(filepath,"r")
for line in file:
    
    line = line.replace('\n','')
    print(line)
    webaddresses.append(line)
file.close

filename_webs_pl_txt = 'webs_pl.txt'
filename_webs_other_txt = 'webs_other.txt'
dirname = os.path.dirname(filepath) # folder danego pliku zadeklaarowanego wcześniej

def zapis_pliku(filepath, webaddresse): #definicja funkcji
        if os.path.isfile(filepath): # sprawdzenie istnienia pliku
            print('plik istnieje')
            file = open(filepath, 'a') # aktualizacja pliku
            file.write(webaddresse + '\n')
            file.close() 
        else:
            print('plik nie istnieje')
            file = open(filepath, 'w') # tworzenie nowego pliku
            file.write(webaddresse + '\n')
            file.close()
        return

for webaddresse in webaddresses:
    #print(type(webaddresse))
    #print(webaddresse.endswith('.pl'))
    if webaddresse.endswith('.pl'):
        print("adres %s jest adresem z Polski" % (webaddresse))
        filepath = os.path.join(dirname, filename_webs_pl_txt)
        print(filepath)
        zapis_pliku(filepath, webaddresse)
       
    else:
        print("adres %s nie jest adresem z Polski" % (webaddresse))
        filepath = os.path.join(dirname, filename_webs_other_txt)
        print(filepath)
        zapis_pliku(filepath, webaddresse)
        
print('------------------------------------------')
print('----------zadanie nr 3B----------')

import os
filename =input('Enter filename with web addresses to read: ')
while not os.path.isfile(filename):
    print("File does not exist. Try again: ")
    filename =input('Enter filename to read: ')
webaddresses=[]
with open(filename,'r') as file:
    for line in file:
        webaddresses.append(line.replace("\n",''))
dirname = os.path.dirname(filename)
websPathPL = os.path.join(dirname,'webs_pl.txt')
websPathOther = os.path.join(dirname,'webs_other.txt')
filePL = open(websPathPL,'w')
fileOther = open(websPathOther,'w')
for line in webaddresses:
    if line.endswith('.pl'):
        filePL.write(line+"\n")
    else:
        fileOther.write(line+"\n")
filePL.close()
fileOther.close()





  
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
