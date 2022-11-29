name = 'Damian'
age = 37
daysInYear = 365

message = '%s is %d years old, so is about %d days old'
print(message % (name,age, daysInYear*age))

message = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format (name,age, daysInYear*age))

name = 'Justyna'
age = 32
print(message.format (name,age, daysInYear*age))

name = 'Chris'
age = 17
print(message.format (name,age, daysInYear*age))

a = 1234567890
b = 12345
message = '{0:d} divided by {1:d} is  {2:d} and the rest is {3:d}'
print(message.format (a,b, a//b, a%b)) 


