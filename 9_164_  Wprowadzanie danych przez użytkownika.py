# program  wprowadzanie danych przez użytkownika 

'''

filename = input("Enter filename: ")        # wprowadzenie - c:\temp\reasults.py
                                            # w pliku filename będie przechowana waartość jako - c:\\temp\\reasults.py
                                            # wprowadzona wartość jest zawsze interpretowana jako napis - string
print("The file name is: %s" % (filename))  # wyświetli - The file name is: c:\temp\reasults.py - oczekujemy że to będą znaki


filesize = input("Enter the max file size (MB): ") 
print("The max size is %s" % (filesize))
print("Size in KB is %s" % (filesize *1024)) # napis zostałtyle razy powielony ile wskazuje liczba (tu 1024)

'''
while True: #warunek dla sprawdzenia poprawności wprowadzonych danych
    filesizeStr = input("Enter the max file size (MB): ") # filesizeStr w formacie string

    if filesizeStr.isdecimal(): # warunek czy dana wartość jest liczbą - funkcja testująca zawartość danych
        filesizeInt = int(filesizeStr)
        break

print("The max size is %d" % (filesizeInt))
print("Size in KB is %d" % (filesizeInt *1024))





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
