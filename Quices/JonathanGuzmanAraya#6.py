'''

Profesor: Eduardo Canessa Montero
Alumno: Jonathan Alberto Guzman Araya
Carnet: 2013041216
Curso: Introduccion a la programacion
Quiz #6

'''


#ŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎ#
#Entradas: Recibe una matriz.
#Restricciones: Que sea de tamaño mxm.
#Salidas: Retorna "True" en caso de que sea triangular inferior y "False" en caso contrario.

def trian_inf(matriz): # Se crea la funcion "trian_inf".
    # Se crean las restricciones.
    if isinstance(matriz, list) and (len(matriz) == len(matriz[0])):
        return ifn_aux(matriz, 0, 0) # Si las cumple llama la funcion auxiliar.
    else: # Sino retorna un mensaje de error.
        return "Error, debe ingresar una matriz mxm."

def ifn_aux(matriz, i, j): # Se crea la funcion "ifn_aux".
    if i >= len(matriz): # Condicion de parada.
        return True # Retorna "True" en cao de cumplirla.
    elif j >= len(matriz[0]): # Si 'j' es mayor que una columna de la matriz.
        ##CORRECCION## return ifn_aux(matriz, i+1, j) (falta de atencion).##
        ##Se cambia ya que 'j' inicializarse nuevamente en '0'.##
        return ifn_aux(matriz, i+1, 0) # Retorna la funcion con 'i' aumentado en 1 y 'j' se inicializa en 0.
    elif j > i: # SI 'j' es mayor que 'i'.
        if matriz[i][j] == 0: # Si el lemento [i][j] de la matriz es igual a 0.
            return ifn_aux(matriz, i, j+1) # Se retorna la funcion con 'j' aunmentado en 1.
        else:
            return False # Sino cumple lo anterior retorna "False".
    else: # SI 'i' es mayor o iguak que 'j'.
        return ifn_aux(matriz, i, j+1) # Se retorna la funcion con 'j' aumentado en 1.
    

#ŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎŎ#


#ÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂ#
#Entradas: Recibe 2 listas.
#Restricciones: La primera lista debe de contener sublistas en la cual el ultimo elemento de la sublista debe de ser un numero entero.
#Salidas: Retorna una nueva lista con la transformacion respectiva.
    
def transforma(lista, lista2): # Se crea la funcion "transforma".
    # Se establecen las restricciones necesarias.
    if (isinstance(lista, list) and isinstance(lista2, list)) and correcta(lista, 0, 2):
        # Llama la funcion auxiliar.
        return trans(lista, lista2, 0, 0, 0, 1, 2, 0, [])
    else: # Sino cumple las restricciones genera un mensaje de error.
        return "Error"

def trans(lista, lista2, i, j, z, k, n, p, r): # Se crea la funcion "trans".
    ##CORRECCION: Se cambia la condicion de parada (if z >= len(lista).
    ##Ya que no es la manera correcta porque duplica el 'r' final. 
    if lista2 == []: # Condicion de terminacion.
        return r # Retorna el valor de 'r'.
    ##CORRECCION: Se cambia 'i' por 'z' ya que es el mas adecuado para el nuevo metodo de retornar el 'r' final.
    elif z >= len(lista): # Si 'z' (subindice de las sublistas de 'lista) mas grande que su tama;o.
        r.append(lista2[i]) # 'r' toma el valor del elemento en lista2[i].
        return trans(lista, lista2[1:], i, j, 0, k, n, 0, r) # Retorna la funcion con lista2 sin el primer elemento y con z inicializado de nuevo en 0.
    elif lista[z][j] == lista2[i]: # SI el elemento lista[z][j] es igual a lista2[i].
        if p >= lista[z][n]: # SI 'p' (contador de la cantidad de elementos colocados hasta que se igual a 'n').
            return trans(lista, lista2[1:], i, j, z, k, n, 0, r) # Retorna la funcion con lista2 sin su primer elemento y con 'p' en 0.
        else: # Sino entonces a 'r' se le agrega el valor de lista[z][k] cuantas veces se indique.
            r.append(lista[z][k])
            return trans(lista, lista2, i, j, z, k, n, p+1, r) # Se retorna la funcion con 'p' aumentado en 1 ya que hemos agregado el elemento lista[z][k] una vez.
    else: # Sino se aumenta 'z' en 1.
        ##CORRECCION: Se cambia 'i+1' por 'i' el 'z+1' por 'z' y al 'r' se le omite '+lista2[i]'.
        ##Ya que no hemos terminado de hacer la evaluacion con respecto a lista.
        ##Y genera un error al evaluar 2 veces y duplicar el 'r' final al comparar en 2 ocaciones.
        return trans(lista, lista2, i, j, z+1, k, n, 0, r)

def correcta(lista, i, n): # Se crea la funcion correcta.
    if i >= len(lista): # Condicion de parada.
        return True # Retorna "True".
    elif len(lista[i]) == 3: # Evalua que siempre el contenido de las sublistas sea 3, ya que necesita 3 elementos.
        if isinstance((lista[i][n]), int): # Se evalua que el elemento 'n' sea un numero entero.
            return correcta(lista, i+1, n) # SI cumple lo anterior aumenta el 'i' en 1.
        else: # Sino retorna "False". 
            return False
    else: # Sino retorna "False".
        return False

#ÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂ#
