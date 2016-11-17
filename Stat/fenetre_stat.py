from tkinter import *
from tkinter.ttk import *
from Compte import *
from graphique import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure



def ajout_list():
	val = valeur.get()
	if val != '':
		modele(val)

def up_list():
	dico = []
	list_ch = get_modele()
	for i in list_ch:
		mot = i.split()
		dico.append(mot[0])
	liste['values'] = dico
	
def lancement():
	v = StringVar()
	v = liste.get()
	#fig.clear()
	fig = affichage_camembert("Test")
	canvas.draw()

	

main_fenetre = Tk()

#fenetre_graphe = Frame(main_fenetre,borderwidth=2,relief=GROOVE)	#Frames generales
fenetre_gauche = Frame(main_fenetre,width=300,height=700,borderwidth=2,relief=GROOVE)
fenetre_haut = Frame(fenetre_gauche,borderwidth=2)
fenetre_centre = Frame(fenetre_gauche,borderwidth=2,relief=GROOVE)
fenetre_bas = Frame(fenetre_gauche,borderwidth=2,relief=GROOVE)


valeur = StringVar()	#fenetre du haut
list_ch = []	
dico = []
new_val = Entry(fenetre_haut,textvariable=valeur,width=15)
new_val.config(font=('Inconsolata',16,'bold'))
nouveau = Button(fenetre_haut,text='NOUVEAU',command=ajout_list)	
lancer = Button(fenetre_haut,text='LANCER',command=lancement)
arreter = Button(fenetre_haut,text='ARRETER')
arreter.config(state=DISABLED)
val_list = StringVar()
liste = Combobox(fenetre_haut,textvariable=val_list,values=list_ch,state='readonly',postcommand=up_list)
new_val.grid(row=1,column=1)
nouveau.grid(row=1,column=2)
liste.grid(row=2,column=1)
lancer.grid(row=2,column=2)
arreter.grid(row=4,column=3)

numero = Label(fenetre_centre,text="06 03 81 78 36",width=120)	#fenetre du milieu
numero.config(font=('Inconsolata',37,'bold'))
numero.pack()

liste_graph = Listbox(fenetre_bas,width=20,height=10)	#fenetre du bas
afficher = Button(fenetre_bas,text='AFFICHER')
ou = Label(fenetre_bas,text='ou')
affi = Label(fenetre_bas,text='Afficher')
fct = Label(fenetre_bas,text=' en fonction de ')
liste_graph.grid(row=1,column=1)
afficher.grid(row=1,column=3)

#zone_dessin = Canvas(main_fenetre, width=600, height=600) #Définit les dimensions du canevas
#fig = affichage_camembert("Test")
#fig = affichage_diagramme("Test")
fig = Figure()
canvas = FigureCanvasTkAgg(fig, master=main_fenetre)
canvas.show()
canvas._tkcanvas.pack(side=RIGHT)
#zone_dessin.pack(side=RIGHT) #Affiche le canevas
	
	
main_fenetre.geometry('1100x700+150+50')
fenetre_haut.pack(side=TOP,padx=7,pady=50)
fenetre_centre.pack(padx=7,pady=50)
fenetre_bas.pack(side=BOTTOM,padx=10,pady=50)
	
fenetre_gauche.pack(side=LEFT,padx=8,pady=20)


main_fenetre.mainloop()




