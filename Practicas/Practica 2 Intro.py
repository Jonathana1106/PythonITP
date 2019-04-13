


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

def multi(num1, num2):
    if (isinstance(num1, int) or isinstance(num1, float)) and (isinstance(num2, int)):
        if num1 == 0:
            return 0
        elif num2 == 0:
            return 1
        elif num1 > 0 and num2 > 0:
            return multi_aux2M(num1, num2)
        elif num1 < 0 and num2 < 0:
            return multi_aux2m(abs(num1), num2)
        elif num1 > 0 and num2 < 0:
            return multi_aux1p(num1, abs(num2))
        elif num1 < 0 and num2 > 0:
            return multi_aux1n(num1, num2)
    #else:
    return "Error, introduzca valores numericos"

def multi_aux2M(num1, num2):
    if num2 == 0:
        return 0
    else:
        return num1 + multi_aux2M(num1, num2-1)

def multi_aux2m(num1, num2):
    if num2 == 0:
        return 0
    else:
        return num1 + multi_aux2m(num1, num2+1)

def multi_aux1p(num1, num2):
    if num2 == 0:
        return 0
    else:
        return num1 + (multi_aux1p(num1, num2+1))

def multi_aux1n(num1, num2):
    if num2 == 0:
        return 0
    else:
        return num1 + multi_aux1n(num1, num2-1)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

#def invertir(num):
 #   if isinstance(num, int):
  #      if 10> num >= 0:
   #         return num
    #    elif num >= 10:
     #       return invertir_auxm10(num)

    #return "Error"

#def invertir_auxm10(num):
 #   if n = len("num"):
  #      if 

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

def suma_dig(num):
    if isinstance(num, int):
        if num == 0:
            return 0
        elif num > 0:
            return suma_aux(num)
        else:
            return "Error"
    elif isinstance(num, float):
        if num == 0:
            return 0
        elif num > 0:
            return suma_auxf(num*100)
        else:
            return "Error"

def suma_aux(num):
    if num == 0:
        return 0
    else:
        return num%10 + suma_aux(num//10)

def suma_auxf(num):
    if num == 0:
        return 0
    else:
        return num%10 + suma_auxf(num//10)

        
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
            
def palindromo(num):
    if isinstance(num, int):
        if num >0 and num < 10:
            return True
        elif num >= 10 and num <= 100:
            if num//10 == num%10:
                return True
            else:
                return False
        elif num >= 100 and num < 1000:
            if (num//100) == (num%10):
                return True
            else:
                return False
        else:
            return palindromo_aux(num, (len("num")-1))
    else:
        return "Error"

def palindromo_aux(num, n):
    if num >= 1000:
        if num < 1000:
            return True
        elif (num//(10**n) == (num%10)):
            return palindromo_aux(((num%(10**(n)))//10), n-1)
        else:
            return False
    else:
        return "Error"
        

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

def multdig(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        if len("num1") == len("num2"):
            return multidig(num1, num2, 0)
        else:
            return "Error, el tama;o del los numeros debe de ser igual"
    else:
        return "Error"

def multidig(num1, num2, n):
    if num1 == 0:
        return 0
    elif ((num1%10) * (num2%10)) >= 10:
        return ((((num1%10) * (num2%10))%10)*10**n) + multidig(num1//10, num2//10, n+1)
    else:
        return (((num1%10) * (num2%10))*10**n) + multidig(num1//10, num2//10, n+1)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

def shift(num):
    if isinstance(num, int):
        return auxk(num, (len("num")))
    else:
        return "Error"

def auxk(num, n):
    j = ((((num)%10)*10**n) + (num//10))
    return j, n

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

def sumatoria(n):
    if isinstance(n, int):
        if n == 0:
            return 0
        else:
            return suma_aux(n, 0)
    else:
        return "Error"

def suma_aux(n, i):
    if i > n:
        return 0
    else:
        return i + suma_aux(n, i+1)
        
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

def num_append(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        return aux(num1, num2, len("num2"))
    else:
        return "Error"

def aux(num1, num2, n):
    if num2 == 0:
        return 0
    else:
        return ((num1*10)+(num2//n)) + aux(num1, num2//10)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

def digitos(num):
    if isinstance(num, int):
        if num == 0:
            return (0, 0)
        else:
            return auxM5(num), auxm5(num)
    return "Error"

def auxM5(num):
    if num == 0:
        return 0
    elif num%10 >= 5:
        return 1 + auxM5(num//10)
    else:
        return auxM5(num//10)

def auxm5(num):
    if num == 0:
        return 0
    elif num%10 < 5:
        return 1 + auxm5(num//10)
    else:
        return auxm5(num//10)
    
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

def num_primos(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        return auxn1(num1) + auxn2(num2)
    else:
        return "Error"

def auxn1(num1):
    if num1 == 0:
        return 0
    elif (num1%10)%2 == 0:
        return 1 + auxn1(num1//10)
    else:
        return auxn1(num1//10)
def auxn2(num2):
    if num2 == 0:
        return 0
    elif (num2%10)%2 == 0:
        return 1 + auxn2(num2//10)
    else:
        return auxn1(num2//10)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

    
    
