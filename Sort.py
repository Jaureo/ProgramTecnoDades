x = int(input("Escriu un numero des 1 a nes 3 i mira si guanyes!!: "))
import random
y = random.randint(1, 3)
if x == y:
  print ("Has guanyat uan felicitació")
if x > 3:
  print ("Aquest numero no val")
if x < 1:
  print ("Aquest numero no val")
if x > y:
  print ("Has perdut contra una maquina")
if x < y:
  print ("Has perdut contra una maquina")
print ("Es numero correcte era:", y)
