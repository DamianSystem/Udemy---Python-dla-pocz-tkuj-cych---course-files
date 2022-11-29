countries = ['FR','US','DE','RU'] #- lista elementów poroździelanych przecinkami
countries[1] = 'GB'   #- zmiana (podmiana) elementu nr1 Python
print(countries[1]) #- wyświetlanie pojedynczego elementu list[position] pozycja 1
countries.append('PL') #- dodanie elementu PL na końcu listy list.append(element)
countries.insert(2,'ES') #- wstawianie dodatkowej wartości na 2 indeksie Python (list.insert(position,element)
countries.remove('RU') #- usuwanie lementu z listy (podajemy nazwę elementu) list.remove(element)
countries.sort()  #- sortowanie elementów na liście (alfabetycznie) list.sort()
countries.reverse() # - odwrócenie listy list.reverse()
print(countries.pop(2)) # - indeks 2 python jest pokazywany i usuwany z listy (do inicjacji kolejki z listy) list.pop(position)
print(countries.index('PL')) #sprawdzenie czy dany element jest na liście i zwraca nr pozycji na liście - list.index(element)
#print(countries.index('US'))# - gdy sprawdze i elementu nie będzie na liście dostanę błąd
print(countries.count('DE')) # sprawdzenie ile razy na liście jest dany element list.count(element)


newList = ['FI','SE'] # nowa lista
countries.extend(newList) # rozszerzenie elementów listy countries o elementy liste newList list.extend(list)

#countriesCopy = countries # Żle, wartość listy przypisana do wartości innej listy Uwaga ma to samo miejsce w pamięci 
countriesCopy = countries.copy()  #  prawidłowo kopia orginalnej listy  list.copy
countriesCopy.clear() #- list.clear czyści wartości z listy


print(countries)  #- wyświetlenie
print(countriesCopy)  #- wyświetlenie


#- deklaracja zmiennej 
#- wyświetlenie
#- wyniki

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
