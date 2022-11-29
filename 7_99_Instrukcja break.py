#Instrukcja Break dla pętli For
#------------------------
'''
Służy do przerwania pętli w rtakcie jej wykonywania. 

przykład poszukujemy liczby pierwsze od 2 do 30
zawsze można sprawdzić zasade działąnia debug
'''
'''
print('----------sposób nr 1----------')
for candidate in range (2,31):# wykuszikawnie po kolei kandydatów na liczby pierwsze

    isPrime = True# zakładamy że każda liczba badana jest liczbą pierwszą
    
    for divided in range (2,candidate):  # sprawdzanie czy liczba jest liczbą pierwszą

        if candidate % divided ==0: # warunek jeśli liczba jest podzielna divided be reszty (reszta z dzielenia równa jest 0) jest to liczba parzysta
            isPrime = False
            print("%2d is not a prime number - dividerr is %2d" %(candidate, divided))
            break # powoduje natychmistowe wyjście(zerwanie) pętli wewnętrznej
    if isPrime:
        print("%2d is prime!" % (candidate))

'''
print('----------sposób nr 2----------')
for candidate in range (2,31):# wykuszikawnie po kolei kandydatów na liczby pierwsze


    for divided in range (2,candidate):  # sprawdzanie czy liczba jest liczbą pierwszą

        if candidate % divided ==0: # warunek jeśli liczba jest podzielna divided be reszty (reszta z dzielenia równa jest 0) jest to liczba parzysta
            print("%2d is not a prime number - dividerr is %2d" %(candidate, divided))
            break # powoduje natychmistowe wyjście(zerwanie) pętli wewnętrznej

    else: # else nie będzie wykonywane jeżeli pętla została zerwana przez powyższy w if break
        print("%2d is prime!" % (candidate))


'''
#- deklaracja zmiennej 
#- wyświetlenie
#- wyniki
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
