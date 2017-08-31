#Gerardo Arturo Valderrama Quiroz
#A01374994
#Programacion Avanzada
import math

#Ejercicio 1

print "Ejercicio 1"
print ""

numbase = 1
summ = 0

for counter in range (999):
    if (numbase%3 == 0) or (numbase%5 == 0):
        summ = summ + numbase
        numbase = numbase + 1

    else:
        numbase = numbase + 1


print "The sum of the multiples of 3 and 5 is " + str(summ)
print ""
print ""

#Ejercicio 2

print "Ejercicio 2"
print ""

numbase = 0
fibonacci = 0
fibonacci1 = 0
fibonacci2= 1
summ = 0

while (fibonacci <= 4000000):
    if (fibonacci%2 == 0):
        summ = summ + fibonacci

    fibonacci = fibonacci1 + fibonacci2
    fibonacci1 = fibonacci2
    fibonacci2 =fibonacci

print "The sum of the values below 4,000,000 of the fibonacci sequence is " + str(summ)    
print ""
print ""

#Exercise 3

print "Exercise 3"
print ""

numbase = 600851475143
i = 2

while i*i < numbase:
    while numbase%i == 0:
        numbase = numbase / i

    i = i +1

print "The largest prime factor is " + str(numbase)
print""
print""

#Exercise 4

print "Exercise 4"
print""

mult1 = 999
mult2 = 999
pal1 = 0
pal2 = 0
big = 0


while mult1 != 900:
    while mult2 != 900:
        pal1 = str(mult1 * mult2)
        pal2 = ''.join(reversed(pal1))
        if pal1 == pal2:
            if (pal1 > big):
                big = pal1
            mult2 = mult2 - 1
        else:
            mult2 = mult2 - 1

        
    mult1 = mult1 -1
    mult2 = 999

print big
print""
print""



#Exercise 6
print "Exercise 6"
print""

limit = 101
sqr = 0
summ = 0

for i in range (limit):
    summ = summ + i
    sqr = sqr + i**2

print (summ**2) - sqr
print""
print""


#Exercise 7
print "Exercise 7"
print""

maxn = 1000000
count = 0
prime = 0

for x in range (2,maxn+1):
    isPrime = True
    for y in range (2,x):
        if x%y==0:
            isPrime = False
    if isPrime:
        count = count + 1
        prime = x
        print count,
        if count == 10001:
            break
print"El numero numero primo 10001 es " +str(prime)
print""
print"" 

#Exercise 10
print "Exercise 10"
print""

maxn = 2000000
summ = 0

for x in range (2,maxn+1):
    isPrime = True
    for y in range (2,x):
        if x%y==0:
            isPrime = False
    if isPrime:
        summ = summ + x

print"La suma de los numero primos menora a 2,000,000 es " +str(summ)
print""
print""   


#Ejercicios fallidos 

#Exercise 5

#1.-dividir un numero X entre 1
#2.- Si el modulo es igual a cero entonces
    #al divisor sumarle uno y sacar el modulo, si el modulo es cero y la diviso es exacta repetir estemismo paso hasta que se cumpla 20
    #Si no es cero o es exacta, al numero x se le suma uno y se repite le proceso

#Exercise 9
print "Exercise 9"
print""

a=0
b=0
c=1000

while a != 0:
    while b!= 0:
        while c!= 0:
            summ = a + b + c
            pythc = math.sqrt(a**2 +b**2)
            print summ
            if (c == pythc)and summ == 1000 :
                print a*b*c
            else:
                c = c -1
        b=b+1
        c=1000
        print b
    a=a+1
    b=1000
    print a
            
print""
print"" 



         

















