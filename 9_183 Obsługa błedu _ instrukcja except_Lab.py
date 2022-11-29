# moduł Błędy w Python

import sys
 
file_path = r'c:\temp\data_input\orders.csv'
 
 
with open(file_path,"r") as file:
 
    for line in file:
 
        line = line.replace('\n','')
        order = line.split(',')
 
        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
            print('Order from drugstore "%s", item "%s", amount %d' %
                      (pharmacy_name, item, amount))
        except ValueError as e: # możemy różnicować komunikaty błędu ze względu na rodzaj błędu (błąd wartości) 
            print('Sorry - there was an error related to incorrect data conversion in the third field to type int.', e)
            print(line)
        except IndexError as e: # możemy różnicować komunikaty błędu ze względu na rodzaj błędu (błąd wartości) 
            print('Sorry - Error related to not enough fields.', e)
            print(line)
        except:
            print("Problem with line %s" % line)
            print(sys.exc_info()[0])
 
print("Processing finished")

print('-------------------------------------------------------')  
# to samo co wyżej tylko pisane przez autora kursu 

'''Pharma A, Vitamin C,100
Drugstore XYZ,Penicilin, 20, pills
Drugstore ABC,Aspirin,60
Pharma X,Montelukast,10
Pharma at grocery,Amoxicillin,?
Pharmacy 123,Cephalexin,100
Pharmacy 123,Prednisolone Sodium Phosphate
Pharma X,Nystatin,45'''
 
import sys
 
file_path = r'c:\temp\data_input\orders.csv'
 
 
with open(file_path,"r") as file:
 
    for line in file:
 
        line = line.replace('\n','')
        order = line.split(',')
 
        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
            print('Order from drugstore "%s", item "%s", amount %d' %
                      (pharmacy_name, item, amount))
 
        except ValueError as e:
            print("Problem with conversion. Check whether the amount is correct. Line: %s" % line)
 
        except IndexError as e:
            print("Missing information. Check whether the line is build of at least 3 fields separated by comma. Line: %s" % line)
 
        except:
            print("General error: %s" % sys.exc_info()[0])
            
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
