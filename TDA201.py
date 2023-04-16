#ingreso de datos en vatiables
import math

a=int(input("Ingrese el numero a :"))
b=int(input("ingrese el numero b :"))
c=int(input("Ingrese el numero c :"))

print (a)
print (b)
print (c)

#ax^2+bx+c=0
#b^2-4*a*c
dis=math.pow(b,2)-(4*a*c)

print(f"El valor de dis es {dis}")

if(dis>0):
    print("la cuadrática tiene dos soluciones reales distintas")
elif(dis==0):
    print("La solucion cuadratica tiene 2 soluciones reales disponibles")
elif(dis<0):
    print("Ninguna de las soluciones son números reales")

if(dis>0):
    x1 = float((-b+math.sqrt(dis))/math.pow(2,a))
    x2 = float((-b - math.sqrt(dis)) / math.pow(2, a))
    print (f"El valor de x1 es {x1}")
    print(f"El valor de x2 es {x2}")

