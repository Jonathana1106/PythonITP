##################################################################

def todos_div(num, lista):
    if not isinstance(lista, list) or not isinstance(num, int):
        return "Error"
    for i in lista:
        if i%num != 0:
            return False
    return True

#################################################################

def iota(num):
    if not isinstance(num, int):
        return "Error"
    l = []
    for i in range(0, num):
        l = l + [i]
    return l

#################################################################

def notas(lista):
    if not isinstance(lista, list):
        return "Error"
    a = 0
    r = 0
    p = 0
    for i in lista:
        if i >= 70 and i <= 100:
            a = a + 1
        else:
            r = r + 1
        p = p + i
    p = p/(len(lista))
    return {"Aprobados": a, "Reprobados": r, "Promedio": p}

################################################################

def upar(lista):
    if not isinstance(lista, list):
        return "Error"
    u = 3
    for i in lista:
        if i%2 == 0:
            u = i
    if u != 3:
        return u
    else:
        return "La lista no contiene numeros pares"

###############################################################

def ulam(num):
    if not isinstance(num, int):
        return "Error"
    l = []
    while num != 1:
        if num%2 == 0:
            num = num/2
            l = l + [num]
        else:
            num = (num*3)+1
            l = l + [num]
    return l

#################################################################

def invertir(lista):
    if not isinstance(lista, list):
        return "False"
    n = len(lista)-1
    l = []
    while n >= 0:
        l = l + [lista[n]]
        n = n -1
    return l

################################################################

##def elementos(lista):
##    if not isinstance(lista, list):
##        return "Error"
##    n = 0
##    for i in lista:
##        if isinstance(i, list):
##            return elementos(i) + ele
##        else:
##            n = n+1
##    return n

################################################################


