import serial,time,string,threading
from commande import *

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

	def run(self):
		self.ser.open()
		numero = ""
		vote = ""
		print( "connected to: " + self.ser.portstr )
		
		#ser.write( "AT"+chr(13) )
		
		#line = ser.readline()
		#print( line )
		#line = ser.readline()
		#print( line )
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

	def authentication():
		self.ser.open()
		numero = ""
		vote = ""
		auth = []
		print( "connected to: " + self.ser.portstr )
		
		#ser.write( "AT"+chr(13) )
		
		#line = ser.readline()
		#print( line )
		#line = ser.readline()
		#print( line )
		lines = self.ser.readlines()
		lines =""
		if self.ser.isOpen():
			while test == False and tmp == False:
				lines = self.ser.readlines()
				if lines:
					print(lines)	
					numero = lines[1]
					vote = lines[2]
					numero = numero[7:19]
					auth.append(numero)
					auth.append(vote)
					test = authentifie(numero)
					if test == True:
						print("okaye")
					tmp = authentification(auth)
					if tmp == True:
						print("authentifie")
					print(numero)
					print(vote)
					auth =  []
					#fichier.write(numero)
					#fichier.write(" ")
					#fichier.write(vote)
					
		self.ser.close();

		return True

