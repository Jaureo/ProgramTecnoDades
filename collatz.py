import math
l = []
#demanar nombre (?llista)
passos = 0
nombre = float(input("insert number: "))
l=[nombre]
#miram si a != 1 (iteració final)
while (nombre != 1):
    
    if nombre % 2 == 0:
        nombre = nombre/2
    else:
        nombre = nombre*3 +1
        l.append(nombre)
        passos +=1

print ("Passos = " + str(passos))
print (l)
