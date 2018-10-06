# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 19:39:48 2018

@author: edoua
"""

def inverse(A):
    """permet de renvoyer la chaine de caractère dans l'ordre inverse"""
    K=""
    for i in range(len(A)-1,-1,-1):
        K = K+A[i]
    return(K)
    
def palindrome(n):
    """permet de tester si un nombre est palindromique"""
    L=str(n)
    P=inverse(L)
    if P == L:
        return True
    return False

assert(palindrome(132231))

def test(x):
    """indique si le nombre est un nombre de Lychrel"""
    i = 0
    while True :
        x += int(inverse(str(x)))
        if not palindrome(x):
            i += 1
        else:
            return False
        
        if i > 50 :
            return True

        
def resolution(n):
    """resout le probleme 55 du projet Euler"""
    c=0
    for k in range(1,n):
        if test(k):
            c+=1
    return(c)

print(resolution(10000))


