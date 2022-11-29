# moduł odczyt z pliku .csv

#wyświetlanie danych z pliku .csv z obróbką

file_path = r'c:\temp\data_input\orders.csv'

with open(file_path,"r") as file:
    for line in file: # wczytywnie linijka po linijce pliku z powyższym otwarciem liku(bardzo duża wydajność) - nie trzymanie w pamięci komputera
        #print(line)
        line_rob = line
        line_rob = line_rob.replace('\n','').replace(' ','').split(',')
        #print(line_rob)
        #print(len(line_rob))
        #print(line_rob[0])
        if len(line_rob)== 3:
            print('Order from drugstore "%s", item "%s", amount %s' % (line_rob[0], line_rob[1], line_rob[2]))  
        else:
            line_rob = line.replace('\n','')
            print('Line "%s" malformed!!!' % (line_rob))
print('File done :)')


print('-------------------------------------------------------')  
# to samo co wyżej tylko pisane przez autora kursu  

'''Pharma A, Vitamin C,100
Drugstore XYZ,Penicilin, 20, pills
Drugstore ABC,Aspirin,60
Pharma X,Montelukast,10'''
 
file_path = r'c:\temp\data_input\orders.csv' # treść powyższa skopiowana do pliku z podaną ścieżką
 
 
with open(file_path,"r") as file:
 
    for line in file:
 
        line = line.replace('\n','')
        order = line.split(',')
 
        if len(order) == 3:
            print('Order from drugstore "%s", item "%s", amount %s' %
                  (order[0],order[1],order[2]))
        else:
            print("Line %s malformed!!!" % line)
 
print("Processing finished")


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
