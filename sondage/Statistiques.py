# coding: utf-8
import Tkinter 
from Tkinter import *
from ttk import *
from compte import *
from graphique import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from simulation import *
from ConnexionSms import *

class Statistiques(Tkinter.Tk):
	
	def __init__(self, parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.valeur = StringVar()	#fenetre du haut
		self.list_ch = []	
		self.dico = []
		self.val_list = StringVar()
		self.fenetre_graphe = Frame(self,borderwidth=2,relief=GROOVE)
		self.fenetre_gauche = Frame(self,width=300,height=700,borderwidth=2,relief=GROOVE)
		self.fenetre_haut = Frame(self.fenetre_gauche,borderwidth=2)
		self.fenetre_bas = Frame(self.fenetre_gauche,borderwidth=2,relief=GROOVE)
		self.liste = Combobox(self.fenetre_haut,textvariable=self.val_list,values=self.list_ch,state='readonly',postcommand=self.up_list)
		self.arreter = Button(self.fenetre_haut,text='ARRETER',command=self.arret)
		self.lancer = Button(self.fenetre_haut,text='LANCER',command=self.lancement)
		self.liste_graph = Listbox(self.fenetre_bas,width=20,height=10)
		self.new_val = Entry(self.fenetre_haut,textvariable=self.valeur,width=15)
		self.ani = 0
		self.sms = 0
		self.a = 0
		self.initialize()

	def initialize(self):
		
		
		self.fig = plt.figure()
		self.canvas = FigureCanvasTkAgg(self.fig, master=self.fenetre_graphe)
		fenetre_centre = Frame(self.fenetre_gauche,borderwidth=2,relief=GROOVE)
		#self.new_val = Entry(self.fenetre_haut,textvariable=self.valeur,width=15)
		
		self.new_val.config(font=('Inconsolata',16,'bold'))

		#nouveau = Button(self.fenetre_haut,text='NOUVEAU',command=self.ajout_list)	
		
		self.liste.bind("<<ComboboxSelected>>",self.active_lancer)
		
		self.arreter.config(state=DISABLED)
		self.lancer.config(state=NORMAL)
		
		#self.new_val.grid(row=1,column=1)
		#nouveau.grid(row=1,column=2)
		#self.liste.grid(row=2,column=1)
		self.lancer.grid(row=1,column=1)
		self.arreter.grid(row=1,column=2)
		
		question = Label(fenetre_centre,text="Les sciences cognitives vous intéressent ?",width=110)
		question.config(font=('Inconsolata',11))
		suite = Label(fenetre_centre,text="Envoyez Oui Non ou Bof au :",width=110)
		suite.config(font=('Inconsolata',17))
		numero = Label(self.fenetre_bas,text="06 10 84 51 53",width=110)	#fenetre du milieu 
		numero.config(font=('Inconsolata',35,'bold'))
		question.pack()
		suite.pack()
		numero.pack()

			#fenetre du bas
		"""afficher = Button(self.fenetre_bas,text='AFFICHER')
		ou = Label(self.fenetre_bas,text='ou')
		affi = Label(self.fenetre_bas,text='Afficher')
		fct = Label(self.fenetre_bas,text=' en fonction de ')
		self.liste_graph.config(height=18)
		self.liste_graph.config(width=35)
		self.liste_graph.grid(row=1,column=1)
		afficher.grid(row=1,column=3)"""
		
		self.canvas.get_tk_widget().pack()
		self.canvas.show()
		
		self.fenetre_graphe.pack(side=RIGHT)
		self.fenetre_haut.pack(side=TOP,padx=7,pady=50)
		fenetre_centre.pack(padx=7,pady=50)
		self.fenetre_bas.pack(side=BOTTOM,padx=10,pady=50)
			
		self.fenetre_gauche.pack(side=LEFT,padx=8,pady=20)
		self.geometry('1100x700+150+50')
		self.update()

	def ajout_list(self):	#ajoute la valeur saisie à la liste des modalités
		val = self.valeur.get()
		if val != '':
			modele(val)

	def up_list(self):		#met à jour la liste
		dico = []
		self.list_ch = get_modele()
		for i in self.list_ch:
			mot = i.split()
			dico.append(mot[0])
		self.liste['values'] = dico

	def active_lancer(self,event):		#dégrise le bouton lancer lors du choix d'une modalité
		if self.val_list.get() != "":
			self.lancer.config(state=NORMAL)
		print(self.val_list.get())

	def lancement(self):		#lancement de l'affichage dynamique
		self.sms = ConnexionSms()
		self.sms.set_nomfich(self.val_list.get())
		self.arreter.config(state=NORMAL)
		self.sms.start()
		v = StringVar()
		v = self.liste.get()
		self.fig.clear()	#efface la precedente figure
		self.canvas.get_tk_widget().destroy()
		self.canvas = FigureCanvasTkAgg(self.fig,master=self.fenetre_graphe)
		self.canvas.get_tk_widget().pack()
		self.a = graphique("Les sciences cognitives vous interessent ?")
		tmp = self.a.affichage_diagramme(self.fig,self.ani)
		self.canvas.show()
		

	def arret(self):		#arrete la recolte de donnees lors du clic sur arret
		self.a.stop_anim()
		n = self.sms.get_nomfich()
		self.sms.stopthread()
		#self.liste_graph.insert(END,n)




if __name__ == '__main__':
	app = Statistiques(None)
	app.title('Statistiques')
	app.mainloop()
