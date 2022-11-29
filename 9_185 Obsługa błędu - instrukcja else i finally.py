# moduł Błędy w Python

# wyjątki - błędy w programie po kompilacji
import sys # do rozpoznania rodzaju błędu

try: # zapobiegnięcie ukrytym wyjątkom w  pisaniu programu
    # wszystkie podejrzane instrukcje zamieść w bloku try
    tasksPerPerson = 0 # ilość zadań na osobę

    task = 32 # ilość zadań które trzeba rozdzielić w zespole
    personsStr = input('How manypersons are there in the team? ')
    persons = int(personsStr)

    tasksPerPerson = task / persons

   # print("Every person should have around", tasksPerPerson, "tasks") - jedna z możliwości ukrycia komunikatu aby się nie wyświetlał gdy jest błąd w programie(zamiast na końcu programu ta linia
except ValueError as e: # możemy różnicować komunikaty błędu ze względu na rodzaj błędu (błąd wartości) 
    # zmienna e podaje rodzaj błędu który się pojawił, możemy go zebrać do bazy lub pliku błędów
    print('Sorry - you need to enter an integer number.', e)
except ZeroDivisionError  as e: # możemy różnicować komunikaty błędu ze względu na rodzaj błędu (dzielenie przez zero)
    # zmienna e podaje rodzaj błędu który się pojawił, możemy go zebrać do bazy lub pliku błędów
    print('Sorry - you need to enter valume > 0.', e)

except: # jeżeli po drodze pojawi się gdzieś błąd inny niż wyżej wymienione wykona się końcowa instrukcja excep
    print("Something went wrong...",sys.exc_info()) #sys.exc_info() - zawiera informację o błędzie który wystąpił
                                                    #sys.exc_info()[0] - pokaże mi rodzaj błędu, pierwszy element z błędu
else: # instrukcja else wykona się wtedy gdy nie doszło do kompletnie żadnego błędu w części programu try:
    print("Every person should have around", tasksPerPerson, "tasks")
finally: #instrukcje zostaną wykonane niezależnie od tego czy doszło do błędu czy też nie
    # wykonujemy tu czynności które muszą zostać wykonane np. zamykanie otwartych plików, może być użyty do posprzątania po bloku try
    print('Script finished with/without error')






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
