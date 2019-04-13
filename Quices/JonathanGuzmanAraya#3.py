'''

Profesor: Eduardo Canessa Montero
Alumno: Jonathan Alberto Guzman Araya
Curso: Introduccion a la programacion
Quiz #3

'''
####################################Coincide cola##############################

def coincide(lista): # Se crea la funcion
    if isinstance(lista, list): #Condicion que para identificar si es lista o no
        if lista == []: # Condicion de que una lista vacia no sirve
            return "Error" # Mensaje de error
        else:
            return aux(lista, 0, 1, 0) # Llamada a la funcion axuliar
    return "Error" # Mensaje de error

def aux(lista, n, m, h): # Se crea la funcion auxiliar
    if n == (len(lista)-1): # 'Se corrigio al agregar un -1 al final'# Condicion de parada
        return False # Retorna resultado Falso
    elif (lista[n] + h) == lista[m]: # Condicion de validacion
        return True # Si se cumple retorna Verdadero
    else:
        h = h + lista[n] # Asignacion de valor
        return aux(lista, n+1, m+1, h) # Llamada recursiva
    
################################################################################
#################################Insertar cola##################################

def insert_d(ref, ele, lista): # Se crea la funcion
    if isinstance(lista, list): # Se evalua que sea una lista
        if lista == []: # Si la lista es nula
            return "Error" # Retorna un msj de error
        else: 
            return aux(ref, ele, lista, 0, []) # Se llama a una funcion auxiliar
    else: 
        return "Error" # Se crea un msj de error
    
def aux(ref, ele, lista, n, nlista): # Se crea la funcion auxiliar
    if n == len(lista): # Condicion de parada
        return nlista # Retorna la nueva lista
    elif ref == lista[n]: # Si la referencia y un elemento de la lista son iguales
        nlista.append(ref) #'se agrega otro append # 
        nlista.append(ele) # A la lista se le agrega el elemento que queremos
        return aux(ref, ele, lista, n+1, nlista) # Se hace recursividad de la funcion
    else: 
        nlista.append(lista[n]) # Se le agrega el elemento de comparacion
        return aux(ref, ele, lista, n+1, nlista) # Llamada recursiva de si misma

################################################################################

