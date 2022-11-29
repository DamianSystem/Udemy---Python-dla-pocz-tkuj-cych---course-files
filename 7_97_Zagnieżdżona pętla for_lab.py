#zagnieżdżona pętla for 
#------------------------
#zagnieżdżona pętla for inaczej jedna pętla w drugiej
#zagnieżdzać pętle można różnego rodzaju
#tabliczka mnożenia


print('----------zadanie nr 1----------')

i=10+1
silnia=1
for x in range(1,i):
    silnia*=x
    print(x,'! = ',silnia,sep='')


print('----------zadanie nr 1A----------')

i=10+1
silnia=1
działanie = '1'
for x in range(2,i):
    silnia*=x
    działanie+='*'+str(x)
    print(x,'! = ',działanie,' = ',silnia,sep='')

print('----------zadanie nr 2----------')
# zadanie z wyliczaniem silni
i=10+1
silnia=1
działanie = '1'
for x in range(1,i):
    silnia*=x
    if x==1:
        print('%2d! = %d'% (x,silnia))
    else:
        działanie+='*'+str(x)
        print('%2d! = %s = %d' % (x,str(działanie),silnia)) #silnia upożądkowana do prawj strony

print('----------zadanie nr 3----------')
#- mój sposób ułożenia napisu do lewej strony
list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for noun in list_noun:
    word = ''
    for adj in list_adj:
        spacja=18-len(adj+' '+noun)
        word+=(adj+' '+noun+' '*spacja) 
    print(word)



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
