import random
x = random.randint(1,10)

print ("Adivina es numero")
y = int(input())

torn = 0
llista = []

while (y!=x):
    torn += 1
    if (x > y):
        print ("És numero es més gran ")
    else:
        print ("es numero es més petit ")
    llista.append(y)    
    y = int(input())
    if y in llista:
        print ("ja has posat aquest numero")

if (y == x):
    print ("És correcte")
    print(llista)

#created by Jaureo
