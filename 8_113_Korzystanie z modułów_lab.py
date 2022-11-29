#korzystanie z modułów
print('----------zadanie nr 1A----------')
percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,

           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,

           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,

           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,

           8.740978348,6.174819567]

rob_percent = percent.copy()
print(percent)
print('-------------------------------------------------------')
print(rob_percent)
print('-------------------------------------------------------')
rob_percent.sort()
print(rob_percent)
print(len(rob_percent))
import statistics                           # modół statystyki
print(statistics.median(rob_percent))       # pokazuje mediane z dwóch środkowych wyrazów przy parzystej ilości danych lub gdy ilość nieparzysta wartość elementu w środku 
print(statistics.median_low(rob_percent))   # pokazuje mediane poniżej wyrazu środkowego (np 4 wyrazów pokaże 2 wyraz)
print(statistics.median_high(rob_percent))  # pokazuje mediane powyżej wyrazu środkowego (np 4 wyrazów pokaże 3 wyraz)

print('----------zadanie nr 1B----------')

percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,
           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,
           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,
           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,
           8.740978348,6.174819567]
 
percent.sort()
print(percent)
 
 
#this ends with error
#print(median(percent))
#print(median_low(percent))
#print(median_high(percent))
 
 
# this succeeds
import statistics
 
print(statistics.median(percent))
print(statistics.median_low(percent))
print(statistics.median_high(percent))
 
 
#this succeedes
from statistics import *
 
print(median(percent))
print(median_low(percent))
print(median_high(percent))
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
