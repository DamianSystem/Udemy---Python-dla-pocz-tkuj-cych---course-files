# moduł Błędy w Python

#print 'this is a message' # błąd składni brak nawiasów


# wyjątki - błędy w programie po kompilacji
import sys # do rozpoznania rodzaju błędu

try: # zapobiegnięcie ukrytym wyjątkom w  pisaniu programu
    # wszystkie podejrzane instrukcje zamieść w bloku try
    tasksPerPerson = 0 # ilość zadań na osobę

    task = 32 # ilość zadań które trzeba rozdzielić w zespole
    personsStr = input('How manypersons are there in the team? ')
    persons = int(personsStr)

    tasksPerPerson = task / persons 
except: # jeżeli po drodze pojawi się gdzieś błąd wykona się instrukcja excep
    print("Something went wrong...",sys.exc_info()) #sys.exc_info() - zawiera informację o błędzie który wystąpił
                                                    #sys.exc_info()[0] - pokaże mi rodzaj błędu, pierwszy element z błędu
print("Every person should have around", tasksPerPerson, "tasks")

  
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
