helloMessage= "Hello %s!"                    #- deklaracja zmiennej
print(helloMessage % ('Kate'))               #- wyświetlenie
print(helloMessage % ('Chris'))              #- wyświetlenie

helloMessage= "Hello {0:s}!"                 #- deklaracja zmiennej 
print(helloMessage.format ('Kate'))                 #- wyświetlenie
print(helloMessage.format ('Chris'))                #- wyświetlenie

helloMessage= "%s has %d %s"                 #- deklaracja zmiennej
print(helloMessage %('Kate', 1, 'animal'))   #- wyświetlenie
print(helloMessage %('Chris', 100000, '$'))  #- wyświetlenie

helloMessage= "{0:s} has {1:d} {2:s}"        #- deklaracja zmiennej 
print(helloMessage.format ('Kate', 1, 'animal'))    #- wyświetlenie
print(helloMessage.format ('Chris', 100000, '$'))   #- wyświetlenie 
                              
Line= '{0:20s} costs {1:6d} €'               #- deklaracja zmiennej 
print(Line.format ('ICE CREAM', 3))                 #- wyświetlenie
print(Line.format ('TRIP TO VENICE', 119))          #- wyświetlenie
print(Line.format ('PIZZA HAWAII', 6))              #- wyświetlenie

Line= '%s   %d'                              #- deklaracja zmiennej 
print(Line %('ICE CREAM', 3))                #- wyświetlenie
print(Line %('TRIP TO VENICE', 119))         #- wyświetlenie
print(Line %('PIZZA HAWAII', 6))             #- wyświetlenie


                               #- 
                               #- 
                               #- 
                               #- 
