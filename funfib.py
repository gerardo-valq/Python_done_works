
#Gerardo Arturo Valderrama Quiroz
#A01374994

#Funcion de la secuencia fibonacci

def fibonacci(x):
    fibonacci = 0
    fibonacci1 = 0
    fibonacci2= 1
    for x in range (0,x):
        print fibonacci,
        fibonacci = fibonacci1 + fibonacci2
        fibonacci1 = fibonacci2
        fibonacci2 =fibonacci
        
        
