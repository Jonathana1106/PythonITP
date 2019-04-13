'''

Profesor: Eduardo Canessa Montero.
Alumno: Jonathan Alberto Guzman Araya.
Carnet: 2013041216.
Curso: Introduccion a la programacion.
Quiz #4.

'''

#ßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßß#
#ßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßß#
#Entradas: Recibe un digito y un numero entero.
#Restricciones: El digito debe cumplir que sea digito [0,9] y el numero ser positivo.
#Salidas: Retorna una tupla del mismo numero pero sin el dig formando asi nuevos numeros.

def tupla_nums(dig, num): # Se crea la funcion 'tupla_nums'.
    if (isinstance(dig, int) and 0 <= dig <= 9) and isinstance(num, int): # Se crean las restricciones.
        if num == 0: # Si el numero es igual a '0' entonces retorna ...
            return 
        else: # Sino
            return aux(dig, num, 0, 0) # Entonces llama a la funcion auxiliar 'aux'.
    else: # Sino 
        return "Error en los datos de entrada" # Retorna un mensaje de error.

def aux(dig, num, n, r): # Se crea la funcion auxiliar 'aux'.
    if num == 0: # Si el numero es igual a '0' entonces retorna el resultado 'r'.
        return r
    #CORECCION# Se cambia '0' por dig que es la comparacion correcta sino entonces no genera error pero no retorna el resultado deseado.
    elif (num%10) != dig: # Si el ultimo digito del numero es distinto del digito.
        r = r + ((num%10)*(10**n)) # Se asigna el valor de 'r'.
        return aux(dig, num//10, n+1, r) # Retorna la funcion recursiva con el numero sin su ultimo digito y con n aumentado en 1.
    else: 
        return aux(dig, num//10, 0, 0), r # Se cambia de poscicion el 'r' para que retorne en el orden correcto.

#################################### DUDA ###################################
#                                                                           #
#Una tupla es de solo 2 elementos o puede tener varios como una lista..?????#
#                                                                           #
#############################################################################

#ßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßß#
#ßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßß#

#£££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££#
#£££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££#
#Entradas: Recibe dos numeros naturales.
#Restricciones: Tienen que cumplir que sean numeros naturales.
#Salidas: Retorna un solo numero en el que el primero y el segundo estan 'pegados'.

def num_append(num1, num2): # Se crea la funcion 'num_append'.
    if (isinstance(num1, int) and num1 >= 0) and (isinstance(num2, int) and num2 >= 0): # Se establecen las restricciones para ambos numeros.
        # La funcion auxiliar se le elimina '-1'.
        return aux1(num1, cuenta(num2), 0) + aux2(num2, 0, 0) # Si se cumplen retorna la suma de dos funciones auxiliares.
    else: # Sino
        return "Error" # Genera un mensaje de error.

def aux1(num1, n, r): # Se crea la funcion auxiliar 'aux1'.
    if num1 == 0: # Si num1 es igual a '0'.
        return r # Entonces retorna el valor de 'r'.
    else: # Sino.
        r = r + ((num1%10)*(10**n)) # Se incrementa 'r' en el valor de el ultimo digito de num1 elevado a 'n'.
        return aux1(num1//10, n+1, r) # Se retorna la funcion auxiliar con num1 decrementado en un dig y 'n' aumentado en 1.

def aux2(num2, n, r): # Se crea la funcion auxiliar 'aux2'.
    if num2 == 0: # Si num2 es igual a '0'.
        return r # Entonces retorna el valor de 'r'.
    else: # Sino.
        r = r + ((num2%10)*(10**n)) # Se incrementa 'r' en el valor de el ultimo digito de num2 elevado a 'n'.
        return aux2(num2//10, n+1, r) # Se retorna la funcion auxiliar con num2 decrementado en un dig y 'n' aumentado en 1.

def cuenta(num2): # Se crea la funcion auxiliar 'aux3'.
    if num2 == 0: # Si el numero es igual a '0' retorna 1.
        return 1
    else: # Sino.
        return aux3(num2, 0) # Llama a una funcion auxiliar 'aux3'.
    
def aux3(num2, r): # Se crea la funcion 'aux3'.
    if num2 == 0: # Si el num2 es igual a '0'.
        return r # Retorna 'r'.
    else: # Sino.
        r = r + 1 # Se incrementa r en 1.
        return aux3(num2//10, r) # Se retorna la funcion auxiliar con el num disminuido en un digito.
        
#£££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££#
#£££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££££#
    
        
