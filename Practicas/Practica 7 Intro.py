

##########################################################################

def vector_ascendente(vector):
    if not isinstance(vector, list):
        return "Error"
    n = 0
    i = 1
    while i < len(vector):
        if vector[n] <= vector[i]:
            n = n+1
            i = i+1
        else:
            return False
    return True

########################################################################

def repetidas(f1, f2):
    if not isinstance(f1, str) or not isinstance(f2, str):
        return "Error, debe ingresar un string."
    a = f1.split()
    b = f2.split()
    r = 0
    p = len(a)
    n =  0
    while n < p:
        for i in b:
            if a[n] == i:
                r = r+1
        n = n+1
    return r

#######################################################################

def horizontal(matriz):
    if not isinstance(matriz, list) or len(matriz) < 2:
        return "Error"
    r = []
    n = len(matriz) - 1
    while n >= 0:
        r = r + [matriz[n]]
        n = n-1
    return r

######################################################################

def diagonal(matriz):
    if not isinstance(matriz, list) or len(matriz) != len(matriz[0]):
        return "Error"
    i = 0
    j = 0
    r = []
    p = len(matriz)
    while i < p:
        r = r + [matriz[i][j]]
        i = i+1
        j = j+1
    return r

####################################################################

def upar(lista):
    if not isinstance(lista, list):
        return ""
    for i in lista:
        if i%2 == 0:
            r = i
    return r

###################################################################

def transpuesta(matriz):
    if not isinstance(matriz, list):
        return "Error"
    i = 0
    j = 0
    r = []
    rt = []
    while j < len(matriz[0]):
        if i >= len(matriz):
            i = 0
            j = j+1
            rt = rt + [r]
            r = []
        else:
            r = r + [matriz[i][j]]
            i = i+1
    return rt

################################################################

def multiplicar(vector, matriz):
    if not isinstance(matriz, list) or not isinstance(vector, list) or len(vector) != len(matriz):
        return "Error"
    i, j, r, rt, k = 0, 0, 0, [], (len(matriz))
    while i < k:
        if j >= len(matriz[0]):
            i = i+1
            j = 0
            rt = rt + [r]
            r = 0
        else:
            r = r + (vector[j]*matriz[i][j])
            j = j+1
    return rt

#################################################################

def trian_superior(matriz):
    if not isinstance(matriz, list) or len(matriz) != len(matriz[0]):
        return "Error"
    i, j, n = 0, 0, len(matriz)
    while i < n:
        if i <= j:
            if matriz[i][j] == 0:
                return False
            else:
                i = i+1
                j = 0
        else:
            if matriz[i][j] == 0:
                j = j+1
            else:
                return False
    return True

##################################################################

def unir_ordenar(vector1, vector2):
    if not isinstance(vector1, list) or not isinstance(vector2, list):
        return "Error"
    r = vector1 + vector2
    if vector_ascendente(r):
        return r
    i, j, n = 0, 1, len(r)
    while not vector_ascendente(r):
        if j >= n:
            i, j = 0, 1
        if r[i] > r[j]:
            c = r[j]
            r[j] = r[i]
            r[i] = c
            i, j = i+1, j+1
        else:
            i, j = i+1, j+1
    return r

#############################################################
    
