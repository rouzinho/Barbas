import numpy as np

def serie_un():
	tab_serie = []
	try :
		with open('serie.txt', 'r') as openedFile :
			for line in openedFile :
				tab = line.split()
				tab_serie.append(tab[1])
	except IOError :
		print("IOError!")

	return tab_serie

def moyenne_serie(serie):
	total = 0
	j = 0
	for i in serie:
		total = total + i
		j = j + 1
	moyenne = total / j

	return moyenne

def mediane_serie(serie):
	med = np.median(serie)
	return med
