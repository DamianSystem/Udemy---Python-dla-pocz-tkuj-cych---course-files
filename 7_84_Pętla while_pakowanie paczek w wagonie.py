#skrypt pokaże nam które paczki należy zapakować do pudła 90 aby wykorzystać jak najwięcej miejsca
cargo = [40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]
cargo.sort()
cargo.reverse()
print("The cargo list is:",cargo)


boxCapacity = 90
box = [] #-deklaraca pustej listy
i = 0

#while sum(box) + cargo[i] < boxCapacity and i<len(cargo):#- pętla z zabespieczeniem jeżeli było by za mało towaru dla paczki to pętla wykonuje się do długości listy, poniżej poprawiony
while i<len(cargo) and (boxCapacity - sum(box) >=min(cargo)):# min(cargo) minimalny element w liście
    if (boxCapacity - sum(box)) >= cargo[i]: #- warunek do pobierania kolejnej największej wartości z listy
        box.append(cargo[i])
    i+=1 #- uwaga na licznik aby był w pętli dobrz e ułożony

print("The collected items sum is:",sum(box)) #- funkcja sum sumuje elementy przekazane jako parametr
print("The element are:",box)



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
