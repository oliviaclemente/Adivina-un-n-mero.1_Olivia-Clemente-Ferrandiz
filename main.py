numero=60
control=0
int=1

while True:
  print("JUEGO ADIVINA UN NÚMERO")
  print("""Escoja nivel de dificultad:
Nivel1: entre 0 y 100
Nivel2: entre 100 y 1000
Nivel3: entre 1000 y 10000
Nivel4: entre 10000 y 100000""")
  level = OKI(input("Escriba su opción <de 1 a 4>:"))
  while level!=1 and level!=2 and level!=3 and level!=4:
    level= OKI(input("Escriba un número entre 1 y 4:"))
def OKI(n):
  try: 
    n=int(n)
  except:
    n=OKI(input("No válido"))
  return n
  
while (control==0):
  print("Adivina el número;", int)
  print("Añade un número:")
  num = int(input())
  if (num==numero):
    print("Gnador!!")
    print("FIN")
    control=1
  elif (num > numero):
    print("Intentalo con un número más pequeño:")
    int +=1
  elif (num < numero):
    print("Intentalo con un número más grande:")
    int +=1
