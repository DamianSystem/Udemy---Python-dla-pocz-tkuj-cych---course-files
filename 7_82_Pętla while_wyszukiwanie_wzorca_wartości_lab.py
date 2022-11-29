#- znalezienie trzech liczb ułożonych rosnąco w liście, znalezienie trójki liczb:

numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11] 

print(type(numbers))

i_2 = 0
i_3 = 0
max_2 = len(numbers) -1
print(max_2)

max_3 = len(numbers) -2
print(max_3)

while i_2<max_2: 
    print(i_2,numbers[i_2])
    if(numbers[i_2]**2==numbers[i_2+1]):
        print('\tFound: ', numbers[i_2], numbers[i_2+1])

    i_2+=1

print('--------')
while i_3<max_3: 
    print(i_3,numbers[i_3])
    if(numbers[i_3]**2==numbers[i_3+1] and numbers[i_3+1]**2==numbers[i_3+2]):
        print('\tFound: ', numbers[i_3], numbers[i_3+1], numbers[i_3+2])

    i_3+=1
    
print('--------')




texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

texts_i = 0
max_texts_i_2 = len(texts) -1

print(type(texts))

while texts_i<max_texts_i_2: 
    print(texts_i,texts[texts_i])
    if(len(texts[texts_i])==len(texts[texts_i+1])):
        print('\tFound: ', texts[texts_i], texts[texts_i+1])

    texts_i+=1








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
