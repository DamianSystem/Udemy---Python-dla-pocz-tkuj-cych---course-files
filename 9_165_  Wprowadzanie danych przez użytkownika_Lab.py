# program  wprowadzanie danych przez użytkownika 

print('Program ma obliczyć funkcję pierwiastki funkcji kwadratowej y=a*x*x+b*x+c')
a_Str = input("Podaj wartość a: ")
b_Str = input("Podaj wartość b: ")
c_Str = input("Podaj wartość c: ")


#print(type(a_Str))
#print(a_Str.find('-'))
#print(b_Str.find('-'))
#print(c_Str.find('-'))
char_a = 1
char_b = 1
char_c = 1 

if a_Str.find('-') == 0:
    a_Str = a_Str.replace('-','')
    char_a = -1
    
if b_Str.find('-') == 0:
    b_Str = b_Str.replace('-','')
    char_b = -1
    
if c_Str.find('-') == 0:
    c_Str = c_Str.replace('-','')
    char_c = -1
#print(a_Str)
#print(b_Str)
#print(c_Str)
    
if a_Str.isdecimal() and b_Str.isdecimal() and c_Str.isdecimal():
    a_Int = int(a_Str)*char_a
    b_Int = int(b_Str)*char_b
    c_Int = int(c_Str)*char_c
    #print("to liczby całkowite")
    if a_Int==0 :
        print("to nie jest równanie kwadratowe")
    else:
        delta = b_Int*b_Int-(4*a_Int*c_Int)
        if delta <0:
            print("brak rozwiązań")
        elif delta == 0:
            x1=(-b_Int-(delta**0.5))/(2*a_Int)
            print('x = ', round(x1,2))
        elif delta >0:
            x1=(-b_Int-(delta**0.5))/(2*a_Int)
            x2=(-b_Int+(delta**0.5))/(2*a_Int)
            print("x1 = ", round(x1,2), ", x2 = ", round(x2,2))
else:
    print ("Podane liczby nie są liczbami całkowitymi")

 print('-------------------------------------------------------')  
 # to samo co wyżej tylko pisane przez autora kursu 


def check_int(s):   # sprawdzenie czy dane wejściowe są liczbą WAżne
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()
 
print('This program solves equation ax^2+bx+c = 0')
print('Enter the values for a, b and c:')
 
a_str = input('a=')
b_str = input('b=')
c_str = input('c=')
 
if not( check_int(a_str) and check_int(b_str) and check_int(c_str) ):
    print("a, b and c need to be int!")
else:
    a = int(a_str)
    b = int(b_str)
    c = int(c_str)
 
    if a == 0:
        print('a cannot be 0!')
    else:
        delta = b**2 - 4*a*c
 
        if delta < 0:
            print("there is no solution")
        elif delta == 0:
            x1 = -b/(2*a)
            print("there is one solution: %.2f" % (x1))
        else:
            x1 = (-b-delta**0.5)/(2*a)
            x2 = (-b+delta**0.5)/(2*a)
            print("there are two solutions: %.2f and %.2f" % (x1,x2))




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
