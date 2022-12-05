#Hora
h = int(input("escriu una hora:"))
#Minut
m = int(input("escriu un minut:"))
#Segon
s = int(input("escriu un segon:"))

#Comprovar que no és major
if h > 24:
    print (h,"no és una hora")
if m > 60:
    print (m,"no és un minut")
if s > 60:
    print (s,"no és un segon")

#Sumar i calcular
s = s+1
if s >= 60:
    s = 0
    m = m+1

if m >= 60:
    m = 0
    h = h+1

if h >= 24:
    h = 0


#Donam temps actualitzat
def formataDos(x):
    if (x < 10):
        return '0'+ str(x)
    else:
        return str(x)
print (formataDos(h) + ':' + formataDos(m) + ':' + formataDos(s))
