#Funkcje moduł time i calendary
import time # używane od wersji 3.7 Python


 
# sprawdzenie wersji pythona
import sys
print(sys.version)
 
# zamiast
# print(time.clock(), time.localtime(time.clock())) # funkcja dostępna w wersji 2.x Python
# korzystaj z funkcji time.perf.counter():
print(time.perf_counter(), time.localtime(time.perf_counter()))


import time # moduł operujący na dacie i czasie

print("current time is ... unix epoch", time.time()) # funkcja zwraca czas( od 1 styczznia 1970 roku - powstanie unix zegar idzie do przodu 1raz / sekunde)
print("\n")
print("current time is ... tuple", time.localtime(time.time())) # pokazuje aktualny czas (tm_year=2022, tm_mon=7, tm_mday=13, tm_hour=11, tm_min=5, tm_sec=38, tm_wday=2, tm_yday=194, tm_isdst=1)
# np. tm_year=2022,- aktualny rok
#tm_mon=7, - miesiąc
#tm_mday=13, - dzień
#tm_hour=11, - godzina
#tm_min=5, - minuty
#tm_sec=38, - sekundy
#tm_wday=2, - dzień tygodnia
#tm_yday=194, - dzień  w roku
#tm_isdst=1 - strefa czasowa
print("\n")
print("current time is ... for human", time.asctime(time.localtime(time.time()))) # pokazuje datę (Wed Jul 13 11:05:38 2022)
print("\n")
print("current time is ... for human", time.localtime(time.perf_counter())) # czas opierany na prędkości procesora, badzo dokładne obliczenia można na tym opierać
print("\n\n\n\n\n\n")

# playing with calendar

import calendar # moduł operujący na dacie, miesiącu i latach służy do wyświetlania kalendarzy 
print('-------------------------------------------------------')
print(calendar.month(2017,9,w=5,l=2)) # wyświetlenie kalendarza za określony miesiąc na każdy dzień jest po 5 znaków a odstępy między liniami mają wynosić 2
print('-------------------------------------------------------')
print(calendar.month(2017,9)) # wyświetlenie kalendarza za określony miesiąc na każdy dzieńz minimalnymi wartościami
print('-------------------------------------------------------')
print('week day is',calendar.weekday(2017,9,29)) # pokazuje, który dzień tygodnia jest danego dnia (week day is 4) 0- poniedziałek 1- wtorek...
print('-------------------------------------------------------')
calendar.setfirstweekday (6) # ustawienie aby pierwszym dniem tygodnia była niedziela a nie poniedziałek - wpływa tylko jak kalendarz jest rysowany
print('-------------------------------------------------------')
print(calendar.month(2017,9)) # calendar.setfirstweekday (6) ma wpływ od jakiego dnia tygodnia rysuje się kalendarz
print('-------------------------------------------------------')
print('week day is',calendar.weekday(2017,9,29)) # calendar.setfirstweekday (6) nie zmienia wartości funkcji .weekday
print('-------------------------------------------------------')
print('is 2020 a leap year?', calendar.isleap(2020)) # .isleap - zwraca wartość true jeśli dany rok jest przestępny
print('-------------------------------------------------------')
print('Leap day 2000-2017', calendar.leapdays(2000,2017)) # .leapdays - ile było dni przestępnych w tych latach
print('Leap day 2000-2020', calendar.leapdays(2000,2020)) # końcowy zakres funkcji nie jest bany pod uwagę
print('Leap day 2000-2021', calendar.leapdays(2000,2021))

print(calendar.calendar(2018)) # funkcja ta powoduje wyrysowanie kalendarza za cały rok.

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
