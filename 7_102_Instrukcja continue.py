#Instrukcja continue dla pętli
'''
jeżeli continue mamy wpisaną w pętle,
to po przejściu na continue w pętli nagle sterowanie przenosimu się do początkowych warunków pętli

przykład ze zmianą i przypisaniem na adres mailowy
'''




'''
print('----------zadanie nr 1A----------')

persons=['Elizabeth','Steven@sales.mycompany.com','Sebastian','Margaret','Svetlana@mycompany.eu','Raphael']


domain = 'mycompany.com'

emails = [] #adresy mailowe chcemy aby były w nowej liście


for person in persons:

    if'@' in person:
        emails.append(person)   # warunek jeżeli zmienna ma małpe (2) dodaj go do listy
    else:                       # jeżeli zmienna nie ma małpki(@) dopisz końcową część adresu     
        email = person+'@'+domain
        emails.append(email)

for email in emails: # wyśietlanie poszczególnych elementów
    print (email)

'''
print('----------zadanie nr 1B----------')

persons=['Elizabeth','Steven@sales.mycompany.com','Sebastian','Margaret','Svetlana@mycompany.eu','Raphael']


domain = 'mycompany.com'

emails = [] #adresy mailowe chcemy aby były w nowej liście

# rozwiązanie zadania za pomocą pętli z poleceniem continue
for person in persons:

    if'@' in person:
        emails.append(person)   # warunek jeżeli zmienna ma małpe (2) dodaj go do listy
        continue                      # przejście na początek pętli do warunku     

    email = person+'@'+domain
    emails.append(email)



for email in emails: # wyśietlanie poszczególnych elementów
    print (email)



'''
#- deklaracja zmiennej 
#- wyświetlenie
#- wyniki
print('----------zadanie nr 1----------')
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
