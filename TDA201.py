#ingreso de datos en vatiables #A listo
import math

a=int(input("Ingrese el numero a :"))
b=int(input("ingrese el numero b :"))
c=int(input("Ingrese el numero c :"))


#ax^2+bx+c=0
#b^2-4*a*c
dis=math.pow(b,2)-(4*a*c)

print(f"El valor de dis es {dis}") #c listo

if(dis>0):
    print("la cuadraﾌ》ica tiene dos soluciones reales distintas")
    x1 = float((-b + (math.sqrt(dis)))/(2*a))
    x2 = float((-b - (math.sqrt(dis)))/(2*a))
    print(f"El valor de x1 es {x1}")
    print(f"El valor de x2 es {x2}")

elif(dis==0):
    print("La cuadratica tiene una solucion real repetida")
elif(dis<0):
    print("Ninguna de las soluciones son nuﾌ［eros reales")


