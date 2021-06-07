print("Funciones: Sumar, Restar, Multiplicar, Dividir")
a=input("Selección de función: ")
n1=int(input("Número 1: "))
n2=int(input("Número 2: "))

suma=(n1)+(n2)
resta=(n1)-(n2)
multiplicacion=(n1)*(n2)
division=(n1)/(n2)

b="Sumar"
c="Restar"
d="Multiplicar"
e="Dividir"

if a==b:
  print("Resultado",suma)
elif a==c:
  print("Resultado",resta)
elif a==d:
  print("Resultado",multiplicacion)
elif a==e:
  print("resultado",division)