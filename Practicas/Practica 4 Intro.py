############################## Practica Examen #2 ##############################

################################################################################

def contar(lista):
    if isinstance(lista, list):
        return lista_aux(lista, 0, len(lista), 0)
    else:
        return "Error"

def lista_aux(lista, i, n, r):
    if i >= n:
        return r
    elif isinstance(lista[i], list):
        return lista_aux(lista, i+1, n, r) + lista_aux(lista[i], 0, len(lista[i]), 0)
    else:
        return lista_aux(lista, i+1, n, r+1)

################################################################################

def foo(x, l):
    if l == []:
        return []
    elif x == l[0]:
        return ['x'] + foo(x, l[1:])
    else:
        return [l[0]] + foo(x, l[1:])

###############################################################################

def ulam(num):
    if isinstance(num, int) and num >= 2:
        if num >= 2 and num < 5:
            return 2
        else:
            return ulam_aux(num, 2, 3, 1, 2, [], True)
    else:
        return "Error"

def ulam_aux(num, s1, s2, s, r, result, T):
    if r >= num:
        return result
    #elif r > num:
     #   return result - [r]
        #return (result[1:]) + [(r-s)]
    elif result == []:
        result = result + [r]
        return ulam_aux(num, s1, s2, s, r, result, T)
    elif T == True:
        r = r + s2
        if r > num:
            return ulam_aux(num, s1, s2, s*s2, r, result, not T)
        else:
            result = result + [r]
            return ulam_aux(num, s1, s2, s*s2, r, result, not T)
            
    else:
        s = 1
        r = r + s1
        if r > num:
            return ulam_aux(num, s1, s2, s*s1, r, result, not T)
        else:
            result = result + [r]
            return ulam_aux(num, s1, s2, s*s1, r, result, not T)

################################################################################

def insert(ref, ele, lista):
    if isinstance(lista, list):
        return aux(ref, ele, lista, 0, [])
    else:
        return "Error"

def aux(ref, ele, lista, i, r):
    if i >= len(lista):
        return r
    elif ref == lista[i]:
        r = r + [ref]
        r = r + [ele] 
        return aux(ref, ele, lista, i+1, r)
    else:
        r = r + [lista[i]]
        return aux(ref, ele, lista, i+1, r)

###############################################################################

def magia(lista):
    if isinstance(lista, list): #and largo(lista):
        return magia_aux(lista, 0, 1)
    else:
        return "Error"

def magia_aux(lista, i, j):
    if j >= len(lista):
        return "Si es un cuadro semi-magico"
    elif suma(lista[i], 0, 0) == suma(lista[j], 0, 0):
        return magia_aux(lista, i+1, j+1)
    else:
        return "Error, no es un cuadro semi-magico"

def suma(l, i, r):
    if i >= len(l):
        return r
    else:
        r = r + l[i]
        return suma(l, i+1, r)


################################################################################

def alternada(lista):
    if isinstance(lista, list):
        return prueba(lista, 0, 1)
    else:
        return "Error"

def prueba(lista, i, j):
    if j >= len(lista):
        return True
    elif (lista[i]%2 == 0) and (lista[j]%2 != 0) or (lista[i]%2 != 0) and (lista[j]%2 == 0):
        return prueba(lista, i+1, j+1)
    else:
        return False
#################################################################################

def coincide(lista):
    if isinstance(lista, list):
        return c_aux(lista, 0, 1, 0)
    else:
        return "Error"

def c_aux(lista, i, j, r):
    if j >= len(lista):
        return False
    elif r + lista[i] == lista[j]:
        return True
    else:
        r = r + lista[i]
        return c_aux(lista, i+1, j+1, r)

################################################################################
        
def invertir(lista):
    if isinstance(lista, list):
        return invertir_aux(lista, len(lista)-1, [])
    else:
        return "Error: Datos invalidos"

def invertir_aux(lista, i, r):
    if i < 0:
        return r
    else:
        if not isinstance(lista[i], list):
            return invertir_aux(lista, i-1, r +[lista[i]])
        else:
            return invertir_aux(lista, i-1, r + [invertir_aux(lista[i], len(lista[i])-1, [])])

################################################################################

def factor_primo(num):
    if isinstance(num, int):
        return primo_aux(num, 2, 3, 5, 7, 11, 13, [])
    else:
        return "Error"

def primo_aux(num, d, t, c, s, o, tr, r):
    if num == 1:
        return r
    elif num%d == 0:
        num = num/d
        r = r + [d]
        return primo_aux(num, d, t, c, s, o, tr, r)
    elif num%t == 0:
        num = num/t
        r = r + [t]
        return primo_aux(num, d, t, c, s, o, tr, r)
    elif num%c == 0:
        num = num/c
        r = r + [c]
        return primo_aux(num, d, t, c, s, o, tr, r)
    elif num%s == 0:
        num = num/s
        r = r + [s]
        return primo_aux(num, d, t, c, s, o, tr, r)
    elif num%o == 0:
        num = num/o
        r = r + [o]
        return primo_aux(num, d, t, c, s, o, tr, r)
    elif num%tr == 0:
        num = num/tr
        r = r + [tr]
        return primo_aux(num, d, t, c, s, o, tr, r)
    else:
        r = r + [num]
        num = num/num
        return primo_aux(num, d, t, c, s, o, tr, r)

################################################################################

def split(ref, lista):
    if isinstance(lista, list):
        return split_aux(ref, lista, 0, [], [])
    else:
        return "Error"

def split_aux(ref, lista, i, rp, r):
    if i >= len(lista):
        r = r + [rp]
        return r
    elif ref == lista[i]:
        #r = r + [rp]
        return split_aux(ref, lista, i+1, [], r+[rp])
    else:
        #rp = rp + [lista[i]]
        return split_aux(ref, lista, i+1, rp+[lista[i]], r)

##############################################################################

def pareja(num):
    if isinstance(num, int):
        return pareja_aux(num, 1, 0, [], [])
    else:
        return "E"

def pareja_aux(num, n, i, rp, rt):
    if i > (num-i):
        return rt
    else:
        n = n *(num-i)
        rp = rp + [[n, i]]
        rt = rt + rp
        return pareja_aux(num, 1, i+1, [], rt)

##############################################################################

def sumact(num):
    if isinstance(num, int):
        return ct_aux(num, 0, 0)
    else:
        return "Error"

def ct_aux(num, t, c):
    if num == 0:
        return [t, c]
    elif num%5 == 0:
        c = (num/5)
        num = num%5
        return ct_aux(num, t, c)
    else:
        num = num -3
        return ct_aux(num, t+1, c)

###############################################################################
