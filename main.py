import random
import os, sys

if os.name == "posix":
  v="clear"
elif os.name == "ce" or os.name =="nt" or os.name == "dos":
  c="cls"

def ns(c):
  while c!=("s") and c!=("n"):
    print(chr(7));c=input("escribe solo \'n\' o \'s\' según la opción: ")
    return(c)
n=1
max=99
def OKI(n):
  try: 
    n=int(n)
  except:
    n=OKI(input("No válido"))
  return n
def limites (n,max):
  while n<0 or n>max:
    n=OKI(input("Error"))
  return n
  
def sing_plu(f):
  if f>1:
    co=("Intentos")
  else:
    co=("Intento")
  return co
  
while True:
  print("JUEGO ADIVINA UN NÚMERO")
  print("")
  print("""Escoja nivel de dificultad:
Nivel1: entre 0 y 100
Nivel2: entre 100 y 1000
Nivel3: entre 1000 y 10000
Nivel4: entre 10000 y 100000""")
  level = OKI(input("Escriba su opción <de 1 a 4>:"))
  print("")
  while level<1 or level>4:
    level= OKI(input("Escriba un número entre 1 y 4:"))

max=(level +1)
Di=("0 y "+ str(max))
num_e=random.randint(0,max)

int=0
tnum=limites(OKI(input("escribe un número entre"+Di+":")),max)
dif=abs(tnum=num_e)
num_a=tnum
int+=1
repes=1

while tnum!=num_e:
  tnum=(limites(OKI(input("Escribe un numero entre"+Di+":"))))
  if abs(tnum-num_e)>0:
    if tnum!=num_a:
      if (abs(tnum-num_e))<dif:
        print("Estas muy cerquita")
      else:
        print("Te alejas")
      repes=1
    else:
      respes+=1
      print("Has puesto el mismo num",repes,"veces seguidas")

  dif= abs(tnum-num_e)
  num_a=tnum
  int+=1
  if int==(max/2):
    print("Loser")
    print("la solución es",num_e)
    break
  if tnum==num_e:
    print("Winner!")
    print("Has ganado en",int,sing_plu(int))
  conti=ns(input("Otra vez:"))
  if conti==("n"):
    break
  os.system(v)