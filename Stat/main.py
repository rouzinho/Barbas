#!/usr/bin/env python
		
from ConnexionSms import *
from graphique import *
import threading

def main():
	
	sur = ConnexionSms()
	sur.start()
	t = "Le projet est il innovant ?"
	affichage_diagramme(t)


	return 0

if __name__ == '__main__':
	main()

