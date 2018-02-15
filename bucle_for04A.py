#coding: utf-8
print "       MAYORES QUE EL PRIMERO"
x = input("¿Cuantos valores vas a introducir? ")
while x<0 :
	print "Imposible"
	x = input("¿Cuantos valores vas a introducir? ")
num = input("Escriba un número: ")
for i in range(1,x):
	num2 = input("Escriba un número más grande que " +str(num)+": ")
	while num2<num :
		print "¡"+str(num2)+" no es mayor que "+str(num)+"!"
		num2 = input("Escriba un número más grande que " +str(num)+": ")
		
print "Fin"
	
