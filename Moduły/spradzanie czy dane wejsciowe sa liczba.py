# program  wprowadzanie danych przez użytkownika 

def check_int(s):   # sprawdzenie czy dane wejściowe są liczbą
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()
 
