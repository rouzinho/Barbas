#!/usr/bin/python
import tkinter
from tkinter import *
from tkinter.ttk import *
from Compte import *
from graphique import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class Statistiques(tkinter.Tk):
	
	def __init__(self, parent):
		tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.valeur = StringVar()	#fenetre du haut
		self.list_ch = []	
		self.dico = []
		self.val_list = StringVar()
		self.fenetre_graphe = Frame(self,borderwidth=2,relief=GROOVE)
		self.fenetre_gauche = Frame(self,width=300,height=700,borderwidth=2,relief=GROOVE)
		self.fenetre_haut = Frame(self.fenetre_gauche,borderwidth=2)
		self.liste = Combobox(self.fenetre_haut,textvariable=self.val_list,values=self.list_ch,state='readonly',postcommand=self.up_list)
		self.fig = affichage_diagramme('test')
		self.canvas = FigureCanvasTkAgg(self.fig, master=self.fenetre_graphe)
		self.initialize()

	def initialize(self):
		#fenetre_graphe = Frame(main_fenetre,borderwidth=2,relief=GROOVE)	#Frames generales
		
		
		fenetre_centre = Frame(self.fenetre_gauche,borderwidth=2,relief=GROOVE)
		fenetre_bas = Frame(self.fenetre_gauche,borderwidth=2,relief=GROOVE)

		new_val = Entry(self.fenetre_haut,textvariable=self.valeur,width=15)
		new_val.config(font=('Inconsolata',16,'bold'))
		nouveau = Button(self.fenetre_haut,text='NOUVEAU',command=self.ajout_list)	
		lancer = Button(self.fenetre_haut,text='LANCER',command=self.lancement)
		arreter = Button(self.fenetre_haut,text='ARRETER')
		arreter.config(state=DISABLED)
		
		new_val.grid(row=1,column=1)
		nouveau.grid(row=1,column=2)
		self.liste.grid(row=2,column=1)
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
		
		self.canvas.get_tk_widget().pack()
		self.canvas.show()
		
		self.fenetre_graphe.pack(side=RIGHT)
		self.fenetre_haut.pack(side=TOP,padx=7,pady=50)
		fenetre_centre.pack(padx=7,pady=50)
		fenetre_bas.pack(side=BOTTOM,padx=10,pady=50)
			
		self.fenetre_gauche.pack(side=LEFT,padx=8,pady=20)
		self.geometry('1100x700+150+50')
		self.update()

	def ajout_list(self):
		val = self.valeur.get()
		if val != '':
			modele(val)

	def up_list(self):
		dico = []
		self.list_ch = get_modele()
		for i in self.list_ch:
			mot = i.split()
			dico.append(mot[0])
		self.liste['values'] = dico

	def lancement(self):
		v = StringVar()
		v = self.liste.get()
		self.fig.clear()
		self.fig = affichage_camembert("Test")
		self.canvas.get_tk_widget().destroy()
		self.canvas = FigureCanvasTkAgg(self.fig,master=self.fenetre_graphe)
		self.canvas.get_tk_widget().pack()
		self.canvas.draw()

if __name__ == '__main__':
	app = Statistiques(None)
	app.title('Statistiques')
	app.mainloop()