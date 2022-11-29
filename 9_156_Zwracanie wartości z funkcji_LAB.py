# program Zwracanie wartości z funkcji LAB

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
    
        info = True
    elif animal == 'bear':
        txt = r'''    
        /  \.-"""-./  \
        \    -   -    /
         |   o   o   |
         \  .-'"'-.  /
          '-\__Y__/-'
             `---`'''
        info = True
    elif animal == 'bat':
        txt = r'''
           /\                 /\
          / \'._   (\_/)   _.'/ \
         /_.''._'--('.')--'_.''._\
         | \_ / `;=/ " \=;` \ _/ |
          \/ `\__|`\___/`|__/`  \/
                  \(/|\)/       '''
        info = True
    else:
        message = "Cannot print '%s'. Correct values for the parameter are: cat, bear, bat"
        print(message%(animal))
        info = False
        return info
    
    print(txt)
    return info




item = PrintAnimal('cat')
print(item,'-------------------------------------------------------')
print(PrintAnimal('bear'),'-------------------------------------------------------')
print(PrintAnimal('bat'),'-------------------------------------------------------')
print(PrintAnimal('Bat'),'-------------------------------------------------------')
print(PrintAnimal(),'-------------------------------------------------------')
#więcej fajnych obrazków znajdziesz np tu: https://www.asciiart.eu/

print('----------zadanie nr 1A----------')
print('-------------------------------------------------------')

def PrintAnimal(animal = ''):
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
        return False
    
    return True
 
 
if PrintAnimal():                        #* test danej funkcji przydatny przy nie znanych funkcjach
    print('The parameter was correct')   #*
else:                                    #*
    print('The parameter was INCORRECT') #*
 
 
if PrintAnimal('dog'):
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')
 
 
if PrintAnimal('bat'):
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')


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
    
    return delta.days


print('Counting from ', date.today(),'days remaining', DaysToEndOfYear())
print('Counting from ', 2022, 1, 1,'days remaining', DaysToEndOfYear(2022, 1, 1))
print('Counting from ',' month=1, day=2, year=2022','days remaining', DaysToEndOfYear(month=1, day=2, year=2022))





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
