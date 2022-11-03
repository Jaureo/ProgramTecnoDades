import random
x = random.randint(1,100)

print ("Adivina es numero")
y = int(input())

torn = 1
llista = []

while (y!=x):
    torn += 1
    if (x > y):
        print ("És numero es més gran ")
    else:
        print ("es numero es més petit ")
    llista.append(y)    
    y = int(input())

if (y == x):
    print ("És correcte")
    print(llista)
    
#Created by Joan Miquel :p
