
#Gerardo Arturo Valderrama Quiroz
#A01374994



#Ejercicio 1 even or odd

num = int(raw_input("Escribe un  mumero "))
check = int(raw_input ("Escrive un numero con el que dividir "))

if num%2 == 0:
    print str(num) + " es un numero par"
else :
    print str(num) + " es un numero impar"
if num%4 == 0:
    print str(num) + " es un multiplo de 4"
else:
    print str(num) + " no es un multiplo 4"
if num%check == 0:
    print str(num) + " es exactamente dividible por " + str(check)
else:
    print str(num) + " no es exatamente divisible por " + str(check)
    
                   
                
#Ejercicio2
print ""
print ""
print "Comienza el ejercicio 2"
print ""

p1=raw_input("Escribe tu nombre ")
p2=raw_input("Escribe tu nombre ")
cp1=raw_input("Selecciona piedra, papel o tijeras " + p1 + " ")
cp2=raw_input("Selecciona piedra, papel o tijeras " + p2 + " ")

if cp1 == "tijeras":
    if cp2 == "tijeras":
        print "Es un empate"
    if cp2 == "papel":
        print "Tijeras le gana a papel, Gana " + p1
    if cp2 == "piedra":
        print "Piedra le gana a tijeras, Gana " + p2
    
if cp1 == "piedra":
    if cp2 == "piedra":
        print "Es un empate"
    if cp2 == "tijeras":
        print "Piedra le gana a tijeras, Gana " + p1
    if cp2 == "papel":
        print "Papel le gana a piedra, Gana " + p2
    
if cp1 == "papel":
    if cp2 == "papel":
        print "Es un empate"
    if cp2 == "piedra":
        print "Papel le gana a piedra, Gana " + p1
    if cp2 == "tijeras":
        print "Tijeras le gana a papel, Gana " + p2

#Ejercicio 3
print ""
print ""
print "Comienza el ejercicio 3"
print ""

string_a = raw_input("Escribe una lista ")
a = string_a.split() 
a = [int(a) for a in a] 
b=[]

for x in a:
    if x%2 == 0:
        b.append(x)

print b

#Ejercicio 4
print ""
print ""
print "Comienza el ejercicio 4"
print ""    

string_c = raw_input("Escribe una lista ")
c = string_c.split() 
c = [int(c) for c in c] 
d=[]

lim= int(raw_input("De esa lista quieres lo valores menores a que numero "))
for x in c:
    if x <= 0:
        d.append(x)
print d


#Ejercicio 5
print ""
print ""
print "Comienza el ejercicio 5"
print ""  

string_l1 = raw_input("Escribe una lista ")
l1 = string_l1.split() 
l1 = [int(l1) for l1 in l1]

string_l2 = raw_input("Escribe otra lista ")
l2 = string_l2.split() 
l2 = [int(l2) for l2 in l2] 

l3=[]

for x in l1:
    if x in l2:
        if x not in l3:
            l3.append(x)
print "The common numbers are " + str(l3)




