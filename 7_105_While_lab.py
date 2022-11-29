#pętla while


print('----------zadanie nr 1----------')

# obliczanie zarobku na lokacie

initialCapital  = 20000
percent         = 0.03
maxTimeYears    = 10
TimeYears       = 0
Capital         = initialCapital

print(type(maxTimeYears))


while TimeYears <  maxTimeYears:
    Capital+=Capital*0.03
    TimeYears+=1
    print('Po ',TimeYears,'roku oszczędzania masz kwote',round(Capital,2))
    
roundCapital = round((float(Capital)-initialCapital),2)
print('Po', maxTimeYears,' latach zarobek to ',roundCapital )

print('-------------------------------------------------------')

print('----------zadanie nr 2----------')
#program do sumowania cyfr
number = 20730906
working_number = number
sum_number = 0
digit_number = 0

while working_number>0:
    digit_number = working_number%10
    working_number = working_number//10
    sum_number += digit_number

print(' suma cyfr wynosi', sum_number)



print('-------------------------------------------------------')
print('----------zadanie nr 3----------')


#program do liczenia w tekście słów dłuższych niż 6 znaków
text = '''
United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.
'''
wordLength = 6
row = text.split('\n')
counter_word = 0

while len(row)>0 :
#    print(row.pop()) # do usunięcia
    words = row.pop(0)
    word = words.split(' ')
    while len(word)>0:
        if len(word[0])>wordLength:
            counter_word += 1
        word.pop(0)    

print('wyrazów które mają powyżej %d liter jest %d' %(wordLength, counter_word))





text = '''
United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.
'''
listOfWords = text.replace('\n',' ').split(' ') # inner rozwiązanie
wordLength = 6
i=0
shortWords = 0
longWords = 0
while i< len(listOfWords):
     if len(listOfWords[i])>wordLength:
        longWords+=1
     elif len(listOfWords[i]) > 0:
        shortWords+=1
    
     i+=1
print("Words shorter than ",wordLength,":",shortWords)
print("Words longer than ",wordLength,":",longWords)
          
#                    
#print(words)
#while 
#len(word)


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
