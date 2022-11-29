# moduł . Kontrola ścieżki do plliku
# sprawdzenie czy plik jest w danej ścieżce
'''
Tym razem otrzymujesz zadanie zautomatyzowania pobierania danych dotyczących zamówień kierowanych
z aptek do dystrybutora leków. Zamówienia są przesyłane w postaci plików CSV
i umieszczane w katalogu c:\temp\data_input. Pliki są tam umieszczane przez różne inne procesy
w ciągu całego dnia. Codziennie o godzinie 19:00 będzie uruchamiany skrypt, który przeniesie te
pliki do innego folderu, np c::\temp\yyyy-mm-dd (gdzie yyyy to rok, mm to miesiąc, a dd to dzień z
daty dzisiejszej). Potem na tych plikach są wykonywane dalsze operacje, jak np. import danych.

Obecnie skupimy sie na etapie sprawdzenia, czy wszystkie warunki do uruchomienia przetwarzania są spełnione, tzn.:
 '''   

import os
import datetime

def check_dir_exist(input_dir):
    if os.path.isdir(input_dir):
        volume = True
    else:
        volume = False
    return volume




data_input_catalog = r'c:\temp\data_input' 
print(data_input_catalog)

data_output_catalog = r'c:\temp\data_output'
print(data_output_catalog)

today = datetime.date.today()
print(today)
print(today.strftime("%Y-%m-%d")) # zamiana daty w formacie data na format str

print(type(today))
print(type(today.strftime("%Y-%m-%d")))

today_output_catalog = os.path.join(data_output_catalog, today.strftime("%Y-%m-%d"))
print(today_output_catalog)

#checking conflicts
 
#input folder must exist

is_input_catalog_ok = check_dir_exist(data_input_catalog)
print(is_input_catalog_ok)

#output folder must exist
is_output_catalog_ok = check_dir_exist(data_output_catalog)
print(is_output_catalog_ok)

#today output catalog cannot exist
is_today_output_catalog_ok = os.path.isdir(today_output_catalog) and os.path.isfile(today_output_catalog)# sprawdzenie czy dana ścieżka nie istnieje jako katalog i plik
print(is_today_output_catalog_ok)



if is_input_catalog_ok and is_output_catalog_ok and not is_today_output_catalog_ok:
    print('Conditions met! We can continue!')
else:
    print('Prerequisites not met! Check the paths!')
    text = ''
    if not is_input_catalog_ok:
        text = text + 'There is no input_catalog.'
    if not is_output_catalog_ok:
        text = text + 'There is no output_catalog.'
    if is_today_output_catalog_ok:
        text = text + 'There is today_output_catalog.'
    print(text)

print('-------------------------------------------------------')  
 # to samo co wyżej tylko pisane przez autora kursu 


import datetime
import os
 
data_input_catalog = r'c:\temp\data_input'
data_output_catalog = r'c:\temp\data_output'
 
today = datetime.date.today()
today_output_catalog = os.path.join(data_output_catalog, today.strftime("%Y-%m-%d"))
 
#checking conflicts
 
#input folder must exist
is_input_catalog_ok = os.path.isdir(data_input_catalog)
 
#output folder must exist
is_output_catalog_ok = os.path.isdir(data_output_catalog)
 
#today output catalog cannot exist
is_today_output_catalog_ok = not(os.path.isdir(today_output_catalog)) and \
                             not(os.path.isfile(today_output_catalog))
 
if is_input_catalog_ok and is_output_catalog_ok and is_today_output_catalog_ok:
    print('Conditions met! We can continue!')
else:
    print('Prerequisites not met! Check the paths!')
    
    #display detailed error conditions
    if not is_input_catalog_ok:
        print("Input catalog %s must exist!" % data_input_catalog)
    if not is_output_catalog_ok:
        print("Output catalog %s must exist!" % data_output_catalog)
    if not is_today_output_catalog_ok:
        print("Today's output %s cannot exist (neither as file nor as directory)!" % today_output_catalog)
 





'''
#- deklaracja zmiennej 
#- wyświetlenie
#- wyniki
print('----------zadanie nr 1----------')
print('------------------------------------------')
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
