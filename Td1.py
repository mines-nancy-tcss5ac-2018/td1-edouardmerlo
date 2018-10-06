# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:22:50 2018

@author: edouard
"""
"""probleme 16"""

def sumdigit(n):
    """somme les chiffres du nombre, solution du problème Euler 16"""
    d=0
    for k in str(n):
        """on cree la chaine de caractère correspondant au nombre"""
        d=d+int(k)
    return d

#assert(sumdigit(15) == 6)
#print(sumdigit(2**1000))

def recsolve(x):
    """version par récurrence de l'algo précédent"""
    ratio, rem = divmod(x, 10)
    """permet de recuperer quotient et reste à la fois"""
    return rem + recsolve(ratio) if ratio !=0 else rem
#
#print(recsolve(2**1000))

"""debut probleme 22"""

def extraction(nomfichier):
    """ouvre le fichier, supprime les guillements"""
    listenoms=[]
    fichier=open(nomfichier,'r')
    for ligne in fichier:
        for presqnoms in ligne.split(','):
            listenoms.append(presqnoms[1:len(presqnoms)-1])
    return(listenoms)
    fichier.close()

def triliste(L):
    """trie la liste dans l'ordre lexicographique"""
    return(sorted(L))

#print(triliste(extraction('names.txt')))

def score(nom):
    return sum(ord(c)-(ord('A')-1) for c in nom)

assert(score('ABA')==4)


list=['ABA','BAC']
for c,value in enumerate(list):
    print(c,value)

def resol22(nomfichier):
    """resolution du problème 22"""
    """l'erreur à corrige concernait l'indice, qui commençait à 0"""
    S = 0
    for i, nom in enumerate(triliste(extraction(nomfichier))):
        S+=score(nom)*(i+1)
    return S

print(resol22('names.txt'))