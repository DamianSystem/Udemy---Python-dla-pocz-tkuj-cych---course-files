#trochę matematyki w Python

print('-------------------------------------------------------')
print('----------zadanie nr 1B----------')

percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,
           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,
           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,
           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,
           8.740978348,6.174819567]
 
countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia',
             'Norway', 'Portugal','United Kingdom','Serbia','Germany','Albania',
             'France','Czech Republic','Denmark','Australia','Finland','Bulgaria',
             'Moldova','Sweden','Hungary','Israel','Netherlands','Ireland',
             'Cyprus','Italy']


print(sum(percent))

sumOfPoints = 4988
Dictionary = {}


for number in (range(0, len(percent))):# przypisywanie wartości w słowniku
        Dictionary.setdefault(countries[number],percent[number])

        
print(Dictionary)
print(' min = ',round(min(Dictionary.values()),2) , ' max =  ',round(max(Dictionary.values()),2))

LenCountriesMax=len(max(countries))
LenPercentMax=len(str(max(percent)))

message = '%'+str(LenCountriesMax)+'s %'+str(LenPercentMax)+'s' 
'''
print(message)
for i in range(0,len(countries)):
        print(message %(countries[i],percent[i]))
print('---------------------------------------------------------')
for i in range(0,len(countries)):
    print(message %(countries[i],int(percent[i])))
print('---------------------------------------------------------')
for i in range(0,len(countries)):
    print(message %(countries[i],round(percent[i],2)))
'''
print('---------------------------------------------------------')
for i in range(0,len(countries)):
    print(countries[i],int((sumOfPoints*percent[i])/100))    

print('-------------------------------------------------------')
print('----------zadanie nr 1B----------')


percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,
           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,
           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,
           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,
           8.740978348,6.174819567]
 
countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia',
             'Norway', 'Portugal','United Kingdom','Serbia','Germany','Albania',
             'France','Czech Republic','Denmark','Australia','Finland','Bulgaria',
             'Moldova','Sweden','Hungary','Israel','Netherlands','Ireland',
             'Cyprus','Italy']
 
sumOfPoints = 4988
 
print('min', min(percent), 'max', max(percent))
 
for i in range(len(countries)):
 
    print(percent[i], int(percent[i]), round(percent[i],2), int(round(percent[i]*sumOfPoints/100,0)), countries[i])

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
