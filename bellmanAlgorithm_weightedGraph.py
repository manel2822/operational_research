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

def copy(dict1,dict2):
    for i in range(len(dict1["valeur"])):
        dict1["valeur"][i] = dict2["valeur"][i]
    return dict1["valeur"]

#les algorithme 



#_______ algorithme de djikstra ___________
def djikstra(MV):
    
    dict1 = {
      "valeur": [0],
      "marquer": [1]
    }
    a=0
    for i in range(len(MV)-1):
        dict1["valeur"].append(MV[0][i+1])
        dict1["marquer"].append(0)
    while test(dict1):
        val= inf
        for i in range(len(MV)):
            if (dict1["marquer"][i]==0 and dict1["valeur"][i]<=val):
                val=dict1["valeur"][i]           
                a=i
                
                
        dict1["marquer"][a]=1
        for j in range(len(MV)):
            if (dict1["marquer"][j]==0):
                if(dict1["valeur"][a]+MV[a][j]<dict1["valeur"][j]):
                    dict1["valeur"][j]=dict1["valeur"][a]+MV[a][j]
                      
    return dict1["valeur"]


#_______ algorithme de bellman ___________
def bellman(MV):

    dict1 = {
      "valeur": [0]
      
    }
    dict2 = {
      "valeur": [inf]
      
    }
    for i in range(len(MV)-1):
        dict1["valeur"].append(inf)
        dict2["valeur"].append(inf)
          
    while(dict1["valeur"]!= dict2["valeur"]):
        dict2["valeur"]=copy(dict2,dict1)
        
        for i in range(len(MV)):
            for j in range(len(MV)):
                if (dict1["valeur"][i]+MV[i][j ]< dict1["valeur"][j]):
                    dict1["valeur"][j]=dict1["valeur"][i]+MV[i][j]
        
    return dict1["valeur"]

#_______ algorithme de bellman_long  ___________
def bellman_long(MV):
    
    dict1 = {
      "valeur": [0.0]
      
    }
    dict2 = {
      "valeur": [-inf]
      
    }
    for i in range(len(MV)-1):
        dict1["valeur"].append(-inf)
        dict2["valeur"].append(-inf)
          
    while(dict1["valeur"]!= dict2["valeur"]):
        dict2["valeur"]=copy(dict2,dict1)
        
        for i in range(len(MV)):
            for j in range(len(MV)):
                if (dict1["valeur"][i]+MV[i][j ]> dict1["valeur"][j]):
                    dict1["valeur"][j]=dict1["valeur"][i]+MV[i][j]
        
    return dict1["valeur"]


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
#__________________Graphe valués____________________________

def add_vertex(v):
  global graph
  global vertices_no
  global vertices
  if v in vertices:
    print("Vertex ", v, " already exists")
  else:
    vertices_no = vertices_no + 1
    vertices.append(v)
    if vertices_no > 1:
        for vertex in graph:
            vertex.append(0)
    temp = []
    for i in range(vertices_no):
        temp.append(0)
    graph.append(temp)
def add_edge(v1, v2, e):
    global graph
    global vertices_no
    global vertices
  
    if v1 not in vertices:
        print("Vertex ", v1, " does not exist.")
  
    elif v2 not in vertices:
        print("Vertex ", v2, " does not exist.")
   
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e

def print_graph():
  global graph
  global vertices_no
  for i in range(vertices_no):
    for j in range(vertices_no):
      if graph[i][j] != 0:
        print(vertices[i], " -> ", vertices[j], \
        " edge weight: ", graph[i][j])


vertices = []

vertices_no = 0
graph = []

neighbour=[]
#______________ Affichage des resultats __________________

cprint('******************************************************************************************', 'cyan', 'on_grey')
cprint('                  "Bienvenue """ Problèmes de cheminement et applications""""             ', 'cyan', 'on_grey')
cprint('******************************************************************************************', 'cyan', 'on_grey')
sort=False
while sort==False:
    print("\n vous devez choisir un des choix suivants en entrant le numéro correspondant:\n ")
    print("1 :Problème des Graphes valué\n ")
    print("2: Problème du plus court chemin\n ")

    choix=input()
    if choix=="1":
        cprint('**************************************************************************', 'blue', 'on_grey')
        cprint('                    "1-  Problème des Graphes valués"                     ', 'blue', 'on_grey')
        cprint('***************************************************************************', 'blue', 'on_grey')
        print("\n\n")
        cprint('**********************************Aide:*************************************', 'white', 'on_grey')   
        print("----------------------------------------------------------------------")
        print("| Maintenant nous voulons construire notre  matrice d'adjascence      |")       
        print("| Vous devez entrer n le nombre des sommets.                          |")
        print("| Donner le cardinale d'ensemble des voisinage de chaque sommet       |")
        print("| Pour chaque sommet :                                                | ")
        print("| Entrer le numero de sommet adjascent et le poids d'arc correspondant| ")
        print("| Mi,j=0 si il n'y pas d'arcs/arêtes reliant i à j                    | ")
        print("| Mi,j=valuation de l'arc/arête {i, j}                                | ")
        print("-----------------------------------------------------------------------")




        n=int(input("Entrer le nombre des sommets : "))
        for i in range (n):
            add_vertex(i)
            m=int(input(f"entre le nombre des voisins de ce sommet{i} : "))
            neighbour.append(m)

        for i in range (n):
            for j in range (neighbour[i]):
                v=int(input(f"entrer le numero de sommet adjascente a ce sommet{i} :"))
                p=int(input("entrer le poid  d'arc correspondant : "))
                add_edge(i, v, p)
              

        print_graph()
        print("Internal representation: ", graph)

        print("\n vouler vous sortir : tapez 0 ")
        s=input()
        if s=="0":
             break

    if choix=="2":
        cprint('************************************************************************', 'blue', 'on_grey')
        cprint('                  "2-  Problème du plus court chemin"                   ', 'blue', 'on_grey')
        cprint('************************************************************************', 'blue', 'on_grey')
        print("\n vous devez choisir un des choix suivants en entrant le numéro correspondant:\n ")
        print("1 :algorithme de Bellman\n ")
        print("2: algorithme de Dijkstra\n ")
        print("3:Application d'ordonnancement\n ")
        print("4: algorithme de Prim\n ")
        choix=input()
        if choix=="1":
            print(termcolor.colored(pyfiglet.figlet_format("Bellman "), color="cyan"))
            cprint('****************************Aide:************************************', 'white', 'on_grey')   
            print("-----------------------------------------------------------------")
            print("| Maintenant nous allons construire notre : matrice d'adjascence |")       
            print("| Vous dever entrer n le nombre des sommets et les poids des arcs|")
            print("| Si le sommet x , le sommet y ne sont pas adjascents tapez inf  | ")
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
            
            print("le plus court chemein par bellamn est : ", bellman(MV))


            print("\nvouler vous sortir : tapez 0 ")
            s=input()
            if s=="0":
             break
        
        elif choix=="2":
            print(termcolor.colored(pyfiglet.figlet_format("Dijkstra "), color="cyan")) 
            cprint('****************************Aide:*******************************', 'white', 'on_grey')   
            print("-----------------------------------------------------------------")
            print("| Maintenant nous allons construire notre matrice d'adjascence   |")       
            print("| Vous dever entrer le nombre des sommets et les poids des arcs  |")
            print("| Si le sommet x , le sommet y ne sont pas adjascents tapez inf  | ")
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

            print("le plus court chemein par djikstra est : ", djikstra(MV))

            print("\nvouler vous sortir : tapez 0 ")
            s=input()
            if s=="0":
                break


        elif choix=="3":
            print(termcolor.colored(pyfiglet.figlet_format("Ordonancement"), color="cyan"))
            cprint('******************************Aide:*********************************', 'white', 'on_grey')   
            print("-----------------------------------------------------------------")
            print("| Maintenant nous allons construire notre : matrice d'adjascence |")       
            print("| Vous dever entrer n le nombre des sommets et les poids des arcs|")
            print("| Si le sommet x et le sommet y ne sont pas adjascents tapez -inf| ")
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

            print("le plus long chemein par bellman_long est : ", bellman_long(MV))

            print("\nvouler vous sortir : tapez 0 sinon 1")
            s=input()
            if s=="0":
             break

        elif choix=="4":
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

            print("\nvouler vous sortir : tapez 0")
            s=input()
            if s=="0":
             break
           



