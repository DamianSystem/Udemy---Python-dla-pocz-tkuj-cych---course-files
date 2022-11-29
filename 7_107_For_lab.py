#pętla FOR

'''
print('----------zadanie nr 1A----------')
# liczby Fibionacciego rozkład do 20 

fibonacci_number_previous = 0
fibonacci_number_actualy = 0
fibonacci_number_next = 1
fibonacciIterations=20

print ('Fibonacci nr %3d is %d' %(1,fibonacci_number_actualy))

for number in range(2,fibonacciIterations+1):
    fibonacci_number_previous = fibonacci_number_actualy
    fibonacci_number_actualy=fibonacci_number_next
    fibonacci_number_next = fibonacci_number_previous + fibonacci_number_actualy
    print ('Fibonacci nr %3d is %d'%(number ,fibonacci_number_actualy))

'''
print('----------zadanie nr 1B----------')
fibonacciIterations = 20
a1 = 0
a2 = 1
a3 = 0
for i in range(0,20):
    print('Step',i,'value',a3)
    a1=a2
    a2=a3
    a3=a1+a2

print('-------------------------------------------------------')
print('----------zadanie nr 2----------')
# znajdowanie i wyświetlanie słowa z literką 'p'

text = '''
Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn’t do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it’s an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can’t.'''

'''
words = text.replace('\t',' ').replace('\n',' ').split(' ')

for word in words:
    if word.find('p')>=0:
        print(word)
'''
        
print('-------------------------------------------------------')
print('----------zadanie nr 3A----------')
'''          
# wyświetlanie elementów słownika w postaci wierszy klucz i wartość
dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less then 50%'}

keys=dictionary.keys()

for key in keys:
    print ('%s - %s'%(key, dictionary[key]))
'''

print('-------------------------------------------------------')
print('----------zadanie nr 3B----------')

'''
dictionary={'A':'80%-10%','B':'60%-80%','C':'50-60%','D':'less then 50%'}
for word in dictionary.keys(): # inne rozwiązanie
    print(word,'-',dictionary[word])

'''

print('-------------------------------------------------------')
print('----------zadanie nr 4A----------')
text = '''
ZADANIE 1

Ciąg Fibonacciego to ciąg rozpoczynający się od 0 i 1 a każda kolejna liczba to suma dwóch poprzednich, np:

0
1
0+1 = 1
1+1 = 2
1+2 = 3
2+3 = 5
....

Korzystając z pętli for napisz program, który wyliczy fibonacciIterations=20 pierwszych elementów ciągu Fibonacciego

Wskazówka:
-zadeklaruj 3 dodatkowe zmienne a1, a2 i a3. Początkowo a1=0 a a2=1. a3 będziesz wyliczać jako sumę a1 i a2. W pętli trzeba też będzie zmieniać wartość a1 na a2 oraz a2 na a3



ZADANIE 2

Masz dany tekst:

Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn’t do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it’s an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can’t.
Twoim zadaniem jest wyświetlić tylko te słowa, które zawierają literkę "p"



ZADANIE 3

Dany masz słownik:

dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less then 50%'} 

Wyświetl zestawienie w postaci (kolejność nie jest istotna):

A - 80%-100%
B - 60%-80%
C - 50-60%
D - less then 50%

'''
user_text = text.replace('\t',' ').replace('\n',' ').replace(',',' ').replace('\'',' ').replace('  ',' ') # pomocne przy wyszukiwaniu tekstu
user_text =  user_text.split(' ')    
new_word_dictionary={user_text[1]: '0'}
word_dictionary={}

for word in user_text:
    word_dictionary.update(new_word_dictionary)
    for item_dictionary in word_dictionary:
        if word == item_dictionary:
           new_word_dictionary[word]= int(word_dictionary.pop(word))+1
           break
        else:
            new_word_dictionary[word]=1
print(word_dictionary)


print('----------zadanie nr 4B----------')

wordDictionary={}
for word in listOfWords:
    if word in wordDictionary.keys():
        wordDictionary[word] = wordDictionary[word]+1
    else:
        wordDictionary.setdefault(word,1)
        
print(wordDictionary)





'''
#- deklaracja zmiennej 
#- wyświetlenie
#- wyniki
print('----------zadanie nr 1----------')

print('-------------------------------------------------------')
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
