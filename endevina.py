import random
x = random.randint(1,100)
print ("Adivina es numero")
y = int(input())
while (y!=x):
    if (x > y):
        print ("És numero es més gran ")
    else:
        print ("es numero es més petit ")
    y = int(input())
if (y == x):
    print ("És correcte")
