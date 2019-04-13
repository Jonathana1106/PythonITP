'''

Profesor: Eduardo Canessa Montero
Alumno: Jonathan Alberto Guzman Araya
Curso: Introduccion a la programacion
Quiz #2

'''

#################################Pila###########################################

#def par_impar(num):
 #   if isinstance(num, int) and num >= 0:
  #      if num == 0:
   #         t = (num, num)
    #        return t
     #   else:
      #      return aux(num, 0, 0)
    #else:
     #   return "Error, introducir un numero entero mayor que cero"

#def aux(num, n, m):
 #   if num == 0:
  #      tupla = (par, impar)
   #     return tupla
    #elif ((num%10)%2) == 0:
     #   par = par +((num%10)*10**n)
      #  return par + aux(num//10, n+1, m)
    #else:
     #   impar = impar + ((num%10)*10**m)
      #  return impar + aux(num//10, n, m+1)

#Error del codigo: Las variables par e impar no estan definidas por lo que no guarda
#el resultado de cada operacion
    
###############################Cola###########################################

#Entradas: Numero
#Salidas: Una tupla con los numero pares y numeros impares
#Restricciones: Numero entero y mayor que 0

def par_impar(num): #Se crea la funcion
    if isinstance(num, int) and num >= 0: #Se dictan las condiciones que establecen que el numero sea entero
        if num == 0: # Si el numero es igual que 0
            t = (num, num) #retorna una tupla con el numero
            return t
        else:
            return aux(num, 0, 0, 0, 0) #Llamada de la funcion auxiliar
    else:
        return "Error, introduzca un numero entero mayor que 0" #Msj de error

def aux(num, n, m, par, impar): #Se crea la funcion auxiliar
    if num == 0: #Si el numero es igual a 0
        tupla = (par, impar) # Se crea una tupla con los numeros pares e impares
        return tupla #Se retorna la tupla
    elif ((num%10)%2) == 0: # Si el numero es par
        par = par + ((num%10)*10**n) #Se asigna a la variable par
        return aux(num//10, n+1, m, par, impar) # Se hace recursividad de la misma funcion
    else:
        impar = impar + ((num%10)*10**m) #Si el numero es impar entonces se le asigna a la variable impar
        return aux(num//10, n, m+1, par, impar) #Se hace recursividad de la misma funcion
    
##############################################################################

#Entradas: Recibe 2 numeros
#Salidas: Retorna un nuevo numero producto de la multiplicacion de los digitos de igual valor posicional en cada numero
#Restricciones: Numeros enteros mayores que 0 y de igual tama;o

def multdig(num1, num2): #Se crea la funcion
    if isinstance(num1, int) and isinstance(num2, int): #Se establecen las restricciones
        if len("num1") == len("num2"): #Se asegura que el tamano de los numeros sea igual
            return multidig(num1, num2, 0) #Se llama a la funcion auxiliar
        else:
            return "Error, el tamano del los numeros debe de ser igual" #Se crea un msj de error
    else:
        return "Error, los numeros deben de ser enteros" #Se crea un msj de error

def multidig(num1, num2, n): #Se crea una funcion auxiliar
    if num1 == 0: #Si el numero es igual a 0 
        return 0 #se retorna el resultado
    elif ((num1%10) * (num2%10)) >= 10: # Condicion
        return ((((num1%10) * (num2%10))%10)*10**n) + multidig(num1//10, num2//10, n+1) #Resolucion y llamado recursivo
    else:
        return (((num1%10) * (num2%10))*10**n) + multidig(num1//10, num2//10, n+1) # Resolucion y llamado recursivo

##############################################################################
