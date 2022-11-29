# program parametry funkcji najbliższy dzień roboczy



def GiveWorkingday(year, month, day):
    # (year, month, day) w nawiasie okrągłym określe jakie paramerty ta funkcja może przyjmować
    #print the nearest working day date

    from datetime import date # import dzisiejszego dnia
    from datetime import timedelta # funkcja dodawania np. jednego lub dwóch dni 

    #day = date.today() # prypisywanie daty dzisiejszej

    day = date(year,month,day)# zapis konketnej daty tu niedzieli
    #day = date(2017,9,30) # zapis konketnej daty tu soboty

    if day.weekday() == 5: #gdy dzisiejszy dzieńjest sobotą
        workingday = day + timedelta (days=2) # przypisanie dnia pracującego dwa dni po sobocie (day + timedelta (day=2))
    elif day.weekday() == 6:
        workingday = day + timedelta (days=1)
    else:
        workingday = day

    print ('Working day for',day,'is',workingday)
    return

GiveWorkingday(2017,9,30) #Wywołanie funkcji z wartościami zmiennych (2017,9,30) (year, month, day)
GiveWorkingday(2017,10,1) # wywołanie przekazuje parametry w określonej kolejności (year, month, day), jest istotns kolejność podawania warrtości
GiveWorkingday(2017,10,2) # parametry przekazane przez pozycję
GiveWorkingday(2017,10,3)
GiveWorkingday(2017,10,4)
GiveWorkingday(2017,10,5)
GiveWorkingday(2017,10,6)
GiveWorkingday(2017,10,7)

GiveWorkingday(year=2017,month=12,day=6) # parametry przekazane przez nazwę
GiveWorkingday(day=6,month=12,year=2018) # wywołanie funkcji z przypisaniem wartości konkretnym parametrom. nie jest istotna kolejność podawanych wartości
#GiveWorkingday( # edytor Igle podpowie jakie są parametry w funkcji w dymku
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
