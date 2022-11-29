# program Funkcje_zmienna ilość parametrów LAB

print('----------zadanie nr 1A----------')
print('-------------------------------------------------------')
def PrintAnimal(*animals):
    print(animals)
    for animal in animals:
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
            txt = ''
        print(txt)
    return 




item = PrintAnimal('cat','bear','bat','Bat')
print(item,'-------------------------------------------------------')

print('----------zadanie nr 1B----------')
print('-------------------------------------------------------')
def PrintAnimal(*animals):
    # this function prints a cat, bear or bat ascii-art
    txt_cat = r'''
|\---/|
| o_o |
 \_^_/'''
    txt_bear = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''
    txt_bat = r'''
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/  
     '''
 
    for animal in animals:
        if animal == 'cat':
            print(txt_cat)
        elif animal == 'bear':
            print(txt_bear)
        elif animal == 'bat':
            print(txt_bat)
        else:
            print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animal)
    
    return 
 
PrintAnimal('cat','bat')
print('-------------------------------------')
PrintAnimal('cat','bat','dog','bear')
print('-------------------------------------')
PrintAnimal()


print('----------zadanie nr 2A----------')
print('-------------------------------------------------------')
from datetime import date

def DaysToEndOfYear(*Dates):
    #Days To End Of Year
    for date_one in Dates:
        #print(date_one)
        print(type(date_one))
        year=date_one.year # wywołnie roku z datetime.date
        print(year)
        date_end_year = date(year, 12, 31)
        print(date_end_year)
        delta = date_end_year - date_one
        print('Counting from ', date_one,'days remaining',delta)
        
    return 


DaysToEndOfYear(date.today(), date(2020, 1, 1), date(2019, 2, 1))

print('----------zadanie nr 2B----------')
print('-------------------------------------------------------')
from datetime import date
 
def DaysToEndOfYear(*dates):
 
    for date_today in dates:
        
        date_end_year = date(date_today.year, 12, 31)
        delta = date_end_year - date_today
        print('Date', date_today, 'days to end of year', delta.days)
 
DaysToEndOfYear(date(1999,1,15))
print('----------------')
DaysToEndOfYear(date(1999,1,15),date(2009,1,15))
print('----------------')
DaysToEndOfYear(date(1999,1,15),date(2009,1,15),date(2019,1,15))
print('----------------')
DaysToEndOfYear(date(1999,1,15),date(2009,1,15),date(2019,1,15),date.today())


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
