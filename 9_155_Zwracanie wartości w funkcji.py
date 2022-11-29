# program Zwracanie wartości w funkcji

from datetime import date # import dzisiejszego dnia
from datetime import timedelta # funkcja dodawania np. jednego lub dwóch dni 

def GiveWorkingday(year=date.today().year, \
                   month=date.today().month, \
                   day=date.today().day):
    day = date(year,month,day)# zapis konketnej daty tu niedzieli
    if day.weekday() == 5: #gdy dzisiejszy dzieńjest sobotą
        workingday = day + timedelta (days=2) # przypisanie dnia pracującego dwa dni po sobocie (day + timedelta (day=2))
    elif day.weekday() == 6:
        workingday = day + timedelta (days=1)
    else:
        workingday = day
    
    return workingday # po słowie return jest zwracana wartość


nextworkingday = GiveWorkingday(2017,9,2) # zwrócona wartość workingday i przypisana do nextworkingday
print ('Next working day after',2017,9,2,'is',nextworkingday)

nextworkingday = GiveWorkingday() # przypisanie wartości wynikowej z funkcji (workingday) do nextworkingday
print ('Next working day after today is',nextworkingday) # to samo co poniżej
print ('Next working day after today is',GiveWorkingday())


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
