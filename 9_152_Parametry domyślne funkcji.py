# program parametry domyślne funkcji 

from datetime import date # import dzisiejszego dnia
from datetime import timedelta # funkcja dodawania np. jednego lub dwóch dni 


def GiveWorkingday(year=date.today().year, month=1, day=1):
    #day=1 parametr domyślny w funcji zadziała gdy wywołanie funkcji będzie  GiveWorkingday(2017,9)
    #wartość day zostanie domyślnie zmieniona na 1

    

    day = date(year,month,day)# zapis konketnej daty tu niedzieli
  
    if day.weekday() == 5: #gdy dzisiejszy dzieńjest sobotą
        workingday = day + timedelta (days=2) # przypisanie dnia pracującego dwa dni po sobocie (day + timedelta (day=2))
    elif day.weekday() == 6:
        workingday = day + timedelta (days=1)
    else:
        workingday = day

    print ('Working day for',day,'is',workingday)
    return

GiveWorkingday(2017,9,) # wywołanie funkcji bez jednego parametru
GiveWorkingday(2017,9,2) 
GiveWorkingday(2017)

print('-------------------------------------------------------')

from datetime import date # import dzisiejszego dnia
from datetime import timedelta # funkcja dodawania np. jednego lub dwóch dni 



def GiveWorkingday(year=date.today().year, \
                   month=date.today().month, \
                   day=date.today().day):
    #parametr domyślny w funcji zadziała gdy wywołanie funkcji będzie  GiveWorkingday()
    #wartość year zostanie domyślnie zmieniona rok dzisiejszy
    #wartość month zostanie domyślnie zmieniona miesiąc dzisiejszy
    #wartość day zostanie domyślnie zmieniona dzień dzisiejszy
    

    

    day = date(year,month,day)# zapis konketnej daty tu niedzieli
  
    if day.weekday() == 5: #gdy dzisiejszy dzieńjest sobotą
        workingday = day + timedelta (days=2) # przypisanie dnia pracującego dwa dni po sobocie (day + timedelta (day=2))
    elif day.weekday() == 6:
        workingday = day + timedelta (days=1)
    else:
        workingday = day

    print ('Working day for',day,'is',workingday)
    return

GiveWorkingday(2017,9,2) 
GiveWorkingday() # zwraca wszystkie wartości domyślne funkcji
GiveWorkingday(2017,2)

'''
#- deklaracja zmiennej 
#- wyświetlenie
#- wyniki
print('----------zadanie nr 1----------')
print('-------------------------------------------------------')
print('----------zadanie nr 2----------')

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
