drive = 'c:\\'                  #- podwójny \\ oczytuje nam program jako pojedynczy \ inaczej jest błąd
folder = 'scripts\\python\\'
file = 'myscript.py'
path = drive + folder +  file
print(path)                     #- wyświetlenie prawidłowe z jednym \ (backslash) (c:\scripts\python\myscript.py)
path                            #- wyświetlenie w shelu nieprawidłowo z dwoma \\ (backslash) ('c:\\scripts\\python\\myscript.py')

justText = "text with\nnewline" #- błąd nie wyświetla \n (backslash)
print(justText)
justText = r"text with\nnewline"#- r jak raw surowy tekst przed cudzysłowiem (r"text with\nnewline") wtedy nie dochodzi do żadnej interpretacji znaków specjalnych w tekście)
print(justText)                                 #- 

justText = 'Mc Donald's'        #- błąd zbyt duża ilość apostrofów
print(justText)
justText = "Mc Donald's"        #- jest ok otwarcie i zamknięcie to cudzysłów " "
print(justText)
justText = 'Mc Donald\'s'       #- jest ok po \(backslash)
print(justText)


line = 'He said"I like Python!"' #- jeżeli używamy cudzysłowia (") w zdaniu klamry zamykające tekst to apostrofy (') 
print(line)                               #- 
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
                               #-
                               #-
                               #- 
                               #- 
                               #- 
                               #- 
                               #- 
                               #- 
