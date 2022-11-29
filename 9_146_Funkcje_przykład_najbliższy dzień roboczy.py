#Funkcje przykład: najbliższy dzień roboczy - VIDEO

def GiveWorkingday():
    #print the nearest working day date

    from datetime import date # import dzisiejszego dnia
    from datetime import timedelta # funkcja dodawania np. jednego lub dwóch dni 

    day = date.today() # prypisywanie daty dzisiejszej

    #day = date(2017,10,1)# zapis konketnej daty tu niedzieli
    #day = date(2017,9,30) # zapis konketnej daty tu soboty

    if day.weekday() == 5: #gdy dzisiejszy dzieńjest sobotą
        workingday = day + timedelta (days=2) # przypisanie dnia pracującego dwa dni po sobocie (day + timedelta (day=2))
    elif day.weekday() == 6:
        workingday = day + timedelta (days=1)
    else:
        workingday = day

    print ('Working day for',day,'is',workingday)
    return

GiveWorkingday()



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
