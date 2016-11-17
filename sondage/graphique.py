#coding: utf-8
import time
from compte import *
import numpy as np
from matplotlib import pyplot as plt 	#pour dessiner une Figure
import matplotlib.animation as animation #pour animer la Figure


class graphique(object):
	
	def __init__(self,titre):
		def_occurences()
		self.nb_occ = tab_nb_occ("data.txt")	#on recupere le tableau du nombre d'occurences
		self.nom_occ = tab_nom_occ("data.txt")	#on recupere le tableau des noms d'occurences
		self.nb_tot = nb_total_occ("data.txt")	#on recupere le nolbre total d'occurences
		plt.title(titre)
		self.width = .35
		self.max_ = max_occ("data.txt")
		self.colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','blue']
		self.rects = []
		self.patch = []
		self.ani = 0
		self.pause = False
		
	
	def update_diagramme(self,*args):
		if self.pause == False:
			def_occurences()
			i = 0
			t = tab_nb_occ("data.txt")
			m = max(t)
			for rec in self.rects:		#parcours la liste des rectangle du diagramme et les ajuste en fonction
				rec.set_height(t[i])	#des nouvelles valeurs du sondage
				i = i+1
			plt.ylim(ymax=m)
			#print("----------")

	def stop_anim(self):
		self.pause = True

	def update_camembert(self,*args):	#bug encore sur l'affichage des pourcentages.
		def_occurences()
		theta_base = 90.0
		i = 0
		occ = []
		tot = 0
		j = 0
		self.nb_occ = tab_nb_occ("data.txt")
		#print(self.nb_occ)
		for x in self.nb_occ:
			tot = tot + x
		for j in self.nb_occ:
			tmp = (j/tot)*100
			angle = (360 * tmp)/100
			occ.append(angle)
		#print(occ)
		for p in self.patch[0]:		#parcours la liste des "portions" de camembert et les réajuste selon l'angle.
			#print("Theta1 :")		#fonctionne bien, mais en plus de redessiner les portions, il faudrait aussi actualiser
			#print(p.theta1)		#l'affichage des pourcentages.
			#print("Theta2: ")
			#print(p.theta2)
			#print(p.label)
			print("-----------------")
			if i == 0:
				teta1 = theta_base
				p.set_theta1(teta1)
				teta2 = theta_base + occ[i]
				p.set_theta2(teta2)
			else:
				teta1 = teta2
				p.set_theta1(teta1)
				teta2 = teta1 + occ[i]
				p.set_theta2(teta2)
			i = i + 1
		

	def auto_pct(self,*args):	#tentative rate d'actualiser les pourcentages affichees.
		l = 0
		pourcentage = []
		tot = 0
		for x in self.nb_occ:
			tot = tot + x
		for j in self.nb_occ:
			tmp = (j/tot)*100
			pourcentage.append(tmp)
		print(pourcentage)
		"""for k in self.patch[2]:
			c = round(pourcentage[l],1)
			k.set_text(c)
			l = l + 1"""

	def my_autopct(self,pct):
		total=sum(self.nb_occ)
		val=int(pct*total/100.0)
    	
		return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)


	def affichage_diagramme(self,figu,anim):	#fonction qui dessine le diagramme. On a besoin de ces paramètres por l'affichage dynamique
		couple = []
		def_occurences()
		ind = np.arange(self.nb_tot)
		self.rects = plt.bar(ind, self.nb_occ,self.width,color = self.colors,bottom=self.max_) #voir l'API bien fournie
		plt.xticks(ind+self.width/2., self.nom_occ)
		anim = animation.FuncAnimation(figu, self.update_diagramme, interval=1000)   #fonction qui "anime" l'affichage en appelant la fonction update_diagramme()
		couple.append(figu)
		couple.append(anim)
		return couple
	


	def affichage_camembert(self):		#analogue à affichage_diagramme()
		
		self.patch = plt.pie(self.nb_occ, labels=self.nom_occ, colors=self.colors,autopct=self.my_autopct, shadow=True, startangle=90)
		plt.axis('equal')
		self.ani = animation.FuncAnimation(self.fig,self.update_camembert, interval=5000)
		plt.show()



