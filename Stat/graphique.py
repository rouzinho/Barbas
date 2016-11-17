import time
from compte import *
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation


def affichage_diagramme(titre):

	OX = []
	OY = []
	nb_occ = tab_nb_occ()
	nom_occ = tab_nom_occ()
	fig = plt.figure()
	plt.title(titre)
	width = .35
	max_ = max_occ()
	colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','blue']
	ind = np.arange(nb_total_occ())
	plt.bar(ind, nb_occ,width,color = colors,bottom=max_)

	plt.xticks(ind+width/2., nom_occ)

	ani = animation.FuncAnimation(fig, update_diagramme, interval=5)
	plt.show()
	#return fig
	
def update_diagramme(*args):
	colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','blue']
	nb_occ = tab_nb_occ()
	nom_occ = tab_nom_occ()
	ind = np.arange(nb_total_occ())
	plt.bar(ind, nb_occ,0.35,color = colors,bottom=0)
	plt.xticks(ind+0.35/2., nom_occ)


def affichage_camembert(titre):
	nb_occ = tab_nb_occ()
	nom_occ = tab_nom_occ()
	fig = plt.figure()
	colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','blue']
	plt.pie(nb_occ, labels=nom_occ, colors=colors,autopct='%1.1f%%', shadow=True, startangle=90)
	plt.axis('equal')
	#plt.show()

	return fig

#affichage_diagramme('test')
