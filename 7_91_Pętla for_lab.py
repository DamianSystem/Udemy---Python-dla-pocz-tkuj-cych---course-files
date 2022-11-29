data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']
text = 'text_0'
print('--------','zadanie 1','--------')
for print_data in data:
    print(print_data.upper())

print('--------','zadanie 2','--------')

for print_data_2 in data:
    wyswietl = print_data_2.split(':')
   
    print(wyswietl[0].upper(),wyswietl[1])

warunek = 'Error'

print('--------','zadanie 3','--------')



for print_data_3 in data:
    wyswietl_3 = print_data_3.split(':')
    if warunek == wyswietl_3[0]:
        print(wyswietl_3[1].upper()) #operacja na liście duże litery
    else:
        print(wyswietl_3[1])
        


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
