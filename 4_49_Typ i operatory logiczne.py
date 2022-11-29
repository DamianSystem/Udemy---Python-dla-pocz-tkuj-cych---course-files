IsWeekend = True                    #- deklaracja zmiennej logicznej
print("Is weekend =",IsWeekend)     #- wyświetlenie

Temperature = 20                    #- deklaracja zmiennej liczbowej można porównywać
print("Temperature =",Temperature)  #- wyświetlenie

ToDoList=''                         #- deklaracja zmiennej
print("ToDoList =",ToDoList)        #- wyświetlenie

IsHappy = IsWeekend and Temperature >=20 and ToDoList == '' 
# sprawdzenie warunków czy są prawdziwe (true) IsWeekend nie trzeba porównywać(true)
# temperadura czy jest większa od 20 stopni i  ToDoList wartość napisy czy jest pusta
# jeżeli wszystkie warunki są spełnione w wyniku otrzymamy true jeśli nie folse 
print("IsHappy=",IsHappy)

IsWeekend = True                    #- deklaracja zmiennej logicznej
print("Is weekend =",IsWeekend)     #- wyświetlenie

Temperature = 5                    #- deklaracja zmiennej liczbowej można porównywać
print("Temperature =",Temperature)  #- wyświetlenie

ToDoList=''                         #- deklaracja zmiennej
print("ToDoList =",ToDoList)        #- wyświetlenie

IsHappy = IsWeekend and Temperature >=20 and ToDoList == '' 
# sprawdzenie warunków czy są prawdziwe (true) IsWeekend nie trzeba porównywać(true)
# temperadura czy jest większa od 20 stopni i  ToDoList wartość napisy czy jest pusta
# jeżeli wszystkie warunki są spełnione w wyniku otrzymamy true jeśli nie folse 
print("IsHappy=",IsHappy)


IsWeekend = False                    #- deklaracja zmiennej logicznej
print("Is weekend =",IsWeekend)     #- wyświetlenie



Temperature = 5                    #- deklaracja zmiennej liczbowej można porównywać
print("Temperature =",Temperature)  #- wyświetlenie

ToDoList='Shopping'                         #- deklaracja zmiennej
print("ToDoList =",ToDoList)        #- wyświetlenie

IsHappy = not IsWeekend and Temperature <20 and ToDoList != '' 
# sprawdzenie warunków czy są prawdziwe (true) IsWeekend czy jest folse
# temperadura czy jest mniejsza od 20 stopni i  ToDoList wartość napisy czy nie jest pusta
# jeżeli wszystkie warunki są spełnione w wyniku otrzymamy true jeśli nie folse 
print("IsHappy=",IsHappy)


IsHappy = IsWeekend and Temperature >=20 and ToDoList == '' \
          or not IsWeekend and Temperature <20 and ToDoList != '' #warunek z przeniesieniem dalszej części do następnej lini(\)
print("IsHappy=",IsHappy)

IsHappy = IsWeekend and Temperature >=20 and ToDoList == '' \
          or not IsWeekend and not Temperature >=20 and not ToDoList == '' #not Temperature >=20 nie temperatura powyżej lub równa 20, not ToDoList == '' - nieprawda że lista musi być pusta
print("IsHappy=",IsHappy)


IsHappy = IsWeekend and Temperature >=20 and ToDoList == '' \
          or not IsWeekend and not (Temperature >=20 or ToDoList == '' )#  not (Temperature >=20 or ToDoList == '' ) zamiast zaprzeczać dwa warunki zaprzeczamy ich alternatywe
print("IsHappy=",IsHappy)


# \ - przeniesienie, złamanie lini i pisanie w następnym wierszu (kontynuacja lini z \ w następnym wierszu)

# operatory logiczne
#-------------
# == - porównanie wartości przed i za znakiem
# > - większe od wartości za znakiem
# >= - większy lub równy od wartości za znakiem
# != - porównanie wartości czy są różne lewa z prawą stroną 
# 
# and - używany przy warunkach do spradzenia czy ten i ten warunek jest prawdziwy 
# or -  używany przy warunkach do spradzenia czy ten lub ten warunek jest prawdziwy
# not - zaprzeczenie danej zmiennej (przeciwieństwo) zapis X<20 to not X>=20
# not a and not b to tosamo co not(a or b) - zamiast zaprzeczać dwa warunki zaprzeczamy ich alternatywe
# kolejność wykonywania działań jak w matematycze najpier nawiasy później element (np. not) koło nawiasu i dalej


#Uwaga na małe i duże litery

# typ zmiennej
# bool - typ True or False

#Uwaga na małe i duże litery




#- deklaracja zmiennej 
#- wyświetlenie
#- wyniki

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
