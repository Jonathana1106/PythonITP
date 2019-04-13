'''

Profesor: Eduardo Canessa Montero
Alumno: Jonathan Alberto Guzman Araya
Carnet: 2013041216
Curso: Introduccion a la programacion
Quiz #7

'''

#JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ#
#JJJJJJJJJJJJJJJJJJJJJJJJJJJ Mayores JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ#

def mayores(matriz):
    if isinstance(matriz, list):
        return maux(matriz, 0, 0, 1, 0, [])
    else:
        return "Error"

def maux(matriz, f, i, j, r, v):
    if f > len(matriz):
        return v
    elif i == len(matriz[0]) or j >= len(matriz[0]):
        return maux(matriz, f+1, 0, 1, r, v + [r])
    elif matriz[f][i] > matriz[f][j]:
        return maux(matriz, f, i, j+1, r, v)
    else:
        return maux(matriz, f, i+1, j+1, r+1, v)

#JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ#
#JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ#

#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA#
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA Iguales AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA#

def iguales(num):
    if not isinstance(num, int):
        return "Error"
    n = len(str(num))-1
    while num > 9:
        if (num)//(10**n) == num%10:
            return True
        else:
            return False
    return "El numero es de un solo digito por lo tanto su digito mas significativo es igual a menos significativo."

#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA#
