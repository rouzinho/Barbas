def def_occurences() :	#compte les nombre d'occurences et les ecrit dans data.txt
	f = open('sms.txt', 'r')
	g = open('data.txt','w')
	t = f.readline()
	i = 1
	j = 0
	cpt = 0
	dico = []
	df = []
	while t != "" :			#Boucle qui lit chaque lignes
		mot = t.split()
		while i < len(mot) :	#Boucle qui lit les reponses dans chaque lignes
			dico.append(mot[i]) 
			i = i+1
		i = 1
		t = f.readline()
	while j < len(dico) :
		k = 0
		mot_tmp = dico[j]
		while k < len(dico) :
			if mot_tmp == dico[k] and mot_tmp not in df:
				cpt = cpt + 1
			k = k + 1
		if mot_tmp not in df:
			df.append(mot_tmp)
			g.write(mot_tmp)
			g.write(" ")
			g.write(str(cpt))
			g.write("\n")
		cpt = 0
		j = j + 1
	f.close()
	g.close()

def tab_nb_occ():
	nb_occ = []
	try :
		with open('data.txt', 'r') as openedFile :
			for line in openedFile :
				tab = line.split()
				nb_occ.append(int(tab[1]))
	except IOError :
		print("IOError!")

	return nb_occ

def nb_total_occ():
	f = open("data.txt","r")
	t = f.readlines()
	l = len(t)

	return l

def tab_nom_occ():	#retourne le tableau des noms d'occurences
	nom_occ = []
	try :
		with open('data.txt', 'r') as openedFile :
			for line in openedFile :
				tab = line.split()
				nom_occ.append(tab[0])
	except IOError :
		print("IOError!")

	return nom_occ

def max_occ():	#retourne le nombre total des choix de vote
	max_ = 0
	try :
		with open('data.txt', 'r') as openedFile :
			for line in openedFile :
				tab = line.split()
				if max_ >= int(tab[1]) :
					max_ = int(tab[1])

	except IOError :
		print("IOError!")

	return max_

def choix_occ(choix):	#retourne la liste des votes selon les choix imposes
	liste_choix = []
	try :
		with open('data.txt', 'r') as openedFile :
			for line in openedFile :
				for j in choix:
					if j in line:
						ligne = line.split()
						liste_choix.append(ligne[0])
						liste_choix.append(ligne[1])
	except IOError :
		print("IOError!")

	return liste_choix

def modele(mod):		#Retourne vrai si la modalite etait dans la liste
	test = False
	try :
		with open('modele.txt', 'r') as openedFile :
			for line in openedFile :
				if mod in line:
					test = True
		if test == False:
			fich = open('modele.txt','a')
			fich.write(mod)
			fich.write("\n")
			fich.close()
	except IOError :
		print("IOError!")

	return test

def get_modele():
	dico = []
	try :
		with open('modele.txt','r') as openedFile:
			for line in openedFile:
				dico.append(line)
	except IOError:
		print("IOError!")

	return dico


