# program  Funkcje - własna implementacja SWITCH



function (argument){ # ta funkcjonalność nie jest dostępna w Pythonie
    switch(argument) { # funkcja case otrzymuje argument i dopasowywuje go do jednej z możliwości
        case 0:
            return "lundi";
        case 1:
            return "mardi";
        case 2:
            return "mercredi";
        case 3:
            return "jeudi";
        case 4:
            return "vendredi";
        case 5:
            return "samedi";
        case 6:
            return "dimanche";
        default:
            return "! error !";
    };
};

def WeekDayInFrench(dayNumber): # wykonanie funkcji case w Python
    
    names = {  # obiekt dictionary
        0: "lundi",
        1: "mardi",
        2: "mercredi",
        3: "jeudi",
        4: "vendredi",
        5: "samedi",
        6: "dimanche"
    }

    return names.get(dayNumber,"error") #ze słownika ma zostaać pobrana wartość ze zmiennej name, jeżeli nie ma takiej wartości zwraca error

print(WeekDayInFrench (4))
print(WeekDayInFrench (8))

'''
#- deklaracja zmiennej 
#- wyświetlenie
#- wyniki
print('----------zadanie nr 1----------')
print('------------------------------------------

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
