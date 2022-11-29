# moduł Błędy w Python

# wyświetlenie linijki z blędem w pliku i rodzaj błędu
import sys

file_path = r'c:\temp\data_input\orders.csv' # treść powyższa skopiowana do pliku z podaną ścieżką
 
 
with open(file_path,"r") as file:
 
    for line in file:
        line = line.replace('\n','')
        order = line.split(',')
        try:
            pharmacy_name = order[0]
            item =  order[1]
            amount = int(order[2])
            print('Order from drugstore "%s", item "%s", amount %d' %
                  (pharmacy_name, item, amount))
        except:
            print("Problem with line %s" % line)
            print("Something went wrong ...",sys.exc_info()[0])

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
