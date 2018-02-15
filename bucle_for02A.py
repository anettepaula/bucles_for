#coding: utf-8
print "          DIVISORES"
x = input("Escriba un número mayor que cero: ")
y = 2
while x<0 :
	x=input("¡Le he pedido un número entero mayor que cero! ")
for i in range(1,x):
	while x%y==0 :
		print "Los divisores de",x,"son",y
		y += 1
	else :
		y +=1
print "Fintgfk"



