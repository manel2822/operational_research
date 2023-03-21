# -*- coding: utf-8 -*-
"""
Created on Wed Jun 9 18:13:08 2021

@author:manel

"""


from tkinter import *
import pandas as pd
import numpy as np
from pulp import *


#creation de la fenetre
window =Tk()
a=[]
window.title("L'application de Recouvrement minimum")
window.geometry('1080x600')
window.minsize(480,480)
window.config(background='#e0e0e0')
label_title = Label(window, text="Bienvenue sur l'application",font=("Couurrier",35),fg=('#78004A'),bg=("white"))
label_title.pack()



#creatin de l' entérée de n :nombra des somemets
def nget():
  
    usern=nlabel.get()
    print(usern)
    n=int(usern)
    return(n)


label_n = Label(window,text="Entrer le nombre de sommets :",font=("Couurrier",12),fg=('white'),bg="#CC629E")
label_n.place(x=50,y=100)

nlabel=Entry(window,font=("Couurrier",14),fg=("#872A3D"),bg='white',width=5)
nlabel.place(x=280,y=100)


#creatin de l' entérée de m :nombra des aretes
def mget():
    
    userm=mlabel.get()
    print(userm)
    m=int(userm)
    return(m)
    
label_m = Label(window, text="Entrer le nombre d'arêtes        :",font=("Couurrier",12),fg=('white'),bg="#CC629E")
label_m.place(x=50,y=135)

mlabel=Entry(window,font=("Couurrier",14),fg=("#872A3D"),bg='white',width=5)
mlabel.place(x=279,y=135)


#fonction  go_to_next_entry :  faire déplacer le curseur de " nlabel"  vers " mlabel"

def go_to_next_entry(event, entry_list, this_index):
              next_index = (this_index + 1) % len(entry_list)
              entry_list[next_index].focus_set()
entriess = [child for child in window.winfo_children() if isinstance(child, Entry)]
for idx, entry in enumerate(entriess):
        entry.bind('<Return>', lambda e, idx=idx: go_to_next_entry(e, entriess, idx))



text_var = []
entries = []
matrix =[] 



def get_mat():
    if (mlabel.get() != '') &  (mlabel.get() != ''):
        
        rows, cols = (nget(),mget())
        for i in range(rows):
            matrix.append([])
            for j in range(cols):
                matrix[i].append(int(text_var[i][j].get()))
        print(matrix)

def Boxes():
    
      if (mlabel.get() != '') &  (mlabel.get() != ''):
         x2 = 0
         y2 =0
         rows, cols = (nget(),mget())
         for i in range(rows):
    # append an empty list to your two arrays
    # so you can append to those later
            text_var.append([])
            entries.append([])
          
            for j in range(cols):
        # append your StringVar and Entry
                text_var[i].append(StringVar())
                entries[i].append(Entry(window, textvariable=text_var[i][j],width=3))
                
                entries[i][j].place(x=700+ x2, y=120+ y2)
                x2 += 20
              
            y2 += 20
            x2 = 0
     
        ##fonction  go_to_next_entry :  faire déplacer le curseur automtiquement dans les cases de la matrices"
         def go_to_next_entry(event, entry_list, this_index):
              next_index = (this_index + 1) % len(entry_list)
              entry_list[next_index].focus_set()

         entriess = [child for child in window.winfo_children() if isinstance(child, Entry)]
         for idx, entry in enumerate(entriess):
             entry.bind('<Return>', lambda e, idx=idx: go_to_next_entry(e, entriess, idx))
   
      else:
          messagebox.showinfo("my message","veuillez vérifier les donnés saisies") 
          
          



           
def Boxclear():
     cnv = Canvas(window, width=220,highlightthickness=0,height=200,bg="#e0e0e0")
     cnv.place(x=700,y=120)

#fonction  Boxes_ex :pour la relie avec la fonction exemple et efficher un exemple prédifinie de recouvrement 
def Boxes_ex():
    
   
     
    x2 = 0
    y2 =0
    rows = []
    vect=[1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,1,1]
    k=0
    for i in range(7):
    
        cols = []

        for j in range(7):

            e = Entry(relief=GROOVE,width=3)
            
            e.place(x=700+ x2, y=120+ y2)

            e.insert(END,vect[k])
        
            cols.append(e)
            x2 += 20
            k=k+1   
        y2 += 20
        x2 = 0
        
        rows.append(cols)
        
    
        



#fonction exemple        
def ex():
    mlabel.delete(0,END)
    nlabel.delete(0,END)
    sortex.delete(0,END)
    sortez.delete(0,END)
    sorteR.delete(0,END)
    Boxes_ex()
    mlabel.insert(0,7)
    nlabel.insert(0,7)
    def go_in(event):
        
         sortez.insert(0,4)
         vect=[1,0,1,0,0,1,1]
         sortex.insert(0,"[")
         sortex.insert(1,vect)
         sortex.insert(15,"]")
         sorteR.insert(0,"{X_1 , X_3 , X_6 , X_7}")
    vect.bind("<Enter>", go_in)
   
    
entrematr=Button(window,text=" Entrer la matrice d'incidence :",command=Boxes,bg="#CC629E",fg=('white'),font=("Couurrier",12))
entrematr.place(x=470,y=110)

# fonction de nouveau pour recommencer

def nv():
   
    mlabel.delete(0,END)
    nlabel.delete(0,END)
    sortex.delete(0,END)
    sortez.delete(0,END)
    sorteR.delete(0,END)
    Boxclear()
    messagebox.delete() 
  
   

def model_sol(): 
    
    if (mlabel.get() != '') &  (mlabel.get() != ''):
        
        rows, cols = (nget(),mget())  
        rows, cols = (nget(),mget())
        for i in range(rows):
            matrix.append([])
            for j in range(cols):
                matrix[i].append(int(text_var[i][j].get()))
        for i in range(rows):
           for j in range(cols):
              if  int(text_var[i][j].get())!=1:
                    if  int(text_var[i][j].get())!=0:
                       messagebox.showinfo("Erreur","veuillez vérifier les donnés saisies")
                       nv()
                       messagebox.delete()
                  
        for i in range(rows):
            
            som=0
            for j in range(cols):
                
                som= (int(text_var[i][j].get()))+som
            if  som==0:
                
                 messagebox.showinfo("Erreur","veuillez vérifier les donnés saisies \n Le graphe ne doit pas contenir un sommet isolé")
                 nv()
                 messagebox.delete() 
                              
        else:
                         
               model = LpProblem("Problème de recouvrement\n", LpMinimize)   

 
               var_names = [str(j) for j in range(1,cols+1) ]    
               var_names.sort()

               DV_variables = LpVariable.matrix("x", var_names,0,1 ,LpBinary)
               allocation = np.array(DV_variables)


               obj_func =lpSum  (allocation[j] for j in range(cols) ) 
               model +=  obj_func 

               for i in range(rows): 
                     c1= lpSum((allocation[j] *matrix[i][j] )for j in range(cols)) >= (1)
                     model += c1     
 
               model.solve(PULP_CBC_CMD())
               status =  LpStatus[model.status]
               print (model)   
               Z=int( model.objective.value())
        
               S=[]
               sortez.insert(0,Z)
       
               i=0
               for v in model.variables():
                  try:
                      S.insert(i,int(v.value()))
                      i=i+1
                  except:
                        print("error couldn't find value")
               sortex.insert(0,"[")        
               sortex.insert (1,S)
               sortex.insert(len(S)+15,"]")
               X=[]
               i=0
               for v in model.variables():
                  try:  
                        if v.value()!= 0 :
                           X.insert(i,(v.name))
                           i=i+3
                  except:
                        print("error couldn't find value")
               sorteR.insert(0,X)
# fonction close_window                
def close_window():
    window.destroy()


Ex= Button(window ,text="Exemple",font=("Couurrier",14),fg=('white'),bg='#CC629E',command=(ex),width=8,height=1)
Ex.place(x=75,y=520)


vect = Button(window, text="Trouver le recouvrement minimum ",font=("Couurrier",20),bg="#78004A",fg=('white'),command=model_sol,width=27)
vect.place(x=250,y=250)


vecteur = Label(window, text="Solution X*: ",font=("Couurrier",15),fg=('white'),bg="#ff77a9")
vecteur.place(x=270,y=320)

sortex=Entry(window,font=("Couurrier",16),fg=("#872A3D"),bg='#F2F0F1',width=22)
sortex.place(x=400,y=320)

Zmin= Label(window, text="Le cardinel  de recouvremet minimum :        ",font=("Couurrier",15),fg=('white'),bg="#ff77a9")
Zmin.place(x=270,y=370)

sortez=Entry(window,font=("Couurrier",16),fg=("#872A3D"),bg='#F2F0F1',width=20)
sortez.place(x=669,y=370)

R= Label(window, text="Les aretes Xi qui forment ce recouvrement :",font=("Couurrier",15),fg=('white'),bg="#ff77a9")
R.place(x=270,y=419)

sorteR=Entry(window,font=("Couurrier",16),fg=("#872A3D"),bg='#F2F0F1',width=20)
sorteR.place(x=669,y=419)


Nv = Button(window, text="Nouveau",font=("Couurrier",14),fg=('white'),bg="#CC629E",width=8,height=1,command=nv)
Nv.place(x=205,y=520)

quite = Button(window, text="Quitter",font=("Couurrier",14),fg=('white'),bg="#CC629E",width=8,height=1,command=close_window)
quite.place(x=910,y=520)


window.mainloop()
