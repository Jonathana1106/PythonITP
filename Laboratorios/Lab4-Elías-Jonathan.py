'''    Instituto Tecnológico de Costa Rica

		          Ingeniería en Computadores

                Laboratorio de taller #4
                Autores: Elias Granados Ulloa--Jonathan Guzman Araya
                Profesor: Eduardo Canessa Montero
                Fecha de entrega: 23/05/2013
                Hora: 23:55

'''

#ѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺ#
#Producto escalar                                                           
def producto_escalar(vec, num): #Se crea la funcion producto escalar                                 
    if isinstance(vec, list): #Se obliga a que el vector sea una lista
        return producto_escalar_aux(vec, num, 0, len(vec), []) #llama a la funcion auxiliar
    else:
        return "Error, el vector debe de ser una lista" #msj de error  

#Producto escalar auxiliar
def producto_escalar_aux(vec, num, i, n, result): #producto ecalar auxiliar               
    if i == n:            
        return result                                        
    else:                                                    
        result.append(vec[i] * num)                          
        return producto_escalar_aux(vec, num, i +1, n, result)

#ѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺ#
#Multiplicar vectores
def multiplicar_vectores(vec1, vec2):
    if len(vec1) ==  len(vec2):
        return multiplicar_vectores_aux(vec1, vec2, 0, len(vec1), [])
    else:
        return "Error, los vectores deben de ser de igual tama;o"

#Multiplicar vectores auxiliar
def multiplicar_vectores_aux(vec1, vec2, i, n, result):
    if i == n:
        return result
    else:
        result.append(vec1[i] * vec2[i])
        return multiplicar_vectores_aux(vec1, vec2, i +1, n, result)

#ѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺѺ#



#======================================================================================================================================================#
def matrix_octal():#MATRIX OCTAL
    def aux(x,y):  #FUNCION AUXILIAR
        if len(x)==8:#SI SE TIENEN 8 LISTAS
            return x #RETORNA LA MATRIX
        elif len(x)<8 and len(y)==8:#SI EL LARGO DE UNA SUBLISTA ES 8
            return aux(x+[y],[])    #SUMA LA SUB LISTA A LA MATRIX
        else:                                              #SI NO SE CUMPLE NINGUNA CONDICION
            return aux(x,y+[int(str(len(x))+str(len(y)))]) #RETORNA EL LA POSICION DE LA LISTA Y EL LARGO DE LA SUBLISTA
    return aux([],[])                                      #RETORNA LA FUNCION AUXILIAR
#======================================================================================================================================================#
def matrizasterisco(i,j,y):                                                     #SE INTRODUCE LOS INDICES                                              #
    def diagonal1(i,j,result,lectura):                                        #DIAGONAL DE IZQUIERDA A DERECHA                                         #
        if (j==0 or i==0) and lectura==0:return diagonal1(i,j,result,1)       #SE LLEGA AL PUNTO MAXIMO                                                #
        elif j!=0 and i!=0 and lectura==0:return diagonal1(i-1,j-1,result,0)  #SE MUEVE DE IZQUIERDA A ARRIBA                                          #
        elif lectura==1:                                                      #SE LLEGO YA AL PUNTO MAXIMO                                             # 
            try:return diagonal1(i+1,j+1,result+[matrix_octal()[i][j]],1)     #SI SE PUEDE GUARDAR EL DATO SE GUARDA Y SE AVANZA                       #
            except:return result                                              #SI NO SE DEVUELVE EL RESULTADO                                          #
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#                                                                        #
    def diagonal2(i,j,result,lectura):                                        #DIAGONAL DE DERECHA IZQUIERDA                                           #
        if (j==7 or i==0) and lectura==0:return diagonal2(i,j,result,1)       #SE LLEGA AL PUNTO MAXIMO                                                #
        elif j!=0 and i!=0 and lectura==0:return diagonal2(i-1,j+1,result,0)  #SE AVANZA AL PUNTO MAXIMO DE LA DIAGONAL                                #
        elif lectura==1:                                                      #SI YA SE LLEGO AL PUNTO MAXIMO                                          #
            try :                                                             #                                                                        #
                if j>=0:                                                      #                                                                        #
                    return diagonal2(i+1,j-1,result+[matrix_octal()[i][j]],1) #SI HAY DATO LO GUARDA                                                   #
                else:                                                         #                                                                        #
                    return result                                             #                                                                        #
            except:return result                                              #SI NO QUEDAN DATOS ENTREGA EL RESULTADO                                 #
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#                                                                        #
    def vertical(y,j,result):                                                 #SACA LOS VERTICALES                                                     #
        if (i,j,result):                                                      #                                                                        #
            if y==8:return result                                             #CUANDO SE ACABA LA LISTA RETORNA EL RESULTADO                           #
            else:return vertical(y+1,j,result+[matrix_octal()[y][j]])         #GUARDA DATO Y AVANZA HACIA ABAJO                                        #
    try: #RESTRICCIONES
        return {"DIAGOID":diagonal1(i,j,[],0),"DIAGODI":diagonal2(i,j,[],0),"VERTICAL":vertical(y,j,[]),"HORIZONTAL":[matrix_octal()[i]]}              #
    except:
        return "ERROR INTRODUZCA UN DATO VALIDO"
#======================================================================================================================================================#
def imprimirmatriz(matriz,i):#IMPRIME UNA  MATRIZ EN CONSOLA
    if i< len(matriz):       #SI ELINDICE ES MENOR AL FINAL DE LA MATRIZ
        print(matriz[i])     #IMPRIME UNA FILA DE LA MATRIZ
        return imprimirmatriz(matriz,i+1)#CONTINUA CON LA SIGUIENTE FACIL
#==============================================================================================================#
def primo(num):                                                                          #SI ES NUMERO PRIMO   #
    if (num!=2 and num!=3 and num!=5 and num!=7) and (num%2==0 or num%3==0 or num%5==0 or num%7==0 or (pow(num,0.5)==int(pow(num,0.5)))): #REVISA SI ES MULTIPLI#
        return False                                                                     #SI ES PRIMO          #
    else:                                                                                #SI NO TIENE MULTIPLO #
        return True                                                                      #SI NO SE CUMPLE      #
#========================================================================================#*********************##===========#
def matrix_decimal():#MATRIX OCTAL                                                                                          #
    def aux(x,y):  #FUNCION AUXILIAR                                                                                        #
        if len(x)==10:#SI SE TIENEN 8 LISTAS                                                                                #
            return x #RETORNA LA MATRIX                                                                                     #
        elif len(x)<10 and len(y)==10:#SI EL LARGO DE UNA SUBLISTA ES 8                                                     #
            return aux(x+[y],[])    #SUMA LA SUB LISTA A LA MATRIX                                                          #
        else:                                              #SI NO SE CUMPLE NINGUNA CONDICION                               #
            return aux(x,y+[int(str(len(x))+str(len(y)))]) #RETORNA EL LA POSICION DE LA LISTA Y EL LARGO DE LA SUBLISTA    #
    return aux([],[])                                      #RETORNA LA FUNCION AUXILIAR                                     #
#===========================================================================================================================#
def Primos():                                #FUNCION MULTIPLO                     #
    def aux1(matrix,i,j):                    #FUNCION AUXILIAR DE MULTIPLO          #
        if i==len(matrix):                   #SE TERMINO DE VER LA MATRIX           #
            return matrix                    #RETORNA LA MATRIX CON LOS CAMBIOS     #
        elif j==len(matrix[i]):              #SI SE TERMINO EL VECTOR               #
            return aux1(matrix,i+1,0)        #CONTINUA EL SIGUIENTE VECTOR          #
        else:                                #SI SE ENCUENTRA DENTRO DE LA MATRIX   #
            if primo(matrix[i][j]):          #REVISA SI ES PRIMO#
                matrix[i][j]=""              #Y BORRA EL ESPACIO                    #
                return aux1(matrix,i,j+1)    #RETORNA LA FUNCION                    #
            else:                            #SI NO ES DIVISIBLE ENTRE EL DIVISOR   #
                return aux1(matrix,i,j+1)    #SE MUEVE AL SIGUIENTE CAMPO           #
    return aux1(matrix_decimal(),0,0)        #                                      #
#===================================================================================#
def multiplo(matrix, divisor):               #FUNCION MULTIPLO                      #
    def aux1(matrix,i,j,divisor):            #FUNCION AUXILIAR DE MULTIPLO          #
        if i==len(matrix):                   #SE TERMINO DE VER LA MATRIX           #
            return matrix                    #RETORNA LA MATRIX CON LOS CAMBIOS     #
        elif j==len(matrix[i]):              #SI SE TERMINO EL VECTOR               #
            return aux1(matrix,i+1,0,divisor)        #CONTINUA EL SIGUIENTE VECTOR  #
        else:                                #SI SE ENCUENTRA DENTRO DE LA MATRIX   #
            if matrix[i][j]%divisor==0:      #REVISA SI ES DIVISOR                  #
                matrix[i][j]=""             #Y BORRA EL ESPACIO                     #
                return aux1(matrix,i,j+1, divisor)    #RETORNA LA FUNCION           #
            else:                            #SI NO ES DIVISIBLE ENTRE EL DIVISOR   #
               return aux1(matrix,i,j+1,divisor)    #SE MUEVE AL SIGUIENTE CAMPO   #
    try: 
        return aux1(matrix,0,0,divisor)          #                                      #
    except:
        "ERROR INTRODUSCA UN DATO VALIDO"
def eliminar_numeros(cadena):
    try:
        return gg()
    except:
        "Ingrese datos validos"
def esnume(x):
    try:
        float(x)
        return True
    except:
        return False
def gg(lista,i,final,s):
    if i==len(lista) and s==0:
        print("h")
        return gg(lista,0,final,1)
    elif i==len(lista) and s==1:
        print("g")
        return final
    elif i==len(lista) and s==0:
        print("f")
        return gg(lista,0,final,1)
    elif i<len(lista) and s==1:
        print("e")
        return gg(lista,i+1,final+lista[i],s)
    else:
        if esnume(lista[i]):
            print("a")
            del lista[i]
            gg(lista,i,final,s)
        else:
            print("b")
            gg(lista,i+1,final,s)
a=input("""INTRODUZCA 0 PARA USAR LA FUNCION MATRIX OCTAL
           INTRODUZCA 1 PARA USAR LA FUNCION PRIMOS
           INTRODUZCA 2 PARA USAR LA FUNCION DIVISOR""")
#==============================================================================================================#
while a=="0":                                                                                                    #
    imprimirmatriz(matrix_octal(),0)                                                                           #
    i=int(input("*******************INTRODUSCA EL NUMERO DE FILA*******************\n"))                       #
    j=int(input("******************INTRODUSCA EL NUMERO DE COLUMNA*****************\n"))                       #
    x=matrizasterisco(i,j,0)                                                                                   #
    print(x)                                                                                                   #
    a=int(input("""el dato se encuentra en la variable de nombre "x"                 
            INTRODUSCA "0" SI DESEA REVISAR OTRA MATRIZ OCTAL
            O ESCRIBA CUALQUIER OTRA COSA PARA SALIR"""))
while a=="1":                                                                                                    #                                                                       #
    print("*******************NUMEROS QUE NO SON PRIMOS*******************\n")                                 #
    print("******************************************************************\n")                              #                                                                                                 #
    imprimirmatriz(Primos(),0)                                                                                 #
    a=int(input("""el dato se encuentra en la variable de nombre "y"                          
            INTRODUSCA "0" SI DESEA REVISAR OTRA MATRIZ OCTAL
            O ESCRIBA CUALQUIER OTRA COSA PARA SALIR"""))                                                      #
while a=="2":                                                                                                    #
    imprimirmatriz(matrix_octal(),0)                                                                           #
    divi=int(input("*******************INTRODUSCA EL DIVISOR*******************\n"))                           #
    z=multiplo(matrix_decimal(),divi)                                                                          #
    imprimirmatriz(z,0)                                                                                                   #
    a=int(input("""el dato se encuentra en la variable de nombre "z"                 
            INTRODUSCA "2" SI DESEA REVISAR OTRA MATRIZ OCTAL
            O ESCRIBA CUALQUIER OTRA COSA PARA SALIR"""))
#==============================================================================================================#

#def matrices(ma1, ma2,i,j,i1,j1):
#    if i==len(ma1):
#        return ma1
#    elif j==len(ma1[i]):
#        return matrices(ma1, ma2,i+1,0,i1,j1)
#    elif 

#Producto escalar auxiliar
#def producto_escalar_aux(vec, num, i, n, result):                   
#    if i == n:                                               
#        return result                                        
#    else:                                                    
#        result.append(vec[i] * num)                          
#        return producto_escalar_aux(vec, num, i +1, n, result)
#def suma(vector,i,resu):
#    if i=vector:
#        return resu
#    else:
#        return (vector,i+,resu[vector])
#def vertical(y,j,result):                                                 #SACA LOS VERTICALES                                                     #
#    if (i,j,result):                                                      #                                                                        #
#        if y==8:return result                                             #CUANDO SE ACABA LA LISTA RETORNA EL RESULTADO                           #
#        else:return vertical(y+1,j,result+[matrix_octal()[y][j]])         #G

