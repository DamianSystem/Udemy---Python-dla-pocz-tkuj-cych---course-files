marketing = ['loyality program', 'client promotion', 'market research']

print(marketing)

ListMarketing = list(marketing)
ListMarketing.append('public relations')
marketing = ListMarketing.copy()
 
print(marketing)

print(marketing[2])

ListMarketing.insert(1, 'investor relations')
print(marketing)

emailMarketing = marketing.copy()

print(emailMarketing) #- do spawdzenia punkt 5

temp = list(emailMarketing)
temp.sort()
emailMarketing = tuple(temp)
print(emailMarketing)

internalEmails = ['internal communication']
print(internalEmails )
temp = list(emailMarketing)
temp.extend(internalEmails)
print(temp)
print(type(temp))
emailMarketing = tuple(temp)
print(emailMarketing)


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
