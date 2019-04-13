#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

def todos_div(num, lista):
    if isinstance(num, int) and isinstance(lista, list):
        return aux(num, lista)
    else:
        return "Error"

def aux(num, lista):
    if lista == []:
        return True
    elif (lista[0])%num == 0:
        return aux(num, lista[1:])
    else:
        return False

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

def iota(num):
    if isinstance(num, int):
        return aux(num, 0)
    return ""

def aux(num, n):
    if n == num:
        return []
    else:
        return [n] + aux(num, n+1)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

def notas(lista):
    if isinstance(lista, list):
        print("Aprobaron-Reprobaron")
        return auxa(lista), auxr(lista)#, "Promedio" auxp(lista)
    return ""

def auxa(lista):
    if lista == []:
        return 0
    elif (lista[0]) >= 70:
        return 1 + auxa(lista[1:])
    else:
        return auxa(lista[1:])

def auxr(lista):
    if lista == []:
        return 0
    elif (lista[0]) < 70:
        return 1 + auxr(lista[1:])
    else:
        return auxr(lista[1:])

#def auxp(lista):
 #   if lista == []:
  #      return prom

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

def cuenta(lista):
    if isinstance(lista, list):
        return aux(lista)
    else:
        return ''

def aux(lista):
    if lista == []:
        return 0
    elif lista[0] == list:
        (len(lista[0])) + aux(lista[1:])
    else:
        return 1 + aux(lista[1:])

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
