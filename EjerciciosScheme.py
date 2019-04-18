#################################Ejercicios###############################
################################# Factorial ################################

def factorial(num):
    while num > 0:
        if num == 1:
            return 1
        else:
            return num*factorial(num -1)

def Factorial(num):
    #i = num
    r = 1
    while num > 0:
        r = r*num
        num = num - 1
    return r

##########################################################################
        
################################# Fibonacci ################################
def fibonacci(num):
    while num >= 0:
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return (fibonacci(num - 1) + fibonacci(num - 2))
        
##########################################################################

############################### Digitos ##################################
def digitos(num):
    if num < 0:
        num = num*-1
    elif num < 10 and num >=0:
        return 1
    else:
        return aux(num, 0)

def auxD(num, n):
    if num == 0:
        return n
    else:
        num = num//10
        n = n + 1
        return auxD(num, n)

##########################################################################

################################ Eliminar ################################

def eliminar(num, lista):
    if (isinstance(lista, list) and isinstance(num, int)):
        if lista == []:
            return "Lista vacia"
        else:
            return auxL(num, lista, 0, [])

    else:
        return "Error en los argumentos"

def auxL(num, lista, i, listaR):
    if i == 0 and lista[i] == num:
        return lista[1:]
    elif i == len(lista):
        return listaR
    elif lista[i] == num:
        i = i + 1
        return auxL(num, lista, i, listaR)
    else:
        listaR = listaR + [lista[i]]
        i = i + 1
        return auxL(num, lista, i, listaR)
###########################################################################

############################## QuickSort ##################################



