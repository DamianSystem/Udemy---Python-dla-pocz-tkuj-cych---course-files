# program  Funkcje - własna implementacja SWITCH
'''

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

dokończyć 5 zadanie
'''
import geom # import funkcji którą sobie stworzyłem i zapisałem w pliku

a_1=1

q=2
nr_a=60


print(' the number fuction is ',geom.GiveGeomSeqElement(a_1, q, nr_a)) # wywołanie funkcji którą stworzyłem z parametrami do niej wpisanymi


 print('-------------------------------------------------------')  
 # to samo co wyżej tylko pisane przez autora kursu
ZADANIA 1-4



def GiveGeomSeqElement(a1=2,factor=2,index=2):
    #returns n-th term of geometric sequence starting with element a1 and having 
    value = a1*pow(factor,index-1)
    return value
print('element 64 =',GiveGeomSeqElement(1,2,64))
print('------------------------------------------------')
a1=3
factor=2
maxindex=10
for i in range(1,maxindex):
    an = GiveGeomSeqElement(a1=a1,factor=factor,index=i)
    print('Term ',i,'=',an)
print('------------------------------------------------')
def GiveFactorForGeomSeq(term, nextterm):
    #returns factor for geometrical sequence having two following terms of the sequence
    return nextterm/term
print('Factor is', GiveFactorForGeomSeq(12,24))
print('------------------------------------------------')
def GiveSumOfNElementsGeomSeq(a1=2, factor=2, n=2):
    #returns sum of n first elements of geometrical sequence with first term a1 and factor
    sumN = a1*(1-pow(factor,n))/(1-factor)
    return sumN
print('Sum of n elements is', GiveSumOfNElementsGeomSeq(2,3,4))






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
