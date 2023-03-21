import matplotlib.pyplot as plt
import numpy as np

P=[] #matrice P  a remplir
T1=[]#T1 vecteur contient le nom des tache qui seront traitées sur machine 1
T2=[]#T2 vecteur contient le nom des tache qui seront traitées sur machine 2
T1_matrix=np.array(T1)
T2_matrix=np.array(T2)
t1=0
t2=0

n=int(input("Entrer le nombre des taches T "))
print("On a la nombre des machines M =2")

Gant=[]#Gant diagramme a affiché  a la fin de traitemant
for j in range (2):
    Gant.append([0]*n)  
    for i in range(n):
        Gant[j][i]=0


#remplissage de P
for i in range (n):
    P.append([0]*2)  
    for j in range(2):
        P[i][j]=int(input(f"le temps de traitement de la tache T{i+1} dans la machine M{j+1}  :"))

print("\n Le resultat :\n") 
#On traite la tache ayant le plus long temps de traitement sur l’autre machine.

for K in range (n):
    j=0
    while j <2 : 
        
        i=0
        max=0
        while i<n :
            if ( j==0 and i not in T1):
                if(P[i][j]>max):
                    max=P[i][j]
                    k=i
                    h=j
            elif (j==1 and i not in T2):    
                if(P[i][j]>max):
                    max=P[i][j]
                    k=i
                    h=j  
            i=i+1
        if (j==0):    
            T1.insert(t1,k)
            print(f" Le traitemet de la tache T{k+1} sur la machine M{1-h+1}  dans un temps{P[k][1-h]}")
            Gant[j][t1]=P[k][1-h]
            t1=t1+1
        else : 
            T2.insert(t2,k)
            print(f" Le traitemet de la tache T{k+1} sur la machine M{1-h+1}  dans un temps{P[k][1-h]}")
            Gant[j][t2]=P[k][1-h]
            t2=t2+1
 
        j=j+1

################################################################################################
############################### Le Diagramme de Gant ###########################################
################################################################################################

# Declarer a figure "gnt"
gig,gnt = plt.subplots()

#  Y-axis limits
gnt.set_ylim(0, 30)
 
#  X-axis limits
gnt.set_xlim(0, 40)
 
#labels for x-axis and y-axis
gnt.set_xlabel('temps')

 
# ticks on y-axis
gnt.set_yticks([5,16.5])
# Labelling tickes of y-axis
gnt.set_yticklabels(['Machine 2', 'Machine 1'])
 
# attribut de graphe 
gnt.grid(True)
color = ["turquoise","crimson","orange","black","green","yellow","#d1cfcf","#182ef2","#b305b3"]

# Declarer un bar : gnt.broken_barh([(x, xlengh)], (y, yheight), facecolors =('tab:color'))
j=0
start=0
for i in range(n):
    gnt.broken_barh([(start,start+Gant[j][i])], (j*10,10), facecolors =(color[T1[i]]),label="Tache "+str(T1[i]+1))
    start=Gant[j][i]+start
gnt.broken_barh([(start,start+1)], (j*10,10), facecolors =("white"))    
j=1
start=0
for i in range(n):
    gnt.broken_barh([(start,start+Gant[j][i])], ((j*10)+2,10), facecolors =(color[T2[i]]))
    start=Gant[j][i]+start
gnt.broken_barh([(start,start+1)], ((j*10)+2,10), facecolors =("white"))    


plt.title('Algorithme "O2||Cmax",Regle de LAPT ')
plt.legend()                                                               
plt.show() 
plt.savefig("LAPT.png") 