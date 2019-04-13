###############################################################################
###############################################################################

def vector(vec):
    if isinstance(vec, list):
        return vec_aux(vec, 0, 1)
    else:
        return "Error"

def vec_aux(vec, i, j):
    if j >= len(vec):
        return True
    elif vec[i] < vec[j]:
        return vec_aux(vec, i+1, j+1)
    else:
        return False

def vectori(vec1, vec2):
    if isinstance(vec1, list) and isinstance(vec2, list):
        return veci_aux(vec1, vec2, 0)
    else:
        return "Error"

def veci_aux(vec1, vec2, i):
    if i >= len(vec1):
        return True
    elif vec1[i] == vec2[i]:
        return veci_aux(vec1, vec2, i+1)
    else:
        return False


def matriz_s(matriz):
    if isinstance(matriz, list) and len(lista) == len(matriz[0]) and (len(matriz)%2 == 0) and (len(matriz[0])%2 == 0):
        return aux(matriz, 0, 0)
    
##############################################################################
##############################################################################

def vector_ascendente(vector):
    if isinstance(vector, list) and valida(vector, 0):
        return ascendente_aux(vector, 0, 1)
    else:
        return "Error, debe introducir una vector con datos numericos"

def ascendente_aux(vector, i, j):
    if j >= len(vector):
        return True #"El vector si es ascendente"
    elif vector[i] <= vector[j]:
        return ascendente_aux(vector, i+1, j+1)
    else:
        return False #"El vector no es ascendente"

def valida(vector, i):
    if i >= len(vector):
        return True
    elif isinstance(vector[i], int) or isinstance(vector[i], float):
        return valida(vector, i+1)
    else:
        return False

##############################################################################
##############################################################################
    
def repetidas(f1, f2):
    if isinstance(f1, str) and isinstance(f2, str):
        a = f1.split()
        b = f2.split()
        return raux(a, b, 0, 0, 0)
    else:
        return "Error"

def raux(a, b, i, j, r):
    if i >= len(a):
        return r
    elif j >= len(b):
        return raux(a, b, i+1, 0, r)
    elif a[i] == b[j]:
        return raux(a, b, i, j+1, r+1)
    else:
        return raux(a, b, i, j+1, r)
    
##############################################################################
##############################################################################

#def horizontal()               
def reflejo(matriz):
    if isinstance(matriz, list) and len(matriz) >= 2:
        return matriz_aux(matriz, len(matriz)-1, [])
    else:
        return "Error"

def matriz_aux(matriz, i, r):
    if i < 0:
        return r
    else:
        r.append(matriz[i])
        return matriz_aux(matriz, i-1, r)

############################################################################
############################################################################

def transpuesta(matriz):
    if isinstance(matriz, list) and len(matriz) >= 2:
        return taux(matriz, 0, 0, [], [])
    else:
        return "error"

def taux(matriz, i, j, rp, rt):
    if j >= len(matriz[0]):
        return rt
    elif i >= len(matriz):
        rt.append(rp)
        return taux(matriz, 0, j+1, [], rt)
    else:
        rp.append(matriz[i][j])
        return taux(matriz, i+1, j, rp, rt)

###########################################################################
############################################################################

def diagonal_mayor(matriz):
    if isinstance(matriz, list) and len(matriz) == len(matriz[0]):
        return daux(matriz, 0, 0, [])
    else:
        return "Errpr"

def daux(matriz, i, j, r):
    if i >= len(matriz):
        return r
    else:
        r.append(matriz[i][j])
        return daux(matriz, i+1, j+1, r)

###############################################################################
############################################################################

def multiplicar(vector, matriz):
    if isinstance(vector, list) and isinstance(matriz, list) and len(vector) == len(matriz[0]):
        return maux(vector, matriz, 0, 0, 0, 0, [], [])
    else:
        return "Error"

def maux(vector, matriz, i, j, n, rn, rp, r):
    if i >= len(matriz):
        return r
    elif j >= len(matriz[0]):
        r.append(rp)
        return maux(vector, matriz, i+1, 0, 0, 0, [], r)
    else:
        rn = vector[n]*matriz[i][j]
        rp.append(rn)
        return maux(vector, matriz, i, j+1, n+1, 0, rp, r)

#############################################################################
#############################################################################

def producto(A, B):
    if isinstance(A, list) and isinstance(B, list) and len(A[0]) == len(B):
        return paux(A, B, 0, 0, 0, 0, 0, [], [])
    else:
        return "Error"


def paux(A, B,  i, j, k, p, r, f, m):
    if i >= len(A):
        return m
    elif p >= len(B[0]):
        m.append(f)
        return paux(A, B, i+1, 0, 0, 0, 0, [], m)
    elif j >= len(A[0]):
        f.append(r)
        return paux(A, B, i, 0, 0, p+1, 0, f, m)
    else:
        r = r + A[i][j]*B[k][p]
        return paux(A, B, i, j+1, k+1, p, r, f, m)
#producto([[2, 0, 1], [3, 0, 0], [5, 1, 1]], [[1, 0, 1], [1, 2, 1], [1, 1, 0]])

############################################################################
############################################################################

def tsuperior(matriz):
    if isinstance(matriz, list) :
        return taux(matriz, 0, 0)
    return "Error"

def taux(matriz, i, j):
    if i >= len(matriz) :
        return True
    elif i == j:
        if matriz[i][j] == 0:
            return False
        else:
            return taux(matriz, i+1, 0)
    elif i > j:
        if matriz[i][j] == 0:
            return taux(matriz, i, j+1)
        else:
            return False

#tsuperior([[1,8,3],[0,2,4],[0,0,5]])
############################################################################
##########################################################################

def vertical(matriz):
    if isinstance(matriz, list):
        return vaux(matriz, 0, len(matriz[0])-1, [], [])
    else:
        return "Error"

def vaux(matriz, i, n, rp, rt):
    if i >= len(matriz):
        return rt
    elif n < 0:
        rt.append(rp)
        return vaux(matriz, i+1, len(matriz[0])-1, [], rt)
    else:
        rp.append(matriz[i][n])
        return vaux(matriz, i, n-1, rp, rt)

##############################################################################
##############################################################################

def maximo(vector1, vector2):
    if max(vector1) > max(vector2):
        n = max(a)
        return n
    else:
        return max(b)

################################
