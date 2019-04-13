#################################Ejercicios###############################
#################################Factorial################################

def factorial(num):
    while num > 0:
        if num == 1:
            return 1
        else:
            return num*factorial(num -1)

##########################################################################
        
#################################Fibonacci################################
def fibonacci(num):
    while num >= 0:
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return (fibonacci(num - 1) + fibonacci(num - 2))
        
##########################################################################

def eliminar(num, lista):
    if isinstance(lista , list):
        return auxl(num, lista, 0)
    else:
        return "Error:

def auxl(num, lista, i):
    if
    
            
