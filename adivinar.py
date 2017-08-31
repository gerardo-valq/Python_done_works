


#Gerardo Arturo Valderrama Quiroz
#A01374994
#Start
import math

rango = int(input("Di un numero, este sera tu limite de rango para que pueda adivinar."))
print("Escoge un numero entre 1 y " + str(rango))
print("Adivinare el numero en que estas pensando")

datos = range(1,rango+1)
ndatos = len(datos)
guess = math.ceil(rango/2.0)
guess2 = math.ceil(rango/2.0)
nguess = 0

while ndatos != 1:
    answer = str(input("Tu numero es mayor, menor o igual que " + str(guess) + ", escribe mayor, menor o igual."))
    ndatos = int(ndatos)/2
    nguess = nguess + 1
    if answer == "menor" :
        guess2 =math.ceil(guess2/2.0)
        guess = math.ceil(guess - guess2)
    elif answer == "mayor":
        guess2= math.ceil(guess2/2.0) 
        guess = math.ceil(guess + guess2)
    else:
        ndatos=1
        
print("Tu numero es " + str(guess) + ". Adivine en " + str(nguess) + " intentos.")

#End
    
        
    
    



