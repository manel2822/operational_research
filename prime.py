# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 21:46:28 2022

@author: sg
"""

import numpy as np
import termcolor
import pyfiglet
import sys
from tkinter import *
from termcolor import colored, cprint
from math import inf



def test(dict1):
    nonmarquer= False
    for i in range(len(dict1["marquer"])):
        if dict1["marquer"][i]== 0:
            nonmarquer = True
            break
    return nonmarquer


#________ Algorithme De Prim ______________
def Prim(MV):
    dict1 = {
      "marquer": [1]
    }
    arbre ={
        "arborecence":[],
        "valeur":[]
            }
    a=0
    val= inf
    for i in range(len(MV)-1):
        dict1["marquer"].append(0)
    while test(dict1):
        for i in range(len(MV)):
            val= inf
            a=inf
            b=inf
            for j in range(len(MV)):
                
                if (dict1["marquer"][i] == 0  and dict1["marquer"][j]== 1):
                    if(MV[i][j]<val):
                        val = MV[i][j]
                        a=j
                        b=i
            if(val != inf):
                arbre["arborecence"].append([a,b])
                arbre["valeur"].append(val)
                dict1["marquer"][b]=1
                
    return arbre


print(termcolor.colored(pyfiglet.figlet_format("Prim "), color="cyan"))
cprint('******************************Aide:*********************************', 'white', 'on_grey')   
print("-----------------------------------------------------------------")
print("| Maintenant nous allons construire notre : matrice d'adjascence |")       
print("| Vous dever entrer n le nombre des sommets et les poids des arcs|")
print("| Si le sommet x et le sommet y ne sont pas adjascents tapez  inf| ")
print("| Exemple:                                                       | ")
print("| Si n=4 donc on a une matrice 4*4 remplie par les poids des arcs| ")
print("-----------------------------------------------------------------")
n=int(input("Entrer n : "))
print("entrer les poids correspondant")
i=0
j=1
MV=[]
for i in range (n):
    MV.append([0]*n)  
    for j in range(n):
        MV[i][j]=float(input())

print("L'arbre couvrant de poids minimal est : ", Prim(MV))