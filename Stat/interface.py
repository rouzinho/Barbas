from tkinter import *
from tkinter.ttk import *
from time import sleep

#from ConnexionSms import *

def auth():
	# On cree une fenetre, racine de notre interface
	#conn = ConnexionSms()
	fenetre = Tk()
	fenetre.title('Authentification')
	fenetre['bg'] = 'red'
	fenetre.geometry('300x100+400+400')
	var = "Authentification..."
	champ_label = Label(fenetre, text=var)
	champ_label.pack(padx = 0,pady = 30)
	fenetre.update_idletasks()
	#conn.authentication()
	fenetre['bg'] = 'green'
	var = "Okaye"
	champ_label.update_idletasks()
	# On demarre la boucle Tkinter qui s'interompt quand on ferme la fenetre
	fenetre.mainloop()

def choix_modele():
	fenetre_choix = Tk()

	photo=PhotoImage(file="Logo-blanc.png")
	
	fenetre_choix.title('Choix du modèle à utiliser')
	fenetre_choix.geometry('500x150+400+200')
	bouton_sondage = Button(fenetre_choix,text = 'Sondages')
	bouton_sondage.config(height = 5,width = 20)
	bouton_sondage.pack(side = LEFT,padx = 30,pady = 10)
	bouton_stat = Button(fenetre_choix,text = 'Statistiques')
	bouton_stat.config(height = 5,width = 20)
	bouton_stat.pack(side = RIGHT,padx = 30,pady = 10)

	fenetre_choix.mainloop()


def sondage():
	main_frame = Tk()
	fenetre_haut = Frame(main_frame,width=700,height=150)
	fenetre_bas = Frame(main_frame,width=700,height=250)
	fen_haut = Frame(fenetre_bas,width=700,height=100)
	fen_bas = Frame(fenetre_bas,width=700,height=100)


	main_frame.geometry('700x300+300+100')		#PANNEAU DU HAUT
	main_frame.title('Statistiques')
	label_titre = Label(fenetre_haut,text="Envoyez le titre du sondage :",width=120)
	label_titre.config(font=('Inconsolata',20,'bold'))
	photo = PhotoImage(file='refresh.png')
	bouton_refresh = Button(fenetre_haut,image=photo)
	titre = Text(fenetre_haut,width=100,height=1)
	titre.config(font=('Inconsolata',14,'bold'))
	titre.insert(END,"")
	titre.configure(state=DISABLED)
	label_titre.pack(side=TOP,padx=20,pady=10)
	titre.pack()
	bouton_refresh.pack(side=TOP)

	label_mod = Label(fen_haut,text="Envoyez les modalités :",width=120)	#PANNEAU DU BAS
	label_mod.config(font=('Inconsolata',20,'bold'))		
	bouton_ref_mod = Button(fen_bas,image=photo)
	mod0 = Text(fen_bas,width=10,height=1)
	mod0.config(font=('Inconsolata',16,'bold'))
	mod0.configure(state=DISABLED)
	mod1 = Text(fen_bas,width=10,height=1)
	mod1.config(font=('Inconsolata',16,'bold'))
	mod1.configure(state=DISABLED)
	mod2 = Text(fen_bas,width=10,height=1)
	mod2.config(font=('Inconsolata',16,'bold'))
	mod2.configure(state=DISABLED)
	mod3 = Text(fen_bas,width=10,height=1)
	mod3.config(font=('Inconsolata',16,'bold'))
	mod3.configure(state=DISABLED)
	mod4 = Text(fen_bas,width=10,height=1)
	mod4.config(font=('Inconsolata',16,'bold'))
	mod4.configure(state=DISABLED)
	ok = Button(fen_bas,text="OK !")
	label_mod.pack(side=LEFT)
	bouton_ref_mod.pack(side=RIGHT)
	mod0.pack(side=LEFT)
	mod1.pack(side=LEFT)
	mod2.pack(side=LEFT)
	mod3.pack(side=LEFT)
	mod4.pack(side=LEFT)
	ok.pack(side=RIGHT)
	fen_haut.pack(side=TOP,padx=10)
	fen_haut.pack_propagate(False)
	fen_bas.pack(side=BOTTOM,padx=10)
	fen_bas.pack_propagate(False)

	fenetre_haut.pack(side=TOP)
	fenetre_haut.pack_propagate(False)
	fenetre_bas.pack()
	fenetre_bas.pack_propagate(False)

	main_frame.mainloop()


def statistiques():
	main_fenetre = Tk()
	fenetre_graphe = Frame(main_fenetre,borderwidth=2,relief=GROOVE)	#Frames generales
	fenetre_gauche = Frame(main_fenetre,width=300,height=700,borderwidth=2,relief=GROOVE)
	fenetre_haut = Frame(fenetre_gauche,borderwidth=2)
	fenetre_centre = Frame(fenetre_gauche,borderwidth=2,relief=GROOVE)
	fenetre_bas = Frame(fenetre_gauche,borderwidth=2,relief=GROOVE)

	valeur = StringVar()	#fenetre du haut
	list_ch = []	
	new_val = Entry(fenetre_haut,textvariable=valeur,width=15)
	new_val.config(font=('Inconsolata',16,'bold'))
	nouveau = Button(fenetre_haut,text='NOUVEAU')	#faire le append() pour MAJ du list_ch
	lancer = Button(fenetre_haut,text='LANCER')
	arreter = Button(fenetre_haut,text='ARRETER')
	arreter.config(state=DISABLED)
	val_list = StringVar()
	liste = Combobox(fenetre_haut,textvariable=val_list,values=list_ch,state='readonly')
	new_val.grid(row=1,column=1)
	nouveau.grid(row=1,column=2)
	liste.grid(row=2,column=1)
	lancer.grid(row=2,column=2)
	arreter.grid(row=4,column=3)

	numero = Label(fenetre_centre,text="06 03 81 78 36",width=120)	#fenetre du milieu
	numero.config(font=('Inconsolata',35,'bold'))
	numero.pack()

	liste_graph = Listbox(fenetre_bas,width=20,height=10)	#fenetre du bas
	afficher = Button(fenetre_bas,text='AFFICHER')
	ou = Label(fenetre_bas,text='ou')
	affi = Label(fenetre_bas,text='Afficher')
	fct = Label(fenetre_bas,text=' en fonction de ')
	liste_graph.grid(row=1,column=1)
	afficher.grid(row=1,column=3)

	photo = PhotoImage(file="test.png")	#ecran de droite
	zone_dessin = Canvas(main_fenetre, width=600, height=600) #Définit les dimensions du canevas
	zone_dessin.pack(side=RIGHT) #Affiche le canevas
	
	
	main_fenetre.geometry('1000x700+150+50')
	fenetre_haut.pack(side=TOP,padx=7,pady=50)
	fenetre_centre.pack(padx=7,pady=50)
	fenetre_bas.pack(side=BOTTOM,padx=10,pady=50)
	
	fenetre_gauche.pack(side=LEFT,padx=8,pady=20)

	main_fenetre.mainloop()

sondage()
