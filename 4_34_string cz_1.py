atext='This is a text.'                                  #- wprowadzenie zmiennej typu tekstowego
atext.endswith('ext')                                    #- sprawdzenie czy tekst skończył się na 'ext' - wartości true lub false
atext.islower()                                          #- sprawdzenie czy tekst jest napisany małymi literami
atext.upper ()                                           #- zmiana na duże litery chwilowo (.upper ())
atext.upper().isupper ()                                 #- zmiana na duże litery chwilowo (.upper () )i sprawdzenie czy są wszystkie duże litery(.isupper) 
atext.find('is')                                         #- sprawdzenie czy w tekscie występuje słowo 'is' - find('is') - zwraca nr znaku gdzie się pojawił,znaki liczy od zera
atext.find('is',3)                                       #- sprawdzenie czy w tekscie występuje słowo 'is' od 3 znaku liczonego od 0 - find('is',,3) - zwraca nr znaku gdzie się pojawił,znaki liczy od zera
atext.replace('a','4')                                   #- zamiana znaku a na 4 w tekście (.repleace('a','4'))
atext.replace('a','4').replace('i','1').replace('e','3') #- zamiana znaku a na 4, i na 1, e na 3 w tekście (.repleace('a','4').replace('i','1').replace('e','3'))
atext.split(' ')                                         #- podział tekstu ze względu na spacje 

somethingLikeNumber='1000'                               #- wprowadzenie liczby jako typu tekstowego
somethingLikeNumber.isdigit()                            #- sprawdza tekst czy jest to liczba  (.isdigit()) true - wygląda jak liczba false nie jest liczbą
somethingLikeNumber.isdecimal()                          #- sprawdza tekst czy jest to liczba z przecinkiem, może mieć wartości po przecinku (.isdecimal()) true - wygląda jak liczba false nie jest liczbą
somethingLikeNumber.isalpha()                            #- sprawdza tekst czy  ma same literki true - jest false - nie jest
somethingLikeNumber.isalnum ()                           #- sprawdza tekst czy jest alfanumeryczny - ma same cyferki  czy litery
                               #-
                               #-
                               #- 
