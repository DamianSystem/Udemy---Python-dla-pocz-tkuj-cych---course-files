article = '''Monty Python (also collectively known as the Pythons)[2][3] were a British surreal comedy troupe who created the sketch comedy television show Monty Python's Flying Circus, which first aired on the BBC in 1969. Forty-five episodes were made over four series. The Python phenomenon developed from the television series into something larger in scope and influence, including touring stage shows, films, albums, books and musicals. The Pythons' influence on comedy has been compared to the Beatles' influence on music.[4][5][6] Regarded as an enduring icon of 1970s pop culture, their sketch show has been referred to as being "an important moment in the evolution of television comedy".[7]

Broadcast by the BBC between 1969 and 1974, Monty Python's Flying Circus was conceived, written and performed by its members Graham Chapman, John Cleese, Terry Gilliam, Eric Idle, Terry Jones, and Michael Palin. Loosely structured as a sketch show, but with an innovative stream-of-consciousness approach aided by Gilliam's animation, it pushed the boundaries of what was acceptable in style and content.[8][9] A self-contained comedy team responsible for both writing and performing their work, the Pythons had creative control which allowed them to experiment with form and content, discarding rules of television comedy. Following their television work, they began making films, including Monty Python and the Holy Grail (1975), Life of Brian (1979) and The Meaning of Life (1983). Their influence on British comedy has been apparent for years, while in North America, it has coloured the work of cult performers from the early editions of Saturday Night Live through to more recent absurdist trends in television comedy. "Pythonesque" has entered the English lexicon as a result.'''
print(article.upper()) 
print(article.lower().replace('monty','flying'))#-4
print(article.split(' ')) #-5
print('word python appears',article.lower().count('python'),'times')
print('to print the \\ you need to put \\ twice in your text like this: ','\\', sep='\\')#-7
print('The best hits of \'80s!!!') #-8
print("The best hits of '80s!!!")  #-8

amountPLN = 234
exchaneUSD = 3.65
exchaneEUR = 4.23
amountUSD = amountPLN / exchaneUSD
print('cur', 'exchange','amount', sep="\t")
print('USD', exchaneUSD, '', amountUSD, sep="\t") #-9
print('EUR', exchaneEUR, '', amountPLN/exchaneEUR, sep="\t") #-9
ValueAsText='123.45'
factor=1.23
print('value is ', ValueAsText, 'factor is',  factor ,'value*factor=',  factor*float(ValueAsText))

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
                               #- 
                               #- 
