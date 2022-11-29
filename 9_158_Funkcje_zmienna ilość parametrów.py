# program Funkcje_zmienna ilość parametrów

def DoAction (action, parameter):
    print("action:", action)
    print("parameter:",parameter)
    return

DoAction('buy','shoes')
#DoAction('buy','shoes','socks') #- funkcja zakończyła się błędem

def DoAction2 (action, *parameter): # *parameter - gwiastka przy parametrach oznacza kolekcje parametrów (statyczna lista tuple) 
    print("action:", action)
    print("parameter:",parameter)
    for element in parameter:
        print("element is",element) # wydruk elemmentów z listy 
    return

DoAction2('buy','shoes','socks')
DoAction2('buy','shoes','socks','t-shirt')

    
def DoAction3 (action, what, **parameter): # uwaga dwie gwiastki **parameter - zmienna stała się słownikiem 
    print("action:", action)
    print("what:", what)
    print("parameter:",parameter)
    for element in parameter:
        print(element,"=",parameter[element])
    return

DoAction3('buy','shoes',size=45, color='brown',type='sport') # ***poniżej wydruk, bez pętli for
'''                                                          # ***
action: buy                                                  # ***
what: shoes                                                  # ***
parameter: {'size': 45, 'color': 'brown', 'type': 'sport'}   # ***
'''



'''
#- deklaracja zmiennej 
#- wyświetlenie
#- wyniki
print('----------zadanie nr 1----------')
print('-------------------------------------------------------')
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
