#Moduły

print('----------zadanie nr 1----------')
print('-------------------------------------------------------')

inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]



import math
quantity_inputdata = len(inputdata)
print(quantity_inputdata)
quantity_factortable = len(factortable)
print(quantity_factortable)

work_inputdata=inputdata.copy()
work_inputdata.sort()
maxvalue=work_inputdata[0]
minvalue=work_inputdata[quantity_inputdata-1]


if quantity_inputdata == quantity_factortable:
    for i in range(0,quantity_inputdata):
        print(i,' ',inputdata[i]," ok")
        work_min_value = inputdata[i] - factortable[i] * inputdata[i]
        work_max_value = inputdata[i] + factortable[i] * inputdata[i]
        print('work_min_value = ',work_min_value)
        print('work_max_value = ',work_max_value)
        mininteger = math.floor(minvalue)
        print(mininteger)
        maxinteger = math.ceil(maxvalue)
        print(maxinteger)

        if work_min_value<minvalue:
            minvalue=work_min_value
        if work_max_value>maxvalue:
            maxvalue=work_max_value
        
    else:
        print('minvalue = ',minvalue)
        print('maxvalue = ',maxvalue)
else:
    print( "inputdata and factortable need to have equal number of elements")



print('----------zadanie nr 2----------')
print('-------------------------------------------------------')


import random

inputdata = [0,1,2,3,5,8,13,21,34,55,89]





quantity_inputdata = len(inputdata)
print(quantity_inputdata)


work_inputdata=inputdata.copy()
work_inputdata.sort()
maxvalue=work_inputdata[0]
minvalue=work_inputdata[quantity_inputdata-1]



for i in range(0,quantity_inputdata):
     print(i,' ',inputdata[i]," ok")
     factortable = random.random()
     print('factortable = ',factortable)
     work_min_value = inputdata[i] - factortable * inputdata[i]
     work_max_value = inputdata[i] + factortable * inputdata[i]
     print('work_min_value = ',work_min_value)
     print('work_max_value = ',work_max_value)
     if work_min_value<minvalue:
         minvalue=work_min_value
     if work_max_value>maxvalue:
         maxvalue=work_max_value
else:
    print('minvalue = ',minvalue)
    print('maxvalue = ',maxvalue)


print('----------zadanie nr 3----------')
print('-------------------------------------------------------')

import datetime
print(datetime.date.today())
print(datetime.datetime.now().strftime("%Y-%m-%d"))

print('-------------------------------------------------------')

import math
inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]
print('input data has  ',len(inputdata),'elements')
print('factor table has',len(factortable),'elements')
if len(inputdata) == len(factortable):
    i=0
    while i<len(inputdata):
        minvalue=inputdata[i]-factortable[i]*inputdata[i]
        maxvalue=inputdata[i]+factortable[i]*inputdata[i]
        print('minvalue=',minvalue,'maxvalue=',maxvalue)
        
        mininteger = math.floor(minvalue)
        maxinteger = math.ceil(maxvalue)
        print(mininteger,"\t",inputdata[i],"\t",maxinteger)
        i+=1
else:
    print("inputdata and factortable need to have equal number of elements")
print('--------------------------------------------------------------------')
 
import random
i=0
while i<len(inputdata):
    minvalue=inputdata[i]-random.random()*inputdata[i]
    maxvalue=inputdata[i]+random.random()*inputdata[i]
    print('minvalue=',minvalue,'maxvalue=',maxvalue)
    
    mininteger = math.floor(minvalue)
    maxinteger = math.ceil(maxvalue)
    print(mininteger,"\t",inputdata[i],"\t",maxinteger)
    i+=1
print('--------------------------------------------------------------------')
 
from datetime import datetime
print('results generated',datetime.today())
print('results generated:',datetime.today().strftime("%Y-%m-%d"))
 
# another solution (by Tomek - thanks for cooperation!):
import datetime
print('results generated',datetime.date.today())
print('results generated:',datetime.date.today().strftime("%Y-%m-%d"))









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
