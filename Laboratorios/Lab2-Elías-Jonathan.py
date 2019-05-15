#Laboratorio,2 Recursividad
#-------------------------------------Funciones Booleanas------------------------------------
#                                                                                           #
#------------------------Determinar_si_un_numero es binario---------------------------------#
def ebin(nume, bol):               #Funcion que detecta que la funcion es booleana          #
    if (nume%10==1 or nume%10==0) and nume//10==0: #Caso Base                               #
        return bol                                 #Retorna el valor booleano               #
    elif (nume%10==1 or nume%10==0) and nume//10!=0:#Mantiene el valor de True              #
        return ebin(nume//10, bol and True)         #Si solo son valores                    #
    else:                       #El valor cambia a Falso su se introduce un numero != 1 o 0 #
        ebin(nume//10, bol and False)                                                       #
#__________________________________________________________________Booleana primos____________________________________________________________________________-
def bprim(a):#funcion booleana primos True es numero primo, False no es numero prim
    if isinstance (a, int):
        if a<0:#en caso de utilizar un numero negativo
            return bprim(abs(a))# transforma a valor absoluto y continua la funcion
        elif (a==2 or  a==5 or a==7 or a==3) or (a%2!=0 and a%3!=0 and a%7!=0 and a%5!=0) and (float(pow(a,(1/2))!=int(pow(a,(1/2))))):#casos que se deben cumplir para ser primos
            return True       #REtorna True lo que significa que si es numero primo 
        else:       #Si no se cumplen el caso especificado en el if entonces no es un numero primo
            return False #Retorna Falso
#___________________________________________________________________________________________________________________________________________________________________
#-------------------------------------------------------------------------------------------#
#-------------------------------------Convertir binario decimal-----------------------------#
def binario_a_decimal(num):#Funcion de conversion                                           #
    if isinstance(num, int) and ebin(num, True):#Restricciones                              #
        return BaD(num,0, 0)#Retorna los valores y la funcion que convierte a binario       #
    else:#Si no se cumplen las rstricciones                                                 #
        return "Error: introdusca un numero decimal"#indica el error                        #
def BaD(num, val, res):          #Funcion que convierte el binario a decimal                #
    if num//10==0: #Si es el ultimo valor de                                                # 
        return  num%10*(2**val)+res                                                         #
    else:# num//10!=0:                                                                      #
        return BaD(num//10, val+1 ,res+(num%10*2**val))                                     #
#-------------------------------------------------------------------------------------------#

#-----------------------------------------------------Contar Primos-------------------------#
def contar_primos(n,b): #Funcion de contar primos                                           #
    if isinstance (n,int) and n<b:#Se evaluan restricciones                                 #
        return Ca(n,b,0)#Si se cumple la restriccion#                                       #
    else:#Si no se cumple la restriccion                                                    #
         return "Error: introdusca un numero entero y el primer numero menor al otro"       #Indica el error
#-------------------------------------------------------------------------------------------#
def Ca(n,b,res):   #Funcion que cuenta los primos                                           #
    if n==b and bprim(n):#Caso que el ultimo numero es binario                              #
        return 1+res            #El resultado anterior menos uno                            #
    elif n==b and not bprim(n): #Si no es primo el ultimo numero                            #
        return res              #Retorna la cantidad de primos anteriores                   #
    elif n<b and not bprim(n):  #Si no es un numero primo                                   #
        return Ca(n+1,b,res)    #Retorna un numero primo                                    #
    else:                       #Si no se cumple ninguna de las anteriores                  #
        return Ca(n+1,b,res+1)  #Retorna la funcion con un un numero base mayor en uno      #
#-------------------------------------------------------------------------------------------#
#-------------------------------------funcion ring shift-------------------------------------------------------------------------------------------------------#
def ring_shift(lis):#Se define la funcion ring shift                                                                                                           #
    if isinstance (lis, int) and lis>0:# En el caso que se introdusca un numero mayor a cero y sea positivo                                                    #
        return ring(lis, 1,0, len(str(lis)),"pos")#Retorna la funcion ring indicando que el numero era positivo                                                #
    elif lis<0 and isinstance(lis, int):# en caso de que el numero sea negativo                                                                                #
        return ring (abs(lis),1,0,len(str(lis)),"neg")#Retorna la funcion ring indicando que es un numero negativo                                             #
    else:#En caso que no se cumplan las condiciones anteriores                                                                                                 #
        return "Error no se ha introducido numero entero"#Mensaje de Error                                                                                     #
def ring(lis,a,fin, lar,sig):# En el caso de que no se cumplan con ninguna de las dos anteriores se indica el error                                            #
    if a==2 and sig=="pos":#En caso de que se haya marcado que el numero era positivo                                                                          #
        return lis+fin*(10**(lar-1))#Se retorna el numero sin el digito por la menor cantidad de cifras y se le aumenta el valor a la cifra no signicativa     #
    elif a==2 and sig=="neg":#En caso de que sea negativa                                                                                                      #
        return (lis+fin*(10**(lar-2)))*-1#Se realiza el procedimiento anterior pero se multiplica por menos uno                                                #
    elif a==1:                                                                                                                                                 #
        return ring (lis//10 ,2, lis%10,lar,sig)                                                                                                               #
    #__________________________________________________________________________________________________________________________________________________________#
#---------------------------------------Multiplicar lista-------------------------------------------------------------------------------------------------------#
def multi(lis):# Se define la funcion multi                                                                                                                     #
    if isinstance (lis, list) and lis!=[]:# si el dato que se introdujo es una lista que no es vacio                                                            #
        return mul(lis,len(lis)-1, 0, 1)                                                                                                                        #
    else:#si no se cumplio el caso del principio                                                                                                                #
        return "Error se debe introducir una lista ó debe de ser distinta de []"                                                                                #
def mul(li, larg, pas,fin):#se define la funcion mul                                                                                                            #
    try: #en caso de que no sean caracteres numericos                                                                                                           #
        if pas==larg:#se esta multiplicando el ultimo digito                                                                                                    #
            return fin*li[larg]#Retorna el valor de fin multiplicado por el ultimo caracter                                                                     #
        elif pas<larg:#Si el digito que se esta evaluando no es el digito final                                                                                 #
            return mul(li, larg, pas+1, fin*li[pas])#se devuelve la lista pero se avanza un digito hacia la derecha y se multiplica el valor cargado por el valor del digio que se esta observando actualmente
    except:#Si no se han introducido solamente digitos numericos                                                                                                #
        return"Error: introdusca solamente caracteres numericos"#Devuelve al usuario el tipo de error                                                           #
#---------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------Funcion todos pares-------------------------------------------------------------------------------------------------------#
#Entradas: numeros
#Salidas: Booleano indicando si el numero es par
def pares(num):#define la funcion booleana oares
    if num%2==0:#caso que el numero sea par
        return True#retorna true
    else:#Si no es par
        return False#retorna falso
#TODOS PARES
#ENTRADAS LISTA
#SALIDA BOOLEANO TRUE OR FALSE DEPENDIENDO SI TODOS SON PARES O NO
def todos_pares(lis):#FUNCION TODOS PARES
    if isinstance(lis, list) and lis!= []:#SI LO QUE SE INTRODUJO ES UNA LISTA NO VACIA
        return parestodos(lis,0,True)#LLAMA A LA FUNCION AUXILIAR PARES TODOS
    else:#SI NO SE CUMPLIO CON LA RESTRICCION
        return "ERROR:INTRODUSCA UNA LISTA Y QUE NO ESTE VACIA"#RETORNA EL MENSAJE QUE EL ELEMENTO QUE SE INTRODUJO NO ES VALIDO
def parestodos(lis,paso,resultado):#FUNCION AUXILIAR QUE DEFINE SI SON NUMEROS PARES O NO
    if len(lis)==paso:#SE HA TERMINADO LA LISTA
        return resultado#RETORNA EL BOOLEANO
    elif pares(lis[paso]):#SI EL NUMERO QUE SE REVISA ES PAR
        return parestodos(lis,paso+1,resultado and True)#RETORNA LA LISTA AVANZA UN LUGAR A LA DERECHA Y REALIZA LA OPERACION BOOLENA CON EL RESULTADO
    else:#Si no se cumple ninguna de las anteriores
        return parestodos(lis,paso+1,resultado and False)#Retorna la operacion booleana x and False y avanza un paso a la izquierda
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    
