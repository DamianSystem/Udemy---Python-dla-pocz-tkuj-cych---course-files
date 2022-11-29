#moduł math
print('----------zadanie nr 1A----------')
print('-------------------------------------------------------')
import math # import funkcji math



'''
1° = (π * rad)/180 # wzory zamiany radianów na stopnie i odwrotnie   
1 rad = 180°/π
'''

degree_1 = 360

rad_1 = math.pi*degree_1/180
print('rad_1',rad_1)

print('\n')
print('-------------------------------------------------------')
print('\n')
degree_2 = 45

rad_2 = math.pi*degree_2/180
print('rad_2',rad_2)
print('\n')
print('-------------------------------------------------------')
print('\n')
print('rad_1', math.radians(degree_1)) # math.radians(degree_1) - konwertuje stopnie na radiany
print('rad_2', math.radians(degree_2))


small_pizza_r = 22
big_pizza_r = 27
family_pizza_r = 38
small_pizza_price = 11.50
big_pizza_price =  15.60
family_pizza_price = 22.00
print('\n')
print('-------------------------------------------------------')
print('\n')
small_pizza_field = math.pi*(small_pizza_r/100)**2
print('small_pizza_field=',round(small_pizza_field,2))
big_pizza_field = math.pi*(big_pizza_r/100)**2
print('big_pizza_field=',round(big_pizza_field,2))
family_pizza_field = math.pi*(family_pizza_r/100)**2
print('family_pizza_field=',round(family_pizza_field,2))
print('\n')
print('-------------------------------------------------------')
print('\n')
small_pizza_price = (1/small_pizza_field)*small_pizza_price
print('small_pizza_price=',round(small_pizza_price,2))
big_pizza_price = (1/big_pizza_field)*big_pizza_price
print('big_pizza_price=',round(big_pizza_price,2))
family_pizza_price = (1/family_pizza_field)*family_pizza_price
print('family_pizza_price=',round(family_pizza_price,2))

math_ls = dir(math)  #przypisanie do zmiennej math_ls atrybutów(opcji) modułu math 
print(math_ls)       # wyświetlenie atrybutów (opcji)

print('----------zadanie nr 1B----------')
print('-------------------------------------------------------')
import math
 
degree = 360
radian = degree * math.pi /180
print("%d degree is %f radians" % (degree, radian))
 
degree = 45
radian = degree * math.pi /180
print("%d degree is %f radians" % (degree, radian))
print('')
 
print("%d degree is %f radians" % (360, math.radians(360)))
print("%d degree is %f radians" % (45, math.radians(45)))
print('')
      
small_pizza_r = 0.22
big_pizza_r = 0.27
family_pizza_r = 0.38
 
small_pizza_price = 11.50
big_pizza_price = 15.60
family_pizza_price = 22.00
 
small_area = math.pi * small_pizza_r**2
big_area = math.pi * big_pizza_r**2
family_area = math.pi * family_pizza_r**2
 
print('small', small_pizza_r,small_pizza_price, small_area)
print('big', big_pizza_r,big_pizza_price, big_area)
print('family', family_pizza_r,family_pizza_price, family_area)      
print('')
print('small', small_pizza_price/small_area)
print('big', big_pizza_price/big_area)
print('family', family_pizza_price/family_area)
print('')
      
math_ls = dir(math) 
print(math_ls)


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
