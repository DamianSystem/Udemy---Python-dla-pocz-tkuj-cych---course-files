# lista tuple - po polsku krotka - stała lista

Tax = (4, 7, 8, 23) #- używamy nawiasów okrągłych

print(Tax[2]) # wywoływanie nr 2  indeksie liczonego od zera Python

print(Tax[-1]) # wywołanie ostatniego elementu w liscie tuple
print(Tax.index(7)) # - pokaże na jakiej pozycji jet liczba 7 - tuple.index(element)
print(Tax.count(8)) # - ile razy występuje dany element (8) na liście - tuple.count(element)
print(max(Tax)) #- maksymalna wartość w liście tuple

#tax.revert() insert, sort nie ma możliwości modyfikacji, zmieniania zmiennych danych.

TaxList = list(Tax) # konwersja na listę aby poukładać dane
TaxList.append(30) # dodanie do listy wartości 30 na końcu listy
NewTax = tuple(TaxList) # konwersja na listę tuple(stałą listę) aby poukładać dane


print(type(Tax))
print(Tax)
print(TaxList)
print(NewTax)


(tax1, tax2, tax3, tax4) = Tax #- przypisanie zmiennych z listy tuple
print(tax1, tax2, tax3, tax4) # wyświetlenie poszczególnych zmiennych

a=1
b=10
print("a =",a,"\tb = ",b)
#temp=a                      #-dodatkowa zmienna buforowa
#a=b                         #-proces zamiany miejscami wartości zmiennych
#b=temp                      #-proces zamiany miejscami wartości zmiennych

(a,b)=(b,a)                 #-proces zamiany miejscami wartości zmiennych w locie

print("a =",a,"\tb = ",b)   #-wyświetlenie zamiany miejscami wartości zmiennych


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
