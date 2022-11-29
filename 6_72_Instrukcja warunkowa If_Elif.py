#Instrukcja warunkowa If

age = 27
isDrunk = False
isRestrictedArea = False


#-nested if (zagnieżdżone if)

if age <18: #- warunek logiczny jeżeli, pamiętaj o dwukropku
    print("You are too young to buy alcohol") #- pamiętaj o wcięciach
else:
    if  isDrunk: #- warunek logiczny jeżeli, pamiętaj o dwukropku
        print("Are You drunk? We cannot sell you alcohol") #- pamiętaj o wcięciach
    else: 
        if isRestrictedArea: #- warunek logiczny jeżeli, pamiętaj o dwukropku
            print("Restricted area. Alcohol is forbidden") #- pamiętaj o wcięciach
        else:
            print("OK, You can buy alcohol") #- pamiętaj o wcięciach
print("----")

#- składnia If z else if

if age <18: #- warunek logiczny jeżeli, pamiętaj o dwukropku
    print("You are too young to buy alcohol") #- pamiętaj o wcięciach
elif  isDrunk: #- warunek logiczny else if, jeżeli warunek przy pierwszym warunku nie został spełniony
    print("Are You drunk? We cannot sell you alcohol") #- pamiętaj o wcięciach
elif isRestrictedArea: #- warunek logiczny jeżeli, pamiętaj o dwukropku
    print("Restricted area. Alcohol is forbidden") #- pamiętaj o wcięciach
else:
    print("OK, You can buy alcohol") 



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
