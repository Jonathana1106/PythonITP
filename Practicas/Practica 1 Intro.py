############################### Practica 1 ######################################

import math
def calc_circulo(radio):
    if (isinstance(radio, int) or isinstance(radio, float)) and  radio >= 0:
        circunferencia = 2*math.pi*radio**2
        area = math.pi*radio**2
        resultado = [area, circunferencia]
        return resultado
    else:
        return "Error, introduzca un numero >= 0"
    
#PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP#

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
        return "Error en numero de entrada" # Retorna un msj de error

#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA#


def esfera(radio):
    if (isinstance(radio, int) or isinstance(radio, float)) and  radio >= 0:
        #Area = 4*math.pi*radio**2
        #Volumen = 4/3*math.pi*radio**2
        Resultado = {"Area": 4*math.pi*radio**2, "Volumen":  4/3*math.pi*radio**2}
        return Resultado
#UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU#

def bisiesto(ano):
    if (isinstance(ano, int) or isinstance(ano, float)) and ano >= 0:
        if ano%4 == 0 and ano%100 != 0:
            return True
        elif ano%400 == 0 and ano%100 == 0:
            return True
        else:
            return False
    else:
        return "Error"

#LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL#

def foo(op):
    return op / 7

#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII#

def mediano(num, num1, num2):
    if isinstance(num, int) and isinstance(num1, int) and isinstance(num2, int):
        if num<num1<num2:
            return num1
        elif num1<num2<num:
            return num2
        elif num2<num<num1:
            return num
        elif num>num1<num2 and num<num2:
            return num
        elif num>num1>num2:
            return num1
    else:
        return "Error"


#NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN#
    
