#TALLER DE PROGRAMACION, 21/03/2013                PROF. EDUARDO CANESSA
#ELIAS GRANADOS
#JONATHAN G ARAYA
#GRUPO 4                                       
#=============================MULTIPLICAR======================================#
def multi(a,b):  #definicion de funcion multiplicar                            #
    if (isinstance(a,int)or isinstance(a, float)) and isinstance(b,int):       #==>Se define las condiciones que deben ser ingresadas para utilizar la funcion
        if b>=0:  #NO ES UNA VARIABLE NEGATIVA                                 #
            if b!=0:                                                           #
                b=b-1                                                          #
                return a+ (multi(a,b))                                         #
            if b==0:  #caso base                                               #
                return 0                                                       #
        if b<0 and a>0:  #EL MULTIPLICADOR ES NEGATIVO                         #
            a=abs(a)                                                           #
            b=abs(b)
            if b!=0:                                                           #
                b=b-1                                                          #
                return -a-(multi(a,b))                                         #
            if b==0:  #caso base                                               #
                return 0                                                       #
                                                                               #
        else:    #LA VARIABLE ES NEGATIVA                                      # 
            a=abs(a)                                                           #
            b=abs(b)                                                           #
            if b!=0:                                                           #
                b=b-1                                                          #
                return a+ (multi(a,b))                                         #
            if b==0:  #caso base                                               #
                return 0                                                       #
    else:                                                                      #
        return "Error:segundo argumento debe ser entero"                       #
                                                                               #
#===============================INVERTIR=======================================#
def invertir(num):    #definicion de funcion invertir                          #
    if isinstance(num,int): #solamente nummeros enteros                        #
                                                                               #
##**********************************************##                             #
        def cue(n):                             ##                             #
            n=abs(n)                            ##sub funcion para acomodo de  #
            if n//10==0:                        ##numeros                      #
                return 1                        ##                             #
            elif n//10!=0:                      ##                             #
                return 10*cue(n//10)            ##                             #
                                                ##                             #
##**********************************************##                             #
        if num>0: #"""Si la variable no es negativa"""                         #
            if (num//10)==0:     #"""caso base"""                              #
                return num                                                     #
            elif(num//10)!=0:                                                  #     
                a=num%10                                                       #
                return a*cue(num)+invertir(num//10)                            #
        else:  #"""En caso de que sea negativa la variable"""                  #
            num=abs(num)                                                       #
            if (num//10)==0:    #"""caso base"""                               #  
                return num                                                     #
            elif(num//10)!=0:                                                  #     
                a=num%10                                                       #
            return -a*cue(num)-invertir(num//10)                               #
    else:                                                                      #
        return "ingrese numero entero"                                         #
                                                                               #
                                                                               #
#===========================PALINDROMO=========================================#
def palindromo(numero): #"""Definicion de funcion """                          #
    if isinstance(numero,int):                                                  #                       
        if numero==invertir(numero):#"comparacion de variable con su "inverso" #
            return True                                                        #
        else:                       #"""resultados booleanos"""                #
            return False                                                       #
    else:                                                                      #
        return "ingrese numero entero"                                         #
#==============================================================================#
                                                                               
                                                                               
                                                                               
                                                                               
                                                                               
                                                                               
                                                                               
                                                    
