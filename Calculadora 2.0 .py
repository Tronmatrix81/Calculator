import math

print('En caso de raíz cuadrada "(número) sqrt"')
op=str(input("Operación: "))

x1=str("Syntax error!")

if op.find("+")>=0:
  x=op.split("+")
  x1=float(x[0])
  x2=float(x[1])
  x1+=x2
elif op.find("-")>=0:
  x=op.split("-")
  x1=float(x[0])
  x2=float(x[1])
  x1-=x2
elif op.find("*")>=0:
  x=op.split("*")
  x1=float(x[0])
  x2=float(x[1])
  x1*=x2
elif op.find("/")>=0:
  x=op.split("/")
  x1=float(x[0])
  x2=float(x[1])
  x1/=x2
elif op.find("^")>=0:
  x=op.split("^")
  x1=float(x[0])
  x2=float(x[1])
  x1=math.pow(x1,x2)
elif op.find("sqrt")>=0:
  x=op.split("sqrt")
  x1=math.sqrt(float(x[0]))

if x1=="Syntax error!":
  print(x1)
else:
  x3=int(x1)
  if x3==x1:
   print(("Resultado: {}").format(x3))
  else:
    length=len(str(x1))
    if length<=6:
      print(("Resultado: {}").format(x1))
    else:
      length2=len(("{:.2f}").format(x1))
      length-=length2
      if length<1:
        print(("Resultado: {}").format(x1))
      else:
        print("¿Desea redondear las decimales? (a 2 dígitos)")
        a=str(input())
        if a=="Yes" or a=="Si" or a=="si" or a=="yes" or a=="s" or a=="y" or a=="S" or a=="Y" or a=="1":
          print(("Resultado: {:.2f}").format(x1))
        else:
          print(("Resultado: {}").format(x1))