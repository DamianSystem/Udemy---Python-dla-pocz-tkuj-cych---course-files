#Typy timedelta, data i datetime

-------do zapisania w notatniku!!!!!!!!!!!
import datetime #moduł dotyczący daty i czasu
#date time nie uznaje sekund przestępnych

print('Minimum and maximum', datetime.MINYEAR, datetime.MAXYEAR)# minimalna i maksymalna wartość dla roku

#from datetime import timedelta
d1 = datetime.timedelta(days=1,hours=2,minutes=-30) #- służy do liczenia różnicy czasu (d1 to jeden dzień 2 godziny bez 30 minut -Wynik: 1 day, 1:30:00)
print(d1) 

d2 = datetime.timedelta(days=-1,hours=-2,minutes=-3) # d1 to jeden dzień wcześniej 2 godziny wcześniej 3 minuty wcześniej (wynik: -2 days, 21:57:00)
print(d2)

print("timedelta sum:",d1+d2) #- wynik -1 day, 23:27:00 - podsumowując ogólnie - 33 minuty
print('-------------------------------------------------\n\n\n')


#from datetime import date

print('Today is',datetime.date.today()) #- wywołanie daty dzisiejszej
print('\n')

today = datetime.date.today() # zapamiętanie daty w zmiennej
daysToPay = datetime.timedelta(days=7) # płatność w przeciągu 7 dni, obiekt po ilu dniach należy zapłacić
print("Today is ", today)
print("Bills should be paid within:", daysToPay.days,"days") # wyświetlenie po ilu dniah należy zapłacić rachunek
print("The bill should be paid till:",today + daysToPay) # data kiedy trzeba zapłacić rachunek
print('\n')


endOfTheWorld = datetime.date.max
print("The fimal end of world will happend (by Python):",\
      endOfTheWorld) # pokazuje date
print(endOfTheWorld.weekday()) # pokazuje nr dnia tygodnia
print('\n')

bornDate = datetime.date(2000,8,15)
today = datetime.date.today()
print(today - bornDate) # liczymy same dni bez godzin, minut i sekund.
print('\n')

print('-------------------------------------------------\n\n\n')


# from datetime import datetime # aby nazwa nie była taka długa można zaimportować moduł poleceniem from do katalogu głównego

print('now()\t',datetime.datetime.now())#datetime.datetime.now() nr 1 datetime. - nazwa modułu nr2 .datetime. nazwa typu łączącego w sobie datę i czas 
print('today()\t',datetime.datetime.today()) # funkcja now i today pokazuje czas lokalny na komputerze
print('utcnow()\t',datetime.datetime.utcnow()) # pokazywanie czasu w strefie czasowej
print('weekday()\t',datetime.datetime.today().weekday()) # funkcja zwraca nr dnia tygodnia
print('\n')

print('%a\t',datetime.datetime.now().strftime("%a"))# funkcja .strftime("%a") konwertuje czas do napisu, %a skrócona nazwa dnia tygodnia (Wed)
print('%A\t',datetime.datetime.now().strftime("%A"))# funkcja .strftime("%A") konwertuje czas do napisu, %A pełna nazwa dnia tygodnia (Wednesday)
print('%w\t',datetime.datetime.now().strftime("%w"))# funkcja .strftime("%w") oznacza nr dnia tygodnia, niedziele liczymy jako dzień zerowy
print('%a %A %w',datetime.datetime.now().strftime("%a %A %w"))
print("%Y-%m-%d_%H_%M_%S_%f",\
      datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S_%f")) # przydatne do zapisu pliku
#%Y - lata przy użyciu czterech cyfr
#- %m - miesiące
#- %d - dni
#- %H - godziny od 0 - 23
#- %M - minuty
#- %S - sekundy
#- %f - milisekundy

#more details:
#https://docs.python.org/3/library/datetime.html    


'''
#- deklaracja zmiennej 
#- wyświetlenie
#- wyniki
print('----------zadanie nr 1----------')

print('-------------------------------------------------------')
print('----------zadanie nr 2----------')
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
