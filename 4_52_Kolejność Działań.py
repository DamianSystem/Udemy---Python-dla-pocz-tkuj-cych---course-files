# - kiedy pracujesz w Python ze zmiennymi nie musisz określać jej typu, program zrobi to atomatycznie

Title = 'Python'
print('Title is',type(Title))

Version = 3
print('Version is',type(Version))

Progress = 0.21
print('Progress is',type(Progress))

print('This expression is',type(Progress * Version)) # Niektóre typy są silniejsze a niektóre słabsze np. mnożenie

# przypisywanie zmiennych w różnych miejscach w pamięci
x=1
y=1
z=1
print(x,y,z)


# przypisywanie zmiennych w tymm samym miejscu w pamięci

a=b=c=2 # szybki zapis przypisania do zmiennych a, b, c tej samej wartości
print(a,b,c)

c=3 # zmienia tylko wartości przypisanego c
print(a,b,c)

print(2+2*2)

print(6/2*(1+2)) #kolejność działań jak w matematyce

print(4**3**2)

x=1
x+1# wyświetli wartość dwa mimo że wartość x nie zmieniła się i wynosi 1

x = x+1 # przypisanie nowej wartości dla X
x+=1 # oznacza to samo co x = x+1
x++ # ta metoda nie działa w języku python

x = x-1 # przypisanie nowej wartości dla X
x-=1 # oznacza to samo co x = x-1

