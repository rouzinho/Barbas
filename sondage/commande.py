#coding: utf-8
import datetime
import time

class commande():
	def __init__(self):
		self.adm = False
		self.success = False
		self.nom_fichier = ""

	def authentifie(num):		#regarde si l'utilisateur est déja authentifié dans le fichier auth.txt.
		try :
			with open('auth.txt', 'r') as openedFile :
				for line in openedFile :
					if num in line:
						self.adm = True
		except IOError :
			print("IOError!")

		return self.adm

	def authentification(login):	#authentifie l'utilisateut
		f = open('auth.txt','a')
		self.success = False
		print("--------------")
		print(login)
		if login[1] == "1234\r\n":	#attention mot de passe 1234. Il faut faire attention au \r\n, sinon le mot de passe ne sera pas bon.
			f.write(login[0])
			self.success = True
		print(self.success)
		print("--------------")
		return self.success


