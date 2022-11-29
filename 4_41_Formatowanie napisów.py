message1= 'Proces file %s'              #- %s - s od string
print(message1 % ('file_1.txt'))        #- zamiana litery s na tekst file_1.txt (Proces file file_1.txt)
message2= 'File %s has size %d KB'      #- %s - s od string, %d d od ??? (wartość liczbowa)
print(message2 % ('file_1.txt',100))    #- zamiana litery s na tekst file_1.txt  oraz d na 100
#print(message2 % (100, 'file_1.txt'))  #- żle nie można zamieniać typów zmienych, muszą być zgodne z zadeklarowanymi
message3= 'File %20s has size %10d KB'  #- %20s - ilość zarezerwowanych znaków w wartości tekstowej, %d10 - ilość zarezerwowanych znaków w wartości liczbowej
print(message3 % ('file_1.txt',100))
message4= 'Proces file {0:s}'           #- w nowszym oprogramowaniu 0:s mówi o jednym parametrze string - tekstowy, uwaga na nawiasy {}
message4.format ('file1.txt')           #- zerowy parametr to file1.txt
message5= 'File {0:s} has size {1:d}'    #- zerowy parametr to tekst a pierwszy parametr to liczba, uwaga na nawiasy {}
message5.format ('file1.txt',100)       #- zerowy parametr to file1.txt pierwszy parametr to 100
message6= 'File {1:s} has size {0:d}'    #- pierwszy parametr to tekst a zerowy parametr to liczba, uwaga na nawiasy {}
message6.format (100, 'file1.txt')       #- zerowy parametr to 100 pierwszy parametr to file1.txt
message7= 'File {0:20s} has size {1:10d}'    #- zerowy parametr to tekst z 20 polami a pierwszy parametr to liczba z dziesięcioma polami, wyświetlane w słupku, tabela , uwaga na nawiasy {}
message7.format ('file1.txt',100)       #- zerowy parametr to file1.txt pierwszy parametr to 100
 
Zacząć od formatowanie napisów LAB 44


                               #- 
                               #- 
                               #- 
                               #- 
                               #- 
                               #- 
