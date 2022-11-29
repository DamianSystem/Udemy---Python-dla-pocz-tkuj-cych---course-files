min_linkes = 500
min_shares = 100

num_linkes = 1300
num_shares = 55

if num_linkes < min_linkes:
    print('Likes not enough')
else:
    if num_shares < min_shares:
        print('Shares not enought')
    else:
        print('obniżka 10%')

print("-----")

if num_linkes < min_linkes:
    print('Likes not enough')
elif num_shares < min_shares:
    print('Shares not enought')
else:
    print('obniżka 10%')



isPizzaOrdered = False
isBigDrinkOrdered = False
isWeekend = True


if isWeekend == False:
    if isPizzaOrdered == True :
           print('otrzymujesz kupon na Burgera')
    else:
           if isBigDrinkOrdered == True:
               print('otrzymujesz kupon na Burgera')
           else:    
               print("nie zakupiłeś drinka lub pizzy")
else:
    if isPizzaOrdered == True :
           print("zakupy nie były dokonane w weekend")
    else:
           if isBigDrinkOrdered == True:
               print("zakupy nie były dokonane w weekend")
           else:
               print("nie zakupiłeś drinka lub pizzy")
print("-----")       
           
if isWeekend == False:
    if isPizzaOrdered == True :
           print('otrzymujesz kupon na Burgera')
    elif isBigDrinkOrdered == True:
               print('otrzymujesz kupon na Burgera')
    else:    
               print("nie zakupiłeś drinka lub pizzy")
elif isPizzaOrdered == True :
        print("zakupy nie były dokonane w weekend")
elif isBigDrinkOrdered == True:
        print("zakupy nie były dokonane w weekend")
else:
               print("nie zakupiłeś drinka lub pizzy")    
 
#---odpowiedzi Udemy


MIN_LIKES = 500

MIN_SHARES = 100



num_likes = 300

num_shares= 550



if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:

    print('GREAT! Today our prizes drop 10% !!!')

else:

    if num_likes <MIN_LIKES:

        print('We still need more likes to start the promotion')

    else:

        print('We still need more shares to start the promotion')



##############################################



if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:

    print('GREAT! Today our prizes drop 10% !!!')

elif num_likes <MIN_LIKES:

     print('We still need more likes to start the promotion')

else:

     print('We still need more shares to start the promotion')



##############################################



isPizzaOrdered = True

isWeekend = True

isBigDrinkOrdered = True



if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:

    print('Burger for FREE!!!')

else:

    if isWeekend:

        print('Come back on non-Weekend day')

    else:

        print('You need to order Pizza or Big drink to have a Burger coupon')



##############################################



if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:

    print('Burger for FREE!!!')

elif isWeekend:

    print('Come back on non-Weekend day')

else:

    print('You need to order Pizza or Big drink to have a Burger coupon')



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
