#coding: utf-8
import time,string,threading,serial
from commande import *
from simulation import *
import sys

class ConnexionSms(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)	
		self.ser = serial.Serial( 
			port = '/dev/ttyAMA0', \
			baudrate = 115200, \
			parity=serial.PARITY_NONE, \
			stopbits=serial.STOPBITS_ONE, \
			bytesize = serial.EIGHTBITS, \
			timeout = 0.100 )
		self.arret = False
		self.nom_fichier = "sms.txt"

	"""def run(self):		#fonction de test affichant chaque sms reçus au fur et à mesure
		try:
			self.ser.open()
			numero = ""
			vote = ""
			print( "connected to: " + self.ser.portstr )
			lines = self.ser.readlines()
			lines =""
			if self.ser.isOpen():
				while True:
					fichier = open("sms.txt","a")
					lines = self.ser.readlines()
					if lines:
						print(lines)	
						numero = lines[1]
						vote = lines[2]
						numero = numero[7:19]
						print(numero)
						print(vote)
						fichier.write(numero)
						fichier.write(" ")
						fichier.write(vote)
			self.ser.close();
		except:
			print u"%s" % sys.exc_info()"""
	"""def run(self):    #fonction simulant la reception de SMS
		try:			#à remplacer avec le corps de lancement_sms
			numero = "+33600000000"
			vote = "non"
			i = 1
			while True:
				if self.arret == True:
					raise ValueError ("arret demande")
				print(self.nom_fichier)
				fichier = open("sms.txt","a")
				fichier.write(numero)
				fichier.write(" ")
				fichier.write(vote)
				fichier.write("\n")
				print(repr(i)+" vote envoye")
				i = i + 1
				fichier.close()
				time.sleep(5)
		except:
			print("sortie du thread")
			#print(u"%s" % sys.exc_info())"""

	def stopthread(self):
		self.arret = True

	def set_nomfich(self,nom):		#convertis le nom de la modalité choisie en format "nom-date-heure.txt"
		tps = time.strftime("%H:%M:%S")
		date = time.strftime("%d/%m/%Y")
		date = date.replace('/','|')
		self.nom_fichier = nom+"-"+date+"-"+tps+".txt"

	def get_nomfich(self):		#retourne le nom de fichier
		return self.nom_fichier

	

	def run(self):	#véritable fonction permettant de recevoir le sms, de le tronquer et de 
		self.ser.open()			#le stocker dans le fichier prévu par nom_fichier
		numero = ""
		vote = ""
		print( "connected to: " + self.ser.portstr )
		lines = self.ser.readlines()
		lines = ""
		try:
			if self.ser.isOpen():
				while True:
					if self.arret == True:
						raise ValueError ("arret demande")
					fichier = open("sms.txt","a")
					lines = self.ser.readlines()
					if lines:
						print(lines)	
						numero = lines[1]
						vote = lines[2]
						numero = numero[7:19]
						print(numero)
						print(vote)
						fichier.write(numero)
						fichier.write(" ")
						fichier.write(vote)
		except ValueError, e:
			print("sortie du thread")
			print(e)			 			
			self.ser.close();
