# program  Funkcje - własna implementacja SWITCH


import math 
def GiveGeomSeqElement(a1 = 2, factor = 2, index = 2):
    # funkcja wylicza wartość ciągu
    # function computes the string value
    # a1 - pierwszy element ciągu
    # factor - współczynnik ciągu
    # index - nr elementu ciągu do wyliczenia 

    an = (factor**(index-1))*a1
    return an

a_1=1

q=2
nr_a=64


print(' the number fuction is ',GiveGeomSeqElement(a_1, q, nr_a))

a1=3
factor=2
maxindex=10

for i in range(1,maxindex+1,1):
    print(' the number a',i,' fuction is ',GiveGeomSeqElement(a1, factor, i))
    
#---------------------------------
    
def GiveFactorForGeomSeq(an, an_1):
    q=an/an_1
    return q

an=12
an_1=24

print(' Dal parametrów ciągu: an=', an,'i an+1',an_1,' q=',  GiveFactorForGeomSeq(an, an_1))
print('------------------------------------------')
def GiveGeomSeqElement(a1 = 2, factor = 2, index = 2):
    # funkcja wylicza wartość ciągu
    # function computes the string value
    # a1 - pierwszy element ciągu
    # factor - współczynnik ciągu
    # index - nr elementu ciągu do wyliczenia 

    an = (factor**(index-1))*a1
    return an



def GiveSumOfNElementsGeomSeq(a1=2, factor=2, n=2):
    # a1 - pierwszy element ciągu
    # factor - współczynnik ciągu
    # n - nr elementów ciągu do zsumowania 
    sum_elements=0
    for i in range(1,n+1):
        sum_elements=sum_elements+GiveGeomSeqElement(a1, factor,i)
        print('element=',i, 'suma=',sum_elements )
    return sum_elements
print('suma=',GiveSumOfNElementsGeomSeq(2, 3, 4))

#dokończyć 5 zadanie

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
