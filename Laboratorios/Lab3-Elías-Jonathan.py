#LABORATORIO PROGRAMADO 3
#REALIZADO POR ELIAS GRANADOS ULLOA Y JONATHAN ARAYA
#GRUPO 4
#PROFESOR EDUARDO ADOLFO CANESSA
#NOTA INVERTIRC ES CON RECUR. COLA Y INVERTIRP ES CON  RECUR. PILA
#NOTA EL ORDEN DE LAS SOLUCIONES VIENE AL CONTRARIO DEL ORDEN PROPUESTO
#------------------------------------------------------------------------------#
#ENTRADAS NUMERO Y FACTOR
#SALIDAS PRODUCTO
#RESTRICCIONES: FACTOR DEBE DE SER ENTERO, DEBEN SER CARACTERES NUMERICOS
#***********************************************************************************************************************#
def multiplicar(num1, num2):#FUNCION MULTIPLICAR
    try:
        if (isinstance (num1, float) or isinstance (num1, int)) and int(num2)==num2 and num1!=0:#RESTRICCIONES
            return multi(num1,num2,0)                 #LLAMA A LA FUNCION AUXILIAR
        elif num1==0:                               #EN CASO DE QUE EL PRIMER NUMERO SEA CERO
            return 0                                #SE RETORNA CERO PARA NO HACER UNA CORRIDA INECESARIA
        else:                                       #SI NO SE CUMPLEN LAS RESTRICCIONES
            return "ERROR:SEGUNDO ARGUMENTO DEBE SER ENTERO"#DESPLIEGA MENSAJE DE ERROR
    except:
        return "ERROR"
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#ENTRADAS: NUMEROS A MULTIPLICAR Y PUNTO DE INICIO DEL RESULTADO
#SALIDAS: PRODUCTO DE LOS NUMEROS
#RESTRICCIONES DEFINIDAS PREVIAMENTE
def multi(num1, num2, resul):#FUNCION AUXILIAR MULTI
    if num2==0:            #CASO BASE SE LLEGA EL FACTOR A CERO
        return resul       #RETORNA EL RESULTADO
    elif num2>0:           #SI NUM2 ES NUMERO NATURAL
        return multi(num1, num2-1, resul+num1)     #RESTA UNO Y REALIZA SUMAS SUCECIVAS DE NUM1
    elif num2<0 and num1>0:                        #SI NUM2 ES UN ENTERO NEGATIVO Y NUM1 ES ENTERO POSITIVO
        return multi(-1*num1, -1*num2, resul)      #INVIERTE LOS SIGNOS DE LOS SIMBOLOS
    elif num2<0 and num1<0:                        #SI AMBOS SON NEGATIVOS
        return multi(abs(num1),abs(num2), resul)   #RETORNA LOS VALORES ABSOLUTOS DE AMBOS NUMEROS
#------------------------------------------------------------------------------------------------------------------------------#
#ENTRADAS: CARACTER NUMERICO
#SALIDAS: MISMO NUMERO PERO CON ORDEN INVERTIDO
#RESTRICCIONES: DEBE SER UN NUMERO
def invertirc(li):                                    #FUNCION INVERTIR CON RECURCIVIDAD TIPO COLA
    if 0==0:#try:
        if isinstance(li, list):                          #DEBE DE SER UNA LISTA
            return inverc(li,1,[])                          #SE LLAMA LA FUNCION AUXILIAR
        else:                                              #NO SE CUMPLIERON RESTRICCIONES
            return "ERROR DEBE DE SER UN CARACTER NUMERICO"#MUESTRA EL ERROR
    #except:
    #    return "ERROR"
def inverc(li,i,result):                               #FUNCION AUXILIAR DE INVERTIR
    if len(li)-i==0:                               #SI EL LARGO DEL NUMERO ES UN DIGITO
        return result+[li[len(li)-i]]                           #RETORNA EL NUMERO COMPLETAMENTE INVERSO
    else:                                              #SI EL NUMERO ES MAYOR A UN DIGITO
        return inverc(li,i+1,result+[li[(len(li)-i)]]) #RETORNA LA FUNCION PERO EL NUMERO LO DIVIDE ENTRE DIEZ Y INVIERTE LA POSICION DEL PRIMER NUMERO
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#ENTRADAS NUMERO
#SALIDAS NUMERO INVERTIDO
#RESTRICCIONES DEBE SER UN NUMERO
def invertirp(lis):    #INVERTIR NUMERO CON PILA
    try:
        if isinstance(lis,list):                               #RESTRICCIONES: NUMERO DEBE PERTENECER A N* DEBE SER CARACTER NUMERICO
            if len(lis)==1:                                        #CASO BASE EL LARGO DEL NUMERO ES UNO
                return [lis[len(lis)-1]]                                             #RETORNA EL ULTIMO NUMERO DE UN DIGITO
            else:                                                       #SI NO SE CUMPLE
                a=lis[len(lis)-1]
                del lis[len(lis)-1]
                return [a]+invertirp(lis)                                          #RETORNA EL ULTIMO DIGITO ELEVADO AL LARGO DEL NUMERO
        else:
            return "ERROR:DEBE DE SER LISTA"
    except:
        return "ERROR"
#-----------------------------------------------------------------------------------------------------------
#ENTRADAS LISTA
#SALIDA ULTIMO PAR EN LA LISTA
#RESTRICCIONES DEBE DE INGRESARSE UNA LISTA
def ultimo_par(lis):#FUNCION DEVUELVE ULTIMO PAR
    if isinstance(lis, list):             #RESTRICCION ES UNA LISTA
        return ulpar(lis,0,"no hay pares")#LLAMA FUNCION AUXILIAR
    else:return "ERROR DEBE SER UNA LISTA CON CARACTERES NUMERICOS ENTEROS"#RETORNA EL ERROR SI NO SE CUMPLE LA RESTRICCION

def ESNUME(carac):#INDICA SI EL INGRESADO ES DE TIPO NUMERICO
    try:          
        if isinstance(carac,int) or isinstance(carac,float):#SI ES UN NUMERO
            return True                #BOOLEANO TRUE
        else:                          #SI NO LO ES
            return False               #BOOLEANO FALSE
    except: return False               #SI OCURRE UN ERROR EN LA EJECUCION RETORNA FALSO
def ulpar(lis,i,par):                  #FUNCION ULTIMO PAR
    if len(lis)==i:                    #SI EL INDICE RECORRIO LA LISTA
        return par                     #RETORNA EL ULTIMO PAR VISTO
    elif not ESNUME(lis[i]):           #SI NO ES UN NUMERO 
        return ulpar(lis,i+1,par)      #CONTINUA CON EL SIGUIENTE EN LA LISTA
    elif ESNUME(lis[i]) and lis[i]%2==0:# SI ES PAR LO GUARDA EN LA VARIABLE PAR
        return ulpar(lis,i+1,lis[i])     #Y CONTINUA CON EL SIGUIENTE EN LA LISTA
    else:                               #SI NO ES PAR
        return ulpar(lis,i+1,par)       #CONTINUA REVISANDO LA LISTA
#-------------------------------------------------------------------------------------------------------
#ENTRADAS: LISTA
#SALIDAS: CUANTOS SON MAYORES O IGUALES A 70
#RESTRICCION DEBEN SER UNA LISTA Y INDICES DEBEN SER NUMEROS
def notas(lista):
    if 0==0:
        if isinstance(lista, list):#restriccion es una lista
            return notax(lista,0,0,0)#llama a la funcion auxiliar
    #except:#hubo error en el proceso
    #    return "ERROR:INCERTE UNA LISTA"#muestra mensaje de error
def notax(LISTA,I,RES,RES2):#AUXILIAR DE LA FUNCION NOTAS
    if I==len(LISTA):return {"APROBADOS":RES,"REPROBADOS":RES2,"PROMEDIO":promedio(LISTA,0,0)}#RETORNA LA CANTIDAD DE ESTUDIATES QUE SACARON NOTA MAYOR A 70
    elif not ESNUME(LISTA[I]):return "ERROR: INTRODUSCA SOLO CARACTERES NUMERICOS"#notax(LISTA,I+1,RES) #REVISA EL SIGUIENTE INDICE
    elif ESNUME(LISTA[I]) and LISTA[I]>=70:return notax(LISTA,I+1,RES+1,RES2)#CUENTA UNA NOPTA MAYOR IGUAL A 70
    elif ESNUME(LISTA[I]) and LISTA[I]<70:return notax(LISTA,I+1,RES,RES2+1)#CUENTA UNA NOPTA MAYOR IGUAL A 70
def promedio(lista,i,res):
    if i==len(lista):
        return res/i
    else:
        return promedio(lista,i+1,res+lista[i])

#---------------------------------------------------------------------------------------------------------------------------#
def todos_divisores(divisor,lista):#funsion todos divisores
    try:
        if isinstance(lista,list) and isinstance(divisor, int):#si divisor es numero entero y lista es tipo lista
            return divisores(divisor,lista,0)#LLAMA A LA FUNCION AUXILIAR
        else:                                   #SI NO SE CUMPLEN LAS RESTRICCIONES
            return "ERROR: DEBE DE INGRESARSE UNA LISTA NUMERICA"  #RESTORNA MENSAJE DE ERROR
    except:#ERROR DURANTE LA EJECUCION
        return "ERROR:MIENTRAS SE EJECUTABA"#MENSAJE DE ERROR
def divisores(divisor,lista,i):#FUNCION DIVISORES
    if i==len(lista):          #SI RECORRIO LA LISTA
        return True            #RETORNA TRUE SI TODOS FUERON DIVISIBLES
    elif not ESNUME(lista[i]):#SI ENCUENTRA ALGO QUE NO SEA UN NUMERO
        return "ERROR DEBEN SER SOLO CARACTERES NUMERICOS"#RETORNA MENSAJE DE ERROR
    elif lista[i]%divisor==0:               #PRUEBA SI ES DIVISOR
        return divisores(divisor,lista,i+1) #AVANZA AL SIGUIENTE INDICE
    else:                                   #SI NO SE CUMPLE NINGUNO DE LOS ANTERIORES
        return False                        #RETORNA FALSO
