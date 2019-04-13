'''

Profesor: Eduardo Canessa Montero.
Alumno: Jonathan Alberto Guzman Araya.
Carnet: 2013041216.
Curso: Introduccion a la programacion.
Quiz #5.

'''

#ᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯ#
#Entradas: Recibe una lista de numeros.
#Restricciones: Que la lista contenga numeros y no otro tipo de dato.
#Salidas: Retorna una lista con listas que dependen de que el numero
#de la derecha sea mayor que el de la izquierda si es asi entonces formara una
#lista hasta que esto no se cumpla, y entonces comezara a forma una nueva lista.

def natural(lista): # Se crea la funcion 'natural'.
    # CORRECCION: Se quita el 'isinstance' ya que este no hace ninguna
    #validacion (dedazo).
    if isinstance(lista, list) and valida(lista): # Se establecen las
        #restricciones.
        return natural_aux(lista, 0, 1, len(lista), [], []) # Si cumple las
    #condiciones llama a una funcion auxiliar.
    else:
        return "Error, debe introducir una lista de numeros" # Sino,
    #retorna un mensaje de error.
    

def natural_aux(lista, i, j, n, ri, rt): # Se crea la funcion auxiliar.
    # CORRECCION: Se cambia 'i' por 'j'. Ya que el 'i' no es la terminacion
    #correcta de la funcion porque 'j' va a tener un valor fuera de la lista en
    #el momento en que i >= n.
    if j >= n: # Condicion de parada.
        # CORRECCION: Se agrega [[lista[i]]]. Ya que sin esto se deja el ultimo
        #elemento de la lista por fuera de la nueva lista creada.
        return rt + [[lista[i]]] # Retorna el resultado final.
    elif lista[i] < lista[j]: # Si el elemento 'i' es menor que 'j'.
        return natural_aux(lista, i+1, j+1, n, ri + [lista[i]], rt) # Retorna la
    #funcion auxiliar con el 'i' y 'j' aumentados en 1 y con 'ri' tomando el
    #elemento 'i' y formando una lista.
    else: # Sino
        ri.append(lista[i]) # 'ri' toma el ultimo valor 'i' evaluado.
        return natural_aux(lista, i+1, j+1, n, [], rt + [ri]) # Retorna la funcion
    #auxuliar con 'i' y 'j' aumentados en 1 y con 'ri' como una lista vacia y a
    #'rt' se se suma el valor que tenia 'ri' (lista que habia creado). 

def valida(lista): # Se crea la funcion que valida que la lista contenga solo '#'
    if isinstance(lista, list): 
        if lista == []:
            return "Error"
        else:
            return valida_aux(lista, 0, len(lista)) # Llama a la funcion recursiva
    else:
        return "Error"

def valida_aux(lista, i, n): # Valida que cada elemento de la lista sea un numero
    if i >= n: # Si todos son numeros retorna verdadero
        return True
    elif isinstance(lista[i], int) or isinstance(lista[i], float):
        return valida_aux(lista, i+1, n)
    else:
        return False # Sino retorna falso.

#ᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯᵯ#

#ᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺ#
#Entradas: Recibe un numero.
#Salidas: Retorna la raiz cubica de dicho numero.
#Restrcciones: Que el dato de entrada sea un  numero.

def raiz3(y): # Se crea la funcion 'raiz3'.
    #CORRECCION: Se cambia que el numero sea entero o real ya que eso es lo
    #que solicita el ejecricio.
    if isinstance(y, int) or isisntance(y, float): # Se establecen las restricciones.
        if y == 0 or y == 1 or y == 1: # Casos sencillos en los que se hace mas
            #eficiente el programa y se ahorra espacio en la memoria.  
            return y # Si cumple lo anterior retorna 'y'.
        else: # Sino.
            return raiz_aux(y, 1) # Llama la funcion auxiliar.
    else: # Sino.
        return "Error" # Retorna un mensaje de error.

def raiz_aux(y, ri): # Se crea la funcion auxiliar 'raiz_aux'.
    #CORRECCION: Se agrega 'abs' y se cambia 'ri - 3.02658' ya que es un caso
    #esclusivo y unico para raiz de '28' y no para cualquier numero.
    if abs(y -(ri**3)) <= 0.00001: # Se crea la condicion para el resultado.
        return ri # Retorna el resultado.
    else: # Sino.
        #CORRECCION: Se quita 'ri*' y nada mas se deja la formula.
        return raiz_aux(y, ((1/3)*((2*ri)+(y/(ri**2))))) # Retorna la funcion
    #auxiliar hasta que se cumpla la condicion de parada.

#ᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺᵺ#
