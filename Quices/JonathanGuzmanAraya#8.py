'''

Profesor: Eduardo Canessa Montero.
Alumno: Jonathan Alberto Guzman Araya.
Carnet: 2013041216.
Curso: Introduccion a la programacion.
Quiz #8.

'''

#ʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥ#
#ʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥ#
#Entradas: Recibe una matriz.
#Restricciones: Que la matriz sea una matriz.
#Salidas: Devuelve una el reflejo vertical de la matriz ingresada.

def reflejo_v(matriz):
    if not isinstance(matriz, list):
        return "Error debe ingresar una matriz."
    n, i, j, r, rt = len(matriz), 0, len(matriz[0])-1, [], []
    while i < n:
        while j >= 0:
            r = r + [matriz[i][j]]
            j = j-1
        rt = rt + [r]
        r = [] # Se agrego esta linea.
        i = i+1
        j = len(matriz[0])-1 # Se agrego esta linea.
    return rt

#ʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥ#
#ʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥʥ#


#ʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩ#
#ʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩ#
#Entradas: Recibe un vector.
#Restrcciones: Que el vector sea de tamaño 2*n.
#Salidas: Devuelve 2 vectores de tamaño n.

def descomponer(vector):
    if not isinstance(vector, list) or (len(vector))%2 != 0:
        return "Error, debe ingresar una lista con un numero de elementos par (2*n)."
    p, s = [], []
    for i in vector:
        if i%2 == 0:
            p = p+[i]
        else:
            s = s+[i]
    return s, p # Se cambio de posicion.

#ʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩ#
#ʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩʩ#

