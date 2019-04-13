#######################################################

def multi(num, num2):
    if not isinstance(num2, int):
        return "Error"
    elif num == 0 or num2 == 0:
        return 0
    if num2<0:
        flag = True
    else:
        flag = False
    num2 = abs(num2)
    r=0
    while num2 != 0:
        r = r + num
        num2 = num2 - 1
    if flag == True:
        r = -1*r
    return r

######################################################
    
##    elif (num > 0 and num2 > 0) or ( num < 0 and num2 <0):
##        r = 0
##        num = abs(num)
##        num2 = abs(num2)
##        while num2 != 0:
##            r = r + num
##            num2 = num2 - 1
##        return r
##    elif num < 0 and num2 > 0:
##        r = 0
##        while num2 != 0:
##            r = r + num
##            num2 = num2  - 1
##        return r
##    else:
##        r = 0
##        while num2 != 0:
##            r = r + num
##            num2 = num2 + 1
##        return r*(-1)

###################################################################

def invertir(num):
    if not isinstance(num, int):
        return "Error"
    elif num < 0:
        n = len(str(abs(num)))-1
        r = 0
        num = abs(num)
        while num != 0:
            r = r  + ((num%10)*10**n)
            n = n - 1
            num = num // 10
        return r*-1
    n = len(str(num))-1
    r = 0
    while num != 0:
        r = r  + ((num%10)*10**n)
        n = n - 1
        num = num // 10
    return r

#################################################################

def finvertir(num):
    if not isinstance(num, int):
        return ""
    n = str(num)
    invertido = ""
    for nnum in n:
        invertido = nnum+invertido
    return int(invertido)
        
    
#################################################################

def suma_dig(num):
    if isinstance(num, float):
        while (num%1) != 0:
            num = num * 10
        num = int(num)
    if isinstance(num, int):
        r = 0
        while num != 0:
            r = r + (num%10)
            num = num//10
        return r
    else:
        return "Error"
        
################################################################
        
def palindromo(num):
    if not isinstance(num, int):
        return "Error"
    n = len(str(num))-1
    while (num//(10**n)) == (num%10):
        num = (num%(10**n))
        num = num//10
        n = n-2
        if num == 0:
            return True
    return False

##################################################################

def multi_dig(num, num2):
    if not isinstance(num, int) or not isinstance(num2, int):
        return "Error"
    n = 0
    rt = 0
    while num != 0:
        r = ((num%10 )*(num2%10))
        if r >= 10:
            r = (r%10)*(10**n)
            rt = rt + r
        else:
            rt = rt + (r*(10**n))
        num = num//10
        num2 = num2//10
        n = n+1
    return rt
    
#####################################################################

def num_append(num1, num2):
    if not isinstance(num1, int) or not isinstance(num2, int):
        return "Error"
    elif num2 == 0:
        return num1*10
    while len(str(num2)) != len("0"):
        num1 = (num1*(10)) + (num2//(10**(len(str(num2))-1)))
        num2 = (num2%(10**(len(str(num2))-1)))
    return num1

##################################################################

def div(dig, num):
    if not isinstance(num, int) and not isinstance(dig, int) and dig < 0 and dig > 9:
        return "Error"
    r = 0
    while num != 0:
        r = (r*(10)) + int(((num//(10**(len(str(num))-1)))/dig))
        num = (num%(10**(len(str(num))-1)))
    if num == 0:
        return r*10
    else:
        return r

###################################################################
        
def digitos(num):
    if not isinstance(num, int):
        return "Error"
    elif num == 0:
        return 0, 1
    M = 0
    m = 0
    while num != 0:
        if num%10 <= 5:
            m = m + 1
        else:
            M = M + 1
        num = num//10
    return M, m

######################################################################

def C(n, k):
    if isinstance(n, int) and isinstance(k, int) and n > 0 and k > 0 and n >= k:
        return (factorial(n))/((factorial(k))*(factorial(n-k)))
    else:
        return "Error"

def factorial(num):
    if not isinstance(num, int) and num >= 0:
        return "Error"
    elif num == 0 or num == 1:
        return 1
    r = 1
    while num != 0:
        r = r * num
        num = num -1
    return r

#######################################################################

def hormiguitas(n):
    if isinstance(n, int):
        r = 15
        while n != 0:
            r = (r//2)*3
            n = n - 1
        return r
    else:
        return "Error"

######################################################################

def mitad(num):
    if isinstance(num, int):
        if (len(str(abs(num))))% 2 != 0:
            n = 0
            a = ((len(str(abs(num))))//2)+1
            while a > n:
                r = num%10
                num = num//10
                n = n+1
            return r
        else:
            return 0
    else:
        return "Error"

#####################################################################
                
def shift(num):
    if isinstance(num, int):
        n = (len(str(num))-1)
        r = (num%10)*(10**n) + (num//10)
        return r
    else:
        return "Error"

###################################################################
                
##############################################################################

def digitos(num):
    if not isinstance(num, int):
        return "Error"
    if num == 0:
        return 1
    dig = 0
    num = abs(num)
    while num != 0:
        num = num//10
        dig = dig + 1
    return dig

###############################################################################

def par(num):
    if not isinstance(num, int):
        return "Error"
    while num != 0:
        # if num % 2 == 0
        # return True
        if (num%10)%2 == 0:
            return True
        # else:
        # num//10
        num = num//10
    return False

#############################################################################

def factorial(num):
    if not isinstance(num, int) and num >= 0:
        return "Error"
    elif num == 0 or num == 1:
        return 1
    r = 1
    while num != 0:
        r = r * num
        num = num -1
    return r

#############################################################################
    
def multiplica(num, num2):
    if not isinstance(num, int) and not isinstance(num2, int):
        return "Error"
    elif num == 0 or num2 == 0:
        return 0
    #r = 0
    elif num > 0 and num2 > 0:
        while num2 != 0:
            r = r + num
            num2 = num2 -1
        return r
     #elif num < 0 and num2 < 0:
       #  return "a"

####################################################

def cuenta(lista):
    if not isinstance(lista, list):
        return "Error"
    c = 0
    for i in range(0, len(lista)):
        c = c + 1
    return c

###################################################

def fibonacci(num):
    if not isinstance(num, int) or num < 0:
        return "Error"
    elif num == 0:
        return 0
    elif num == 1:
        return 1
    r = 0
    while num > 1:
            r = r + fibonacci(num-1) + fibonacci(num-2)
            num = num - num
    return r
        
#####################################################
