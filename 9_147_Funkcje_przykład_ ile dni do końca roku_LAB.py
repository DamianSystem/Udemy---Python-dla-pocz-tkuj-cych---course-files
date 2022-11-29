# program ile zostało dni do końca roku (do sylwestra)
def DaysToEndOfYear():

    import datetime

    today_day = datetime.date.today()
    current_year  = datetime.datetime.now().strftime("%Y")
    date_end_year = datetime.date(int(current_year),12,31)
    delta = date_end_year - today_day
    
    print(delta.days) # wyświetlanie dni z typu timedelta
    return
    
DaysToEndOfYear()




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
