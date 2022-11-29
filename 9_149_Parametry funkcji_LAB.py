# program parametry funkcji LAB

print('----------zadanie nr 1A----------')
print('-------------------------------------------------------')
def PrintAnimal(animal):
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

#więcej fajnych obrazków znajdziesz np tu: https://www.asciiart.eu/

print('----------zadanie nr 1B----------')
print('-------------------------------------------------------')
def PrintAnimal(animal):
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
 
    if animal == 'cat':
        print(txt_cat)
    elif animal == 'bear':
        print(txt_bear)
    elif animal == 'bat':
        print(txt_bat)
    else:
        print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animal)
    
    return
 
 
PrintAnimal('cat')
PrintAnimal(animal='bear')
PrintAnimal(animal='bat')
PrintAnimal('unicorn')
print('----------zadanie nr 2A----------')
print('-------------------------------------------------------')
def DaysToEndOfYear(year, month, day):
    #Days To End Of Year
    from datetime import date
    date_today = date(year, month, day)
    current_year = date_today.year
    date_end_year = date(current_year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)
    return

DaysToEndOfYear(2022, 1, 1)
DaysToEndOfYear( month=1, day=2, year=2022)
print('----------zadanie nr 2B----------')
print('-------------------------------------------------------')
def DaysToEndOfYear(year, month, day):
    from datetime import date
 
    date_today = date(year,month,day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)
 
DaysToEndOfYear(2020,12,20)
DaysToEndOfYear(2021,12,21)
DaysToEndOfYear(year = 2022, month = 12, day = 22)
DaysToEndOfYear(day = 23, month =12, year = 2023)



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
