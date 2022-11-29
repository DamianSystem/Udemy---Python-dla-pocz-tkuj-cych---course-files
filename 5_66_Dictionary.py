#- dictionary - słownik

CountryLeaders = {'PL':'Duda','US':'Trump'} #- słownik budowa klucz np. PL i wyświetli się wartości przechowywane w słowniku Duda,
#elementy rozdzielone przecinkami, każdy z elementów składa się z dwóch części kraju i liderakraju.(rozdzielone dwukropkami.
# w ten sposób tworzymy słowniki

print(CountryLeaders['US']) #- odwołanie się do klucza aby otrzymać jego wartości uwaga nawiasy kwadratowe


CountryLeaders['DE'] = 'Merkel' #- przypisanie (dodanie) nowego klucza z wartością, powiększenie słownika

#print(CountryLeaders.items())   #- zwraca  elementy dict.items()
#print(CountryLeaders.keys())    #- zwraca klucze dict.keys()
#print(CountryLeaders.values())  #- zwraca  wartości dict.values()


#print(CountryLeaders.popitem()) #- pobierze element z lity zwóci i usunie go z listy, destruktywna literacja po słowniku krok po kroku usuwane są elementy
#print(CountryLeaders.setdefault('FR','Macron')) #- gdyby nie było jeszcze klucza FR wtedy wyświetl wartość Macron dodatkowo wartość zostanie dodana do listy    dict.setdefault
#print(CountryLeaders.get('RU')) #- próbuje dowiedzieć się jaką wartość ma Ru. nie zostje nic dodane do słownika, brak wartości daje None, dict.get(key)

NewLeaders = {'RU':'Putin','DE':'Schulz'}
print(NewLeaders)
CountryLeaders.update(NewLeaders) #- poszerzenie elementów słownika o inny słownik, jeśli znajdzie ten sam klucz to podmieni wartość, jak nie zostanie znaleziona identyczny klucz to zostanie dodany

#print(type(CountryLeaders))
print(CountryLeaders)


'''



#- deklaracja zmiennej 
#- wyświetlenie
#- wyniki
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
