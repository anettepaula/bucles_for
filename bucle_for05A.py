#coding: utf-8
print "            NÚMEROS NEGATIVOS"
x = input("¿Cuantos valores va a introducir? ")
cont = 0
while x<0 :
	print "¡Imposible!"
	x = input("¿Cuantos valores va a introducir?")
for i in range(1,x+1) :
	num = input("Escriba el número "+str(i)+": ")
	if num<0 :
		cont += 1
print "Ha escrito",cont,"número(s) negativos"
	
