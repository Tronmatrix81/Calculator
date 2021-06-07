import math


n1=float(input("Primera cifra: "))
op=str(input("Operación (Símbolo): "))      #Interacción con el usuario
n2=float(input("Segunda cifra: "))

s="+"
r="-"
R="-"       #Definición de variables
m="x"
M="*"
d="/"
p="^"

if op==s:
  r1=n1+n2
elif op==r or op==R:
  r1=n1-n2
elif op==m or op==M:
  r1=n1*n2                #Operaciones
elif op==d:
  r1=n1/n2
elif op==p:
  if n2==0 or n2=="":
    n2=2
  r1=math.pow(n1,n2)

r2=int(r1)
if r2==r1:
  operation=r2         #Float to Integer
else:
  operation=r1

print("Resultado:",operation)     #Imprimir resultado