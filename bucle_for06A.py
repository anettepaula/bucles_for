#coding: utf-8
print "          CONTADOR DE PARES E IMPARES"
x = input("¿Cuantos valores va a introducir? ")
par = 0
impar = 0
while x<0 :
	print "¡Imposible!"
	x = input("¿Cuantos valores va a introducir?")
for i in range(1,x+1):
	num = input("Escriba el valor "+str(i)+": ")
	if num%2==0 :
		par += 1
	else :
		impar += 1
print "Ha escrito ",par," números pares y ", impar," números impares."
