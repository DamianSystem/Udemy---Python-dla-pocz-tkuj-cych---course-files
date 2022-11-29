
musclePain = False
fever = False
weakness = False


print("suspicion of influenza" if (musclePain and fever and weakness) else "The flu is unlikely")
print("Just take a rest!" if (weakness and (not fever or not musclePain)) else "you may be cold")


isMan = True
print("suspicion of influenza" if (musclePain and fever and weakness) else ("suspicion of influenza" if (isMan and(musclePain or fever or weakness)) else "The flu is unlikely" ))
#- reszte przekopiować





isCheckCompleted = True
print("CHECK IS COMPLETED" if isCheckCompleted else "CHECK NOT DONE YET!")

#rozwiązania Udemy --------

musclePain = False
fever = True
weakness = True
if musclePain and fever and weakness:
    print("suspicion of influenza")
else:
    print("The flu is unlikely")
if musclePain and fever and weakness:
    print("suspicion of influenza")
elif not (musclePain and fever) and weakness:
    print("Just take a rest!")
else:
    print("you may be cold")
isMan = True
if musclePain and fever and weakness or  isMan and (musclePain or fever or weakness):
    print("suspicion of influenza")
elif not (musclePain and fever) and weakness:
    print("Just take a rest!")
else:
    print("this only cold")
 
 
 
 
 
 
isCheckCompleted = False
 
print("CHECK IS COMPLETED" if isCheckCompleted else "CHECK NOT DONE YET!")



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
