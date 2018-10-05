# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:22:50 2018

@author: edouard
"""

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
#


Lignes = []
for ligne in open('names.txt','r'):
    Lignes.append(ligne)
    doc = Lignes[0].split(',')
    doctri=sorted(doc)
#    print(doctri)
#    
def propre(L):
    P=[]
    for x in L:
        if ord(x)!=34:
            P.append(x)
    return(P)

#print(propre(doctri))

def corextract(nomfichier):
    """extrait la liste des noms du fichier et supprime les guillemets de fin et de début"""
    listnoms = []
    for ligne in open(nomfichier, 'r'):
        for presqnoms in ligne.split(','):
            listnoms.append(presqnoms[1:len(presqnoms)-1])
    return listnoms
    
test = corextract('names.txt')
print(test)
    
def score(nom):
    offset=ord('A')-1
    return sum(ord(c)-offset for c in nom)
            
def resol22(nomfichier):
    """Résolution du problème 22"""
    rep = 0
    for index, nom in enumerate(sorted(corextract(nomfichier))):
        rep +=score(nom)*index
    return rep