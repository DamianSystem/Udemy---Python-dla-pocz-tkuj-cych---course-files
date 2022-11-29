# program parametry funkcji LAB

print('----------zadanie nr 1A----------')
print('-------------------------------------------------------')
def PrintAnimal(animal=''):
    # this function prints a animal ascii-art
    # uwaga na zmienne tekstowe obsługujące funkcję!!!
    if animal == 'cat':     
        txt = r'''
        |\---/|
        | o_o |
         \_^_/'''
    

    elif animal == 'bear':
        txt = r'''    
        /  \.-"""-./  \
        \    -   -    /
         |   o   o   |
         \  .-'"'-.  /
          '-\__Y__/-'
             `---`'''
    
    elif animal == 'bat':
        txt = r'''
           /\                 /\
          / \'._   (\_/)   _.'/ \
         /_.''._'--('.')--'_.''._\
         | \_ / `;=/ " \=;` \ _/ |
          \/ `\__|`\___/`|__/`  \/
                  \(/|\)/       '''

    else:
        message = "Cannot print '%s'. Correct values for the parameter are: cat, bear, bat"
        print(message%(animal))
        return
    
    print(txt)
    return



PrintAnimal('cat')
print('-------------------------------------------------------')
PrintAnimal('bear')
print('-------------------------------------------------------')
PrintAnimal('bat')
print('-------------------------------------------------------')
PrintAnimal('Bat')
print('-------------------------------------------------------')
PrintAnimal()
print('-------------------------------------------------------')
#więcej fajnych obrazków znajdziesz np tu: https://www.asciiart.eu/


print('----------zadanie nr 2A----------')
print('-------------------------------------------------------')
from datetime import date

def DaysToEndOfYear(year= date.today().year, \
                    month=date.today().month, \
                    day=date.today().day):
    #Days To End Of Year
   
    date_today = date(year, month, day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)
    return

DaysToEndOfYear(2022, 1, 1)
DaysToEndOfYear( month=1, day=2, year=2022)
DaysToEndOfYear()

print('----------zadanie nr 2B----------')
print('-------------------------------------------------------')

from datetime import date
 
def DaysToEndOfYear(year = date.today().year,
                    month = date.today().month,
                    day = date.today().day):
    
    date_today = date(year,month,day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    print('Counting from ', date_today,'days remaining', delta.days)
 
DaysToEndOfYear(2020,12,20)
DaysToEndOfYear(day = 23, month =12, year = 2023)
DaysToEndOfYear()
DaysToEndOfYear(year=2020)
DaysToEndOfYear(year=2020, month=10)
DaysToEndOfYear(day=1)




'''
#- deklaracja zmiennej 
#- wyświetlenie
#- wyniki
print('----------zadanie nr 1----------')
print('-------------------------------------------------------')
print('----------zadanie nr 2----------')

 print('-------------------------------------------------------')  
 # to samo co wyżej tylko pisane przez autora kursu  

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
