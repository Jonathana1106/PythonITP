'''
		Instituto Tecnológico de Costa Rica

		    Ingeniería en Computadores

 Laboratorio #5: Estructuras de datos
 Estudiantes: Elias Granados Ulloa-Jonathan Guzman Araya 
 Profesor: Eduardo Canessa Montero
 Fecha de entrega: 30/05/2013

'''

#۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞FUNCIONES AUXILIARES۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞#
#******************REVISA SI ES UN NUMERO O NO********************************#
                                                                              #
def esnumero(num):#FUNCIO ES NUMERO                                           #
    try:          #SI NO HAY ERROR A LA HORA DE CONVERTIR EN FLOAT            #
        float(num)                                                            #
        return True#RETORNA UN TRUE                                           #
    except:       #SI NO SE PUEDE CONVERTIR EN NUMERO                         #
        return False #RETORNA UN FALSO                                        #
                                                                              #
#۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞Ordenamiento de burbuja۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞#
def burbuja(vector):#ORDENAMIENTO DE BURBUJA                                                                    #
    cambios=0# SE EFECTUA CAMBIO                                                                                #
    i=0      # INDICE EN REVISION EN LA LISTA                                                                   #
    while True:#ABRE UN BUCLE                                                                                   #
        try:   #SI NO SE PRODUCE UN ERROR                                                                       #
            if vector[i]<=vector[i+1]:#REVISA QUE EL ORDEN SEA DE MENOR A MAYOR                                 #
                i+=1  #SE MUEVE HACIA LA DERECHA DE LA LISTA                                                    #
            else:    #SI NO VA DE MAYOR A MENOR                                                                 #
                temp=vector[i]  #GUARDA EL PRIMER DATO                                                          #
                vector[i]=vector[i+1] #CARGA EL DATO DE LA DERECHA EN EL DE LA IZQUIERDA                        #
                vector[i+1]=temp    #CARGA EL DATO DE LA IZQUIERDA EN LA DERECHA                                # 
                i+=1                 #AVANZA                                                                    #
                cambios=1           #indica que se realizo un cambio                                            #
        except:                     #SE PRODUJO UN ERROR "esperando que sea el finde lista"                     #
            if cambios!=0:          #SE REALIZO UN CAMBIO                                                       #
                cambios=0           #REINICIA VARIABLE CAMBIOS                                                  #
                i=0                 #REINICIA VARIABLE INDICE                                                   #
            else:                   #NO SE REALIZO NINGUN CAMBIO EN LA CORRIDA                                  #
                return vector       #RETORNA EL VECTOR YA ORDENADO                                              #
                break               #SE CIERRA EL BUCLE                                                         #
#۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞#
                                                                                                                #
def busquedabina(vector,quebusco):                     #BUSQUEDA BINARIA                                        #
    final=len(vector)-1                 #FINAL ES IGUAL AL FINAL DE LA LISTA                                    #
    principio=0                         #PRINCIPIO ES IGUAL A 0                                                 #
    while True:                     #ABRE UN BUCLE                                                              #
        if quebusco<vector[round((principio+final)/2)]:#SI LO QUE BUSCO ES DISTINTO AL INDICE ACTUAL            #
            print("final",final,"principio",principio,"a")#PRUEBA PARA DEBUGUEO EN CONSOLA                      #
            final=round((principio+final)/2)            #FINAL VA A SER IGUAL AL PRINCIPIO MAS EL FINAL ENTRE 2 #
        elif quebusco>vector[round((principio+final)/2)]:  #SI LO QUE BUSCO ES MAYOR                            #
            print("final",final,"principio",principio,"b") #PRUEBA PARA DEBUGUEO EN CONSOLA                     #
            principio=round(((final+principio)/2)+0.1) #EL PRINCIPIO VA A SER IGUAL A EL PRINCIPIO MAS EL FINAL ENTRE 2
        elif quebusco==vector[round((principio+final)/2)]: #SI SE ENCONTRO LO QUE SE BUSCABA                    #
            print("final",final,"principio",principio, "c")#PRUEBA PARA DEBUGUEO EN CONSOLA                     #
            return round((principio+final)/2)              #DEVUELVE EL INDICE                                  #
            break                                                                                               #
        elif final==principio or final<principio:          #SI NO SE ENCONTRO                                   #
            print("final",final,"principio",principio, "d")#PRUEBA PARA DEBUGUEO EN CONSOLA                     #
            return "NO SE ENCONTRO LO QUE BUSCABA"         #SE INDICA QUE NO EXISTE                             #
            break                                                                                               #
#۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞#
                                                        
#۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞1ER FUNCION INSTRUCCIONES AL USUARIO۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞#
a="1"
vector=[]                                                                    #SE DEFINE LA VARIABLE DEL VECTOR
print("INGRESE NUMEROS DE UNO EN UNO")                                       #SE IMPRIME LAS INSTRUCCIONES
print("SI DESEA SALIR DE LA APLICACION ESCRIBA LA PALABRA 'alto'")
while a=="1":                                                                  #SE ABRE UN BUCLE
    x=input("INTRODUZCA AQUI UN NUMERO \n")                                  #COMPRUEBA QUE SEA UN CARACTER NUMERICO
    if esnumero(x):                                                          #SI ES UN NUMERO
        vector.append(float(x))                                              #INSERTA X EN EL VECTOR
    elif x=="alto":                                                          #SI SE INTRODUJO LA PALABRA ALTO
        a="2"                                                                #SE SALE DEL BUCLE
    else:                                                                    #SI NO SE CUMPLE NINGUNA DE LAS ANTERIORES
        print("NO SE AGREGO POR QUE NO ERA UN NUMERO")                       #SE ENVIA UN MENSAJE AL USUARIO     #
#۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞#                                   #
burbuja(vector)                                                                                                  #
while a=="2":                                                                                                    #
    print("ESCOJA SI DESEA BUSCAR ALGUN ELEMENTO")                                                               #
    busco=float(input("INDIQUE QUE DESEA BUSCAR"))                                                               #
    print(vector)                                                                                                #
    print(busquedabina(vector,busco))                                                                            #
#۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞#
    print("SI DESEA VOLVER A INTRODUCIR UNA LISTA INGRESE 1")                                                    #
    print("SI DESEA REALIZAR UNA BUSQUESA INGRESE 2")                                                            #
    print("SI DESEA SALIR ESCRIBA CUALQUIER CARACTER DISTINTO A ESTOS")                                          #
    a=input("INDIQUE QUE DESEA REALIZAR")                                                                        #
#۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞#
#۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞#



#۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞#
                                                                                                                 #
def posiciones(lista): #Funcion principal que recibe los datos de los jugadores                                  #
    return printlista(sort(lista))                                                                               #
                                                                                                                 #
#۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞#
                                                                                                                 #
def printlista(lista):# Funcion que imprime los datos de la lista (jugadores)                                    #
    print("Posición   Nombre  Movimientos")                                                                      #
    i = 0                                                                                                        #
    while i < len(lista):                                                                                        #
        print(i+1,"        ",lista[i][0],"       ",len(lista[i][1]))                                             #
        i += 1                                                                                                   #
#۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞#

#۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞ORDENAMIENTO EN SORT۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞#
                                                                                                                 #
def sort(lista):                                #FUNCION                                                         #
    try:                                                                                                         #
        if lista != [] and len(lista) > 1:          #SI LA LISTA NO ESTA VACIA Y ES MAYOR A UN                   #
            inicio = 0                            #DEFINA VARIABLE INICIO                                        #
            final = len(lista)-1                  #DEFINE EL FINAL DE LA LISTA                                   #
            menor = []                            #DEFINE A MENORES                                              #
            igual = []                            #DEFINE A IGUALES                                              #
            mayor = []                            #DEFINE A MAYOR                                                #
            while inicio <= final:                #NO SE A SOBREPASADO EL FINAL                                  #
                if len(lista[inicio][1]) > len(lista[final][1]):  #UNO DE LA LISTA ES MAYOR                      #
                    mayor.append(lista[inicio]) #SE AGREGA A LA LISTA MAYORES                                    #
                    inicio += 1                   #SE MUEVE HACIA LA DERECHA                                     #
                elif len(lista[inicio][1]) < len(lista[final][1]):#SI ES MENOR                                   #
                    menor.append(lista[inicio]) #SE AGREGA A MENORES                                             #
                    inicio += 1                   #SE MUEVE HACIA LA DERECHA                                     #
                elif len(lista[inicio][1]) == len(lista[final][1]):#SI ES IGUAL SE AGREGA A LA LISTA IGUALES     #
                    igual.append(lista[inicio])  #LISTA IGUAL                                                    #
                    inicio += 1                    #SE AVANZA HACIA LA DERECHA                                   #
            return sort(menor) + igual + sort(mayor)#SE SUMAN LAS LISTAS                                         #
        else:return lista                       #SI LA LISTA ES DE UN ELEMENTO O VACIA SE RETORNA                #
    except:return "DATOS INGRESADOS INCORRECTOS"#SI OCURRE UN ERRROR SE MUESTRA EL MENSAJE                       #
                                                                                                                 #
#۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞#
