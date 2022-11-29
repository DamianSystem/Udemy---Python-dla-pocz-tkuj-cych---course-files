#zagnieżdżona pętla for 
#------------------------
#zagnieżdżona pętla for inaczej jedna pętla w drugiej
#zagnieżdzać pętle można różnego rodzaju
#tabliczka mnożenia
print('----------zadanie nr 1----------')
for x in range(1,6):
    line = str(x) #- x określa numer wiersza a y nr kolumny
 
    for y in range(1,6):
        line+='\t'+ str(x*y) # dla każdego y który oznacza nr kolumny przy czym tom wyznaczoną wartość będe doklejał do kolejnej liniki 
#- budowanie w pętli for wyrazu który potem jest wyświetlany
    print(line)    

#        print(x ,'*', y,' = ',x*y)

print('----------zadanie nr 1A----------')
#- moja zabawa pokazuje mnożenie i wyniki
for x in range(1,6):
 #   line = str(x) #- x określa numer wiersza a y nr kolumny
    line = ''
    for y in range(1,6):
        line+='\t'+ str(x) +'*'+str(y)+'='+ str(x*y) # dla każdego y który oznacza nr kolumny przy czym tom wyznaczoną wartość będe doklejał do kolejnej liniki 
#- budowanie w pętli for wyrazu który potem jest wyświetlany
    print(line)    

#        print(x ,'*', y,' = ',x*y)

print('----------zadanie nr 2----------')
for x in range(1,6):
    line = str(x) #- x określa numer wiersza a y nr kolumny
 
    for y in range(1,6):
        line+=('\t%3d'% (x*y)) # dla każdego y który oznacza nr kolumny przy czym tom wyznaczoną wartość będe doklejał do kolejnej liniki 
# sumowanie elementów za każdym razem w pętli (tabulator wyrównanie do prawej strony ('\t%%3d'% (x*y)
#- budowanie w pętli for wyrazu który potem jest wyświetlany z formatowaniem tekstu(wyrównaniem do prawej strony)
    print(line)    

#        print(x ,'*', y,' = ',x*y)



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
