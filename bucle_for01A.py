#coding: utf-8
print "                 PARES E IMPARES"
x = int(input("Escriba un numero entero: "))
y = int(input("Escriba un numero entero mayor o igual " + str(x)+" :"))
while y<x :
	y = input("¡Le he pedido un número mayor que "+str(x)+ "!")
for i in range(x,y+1) :
	if i%2==0 :
		print "El número",i,"es par."
	else :
		print "El número",i,"es impar."

