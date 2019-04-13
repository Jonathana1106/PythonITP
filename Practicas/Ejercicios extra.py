'''

Profesor: Eduardo Canessa Montero
Alumno: Jonathan Alberto Guzman Araya
Curso: Introduccion a la programacion '''

#############################Tarea puntos extra################################

#ħħħħħħħħħħħħħħħħħħħħħħħħħħħħ Convertir temperatura ħħħħħħħħħħħħħħħħħħħħħħħħħħ#
                                    #
def fahrenheit(Celcius):            # Se define la funcion "farenheit"
    if isinstance(Celcius, float):  # Se establece la condicion de que solo debe aceptar numeros en R
        F =  (9/5)*Celcius + 32     # A la variable 'F' se le asiga na formula para la conersion de Celcius a Farenheit
        return F                    # Se retorna la variable "F" que es la temperatura en Farenheit
    else:                                                  # Sino
        return "Debe introducir numeros pertenecientes a R"# Se retorna un msj de error
#ħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħ#

#ħħħħħħħħħħħħħħħħħħħħħħħ Convertir numeros a letras ħħħħħħħħħħħħħħħħħħħħħħħħħħ#
                              #
def convertir_a_letras(num):  # Se crea la funcion
    if num == 0:              # Si el numero es igual a 0 
        return "Cero"         # Entonces retorna 'cero'
    elif num == 1:            # Si el numero es igual a 1
        return "Uno"          # Entonces retorna 'uno'
    elif num == 2:            # Si el numero es igual a 2
        return "Dos"          # Entonces retorna 'dos'
    elif num == 3:            # Si el numero es igual a 3
        return "Tres"         # Entonces retorna 'tres'
    elif num == 4:            # Si el numero es igual a 4
        return "Cuatro"       # Entonces retorna 'cuatro'
    elif num == 5:            # Si el numero es igual a 5
        return "Cinco"        # Entonces retorna 'cinco'
    elif num == 6:            # Si el numero es igual a 6
        return "Seis"         # Entonces retorna 'seis'
    elif num == 7:            # Si el numero es igual a 7
        return "Siete"        # Entonces retorna 'siete'
    elif num == 8:            # Si el numero es igual a 8
        return "Ocho"         # Entonces retorna 'ocho'
    elif num == 9:            # Si el numero es igual a 9
        return "Nueve"        # Entonces retornav 'nueve'
    elif num == 10:           # Si el numero es igual a 10
        return "Diez"         # Entonces retorna 'diez'
    else:                     # Sino
        return "Introduzca un numero valido '[0,10]'" # Retorna un msj de error
                              #
#ħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħ#

#ħħħħħħħħħħħħħħħħħħħħħħħħħħħħ Pendiente de una recta ħħħħħħħħħħħħħħħħħħħħħħħħħ#
                                              #
def calcular_pendiente(x1, x2, y1, y2):       # Se crea la funcion
    if (not isinstance(x1, int) and not isinstance(x1, float)) and (not isinstance(x2, int) and not isinstance(x2, float)) and (not isinstance(y1, int) and not isinstance(y1, float)) and (not isinstance(y2, int) and not isinstance(y2, float)):
        return "Error, debe de introducir numero en R" # Sino cumple la anterior condicion entonces retorna un msj de error
    else:                                     # Sino
        m = (y2-y1)/(x2-x1)                   # A la variable m se le asigana el resultado de la operacion
        return m                              # Se retorna el resultado
                                              #
#ħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħ#

#ħħħħħħħħħħħħħħħħħħħħħħħħħħħħ Estado de un estudiante ħħħħħħħħħħħħħħħħħħħħħħħ#
                                                    #
def estado(nota):                                   # Se crea la funcion
    if (isinstance(nota, int) and isinstance(nota, float)): # Condicion
        return "Indroduzca datos validos, numeros en R" # Mensaje de error
    elif 0 <= nota <= 100:                          # Condicion
        if 100 >= nota >= 70:                       # Condicion
            return "Aprobado"                       # Resultado
        elif nota >= 60 and nota <= 69:             # Condicion
            return "Aplazado"                       # Resultado
        elif nota < 60:                             # Condicion
            return "Reprobado"                      # Resultado
    else:                                           # Sino
        return "Introduzca una nota valida [0, 100]" # Mensaje de error

#ħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħ Forma numero ħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħ#
                                                          # 
def forma_num(x, y, z):                                   # Se crea la funcion
    if (isinstance(x, int)) and (isinstance(y, int)) and (isinstance(z, int)): # Se establece una condicion
        return x + y*10 + z*100                           # Si cumple la condicion ejecuta la formula
    else:                                                 # Sino
        return "Error, debe de introducir numeros enteros"# Retorna un msj de error

#ħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħ#

#########################Cuadratica con numeros complejos#######################

import math # Se importa la libreria matematica

def cuadratica(a, b, c): # Se crea la funcion
    if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)) and (isinstance(c, int) or isinstance(c, float)): # Se establece la condicion para el valor de los numeros
        if a != 0 and (b**2 - 4*a*c) >= 0: # Condicion para saber si es un numero en R o en R y I
            x1 = ((-b + (math.sqrt(b**2 - 4*a*c)) / (2*a))) # Formula de 'x1'
            x2 = ((-b - (math.sqrt(b**2 - 4*a*c)) / (2*a))) # Formula de 'x2'
            return x1, x2 # Retorna el resultado de la formulas
        elif a != 0 and (b**2 - 4*a*c) < 0: # Condicion para saber si es un numero en R y I
            x1 = complex((-b / (2*a)), (math.sqrt(-(b**2 - 4*a*c))) / (2*a)) # Formula de 'x1'
            x2 = complex((-b / (2*a)), (-math.sqrt(-(b**2 - 4*a*c))) / (2*a)) # Formula de 'x2'
            return x1, x2 # Retorna el resultado de las formulas
        else:
            return "Programmer error" # Mensaje de error
    else:
        return "Error, debe de introducir valores numericos pertenecientes a R" # Mensaje de error
    
###################################################################################

#ħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħħ#

################################## Prueba #########################################
def prof(lista):
    if isinstance(lista, list):
        return prof_aux(lista, 0, 0)
    return "Error"

def prof_aux(lista, i, r):
    if i >= len(lista):
        return r
    elif isinstance(lista[i], list):
        p = prof_aux(lista[i], 0, 0)
        if r < p+1:
            r = p+1
        return prof_aux(lista, i+1, r)
    else:
        return prof_aux(lista, i+1, r)

###################################################################################
