#!/usr/bin/env python
  
import serial,time,string,threading
	
class EcouteSMS(threading.Thread):
	
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
		lines = self.ser.readlines()
		lines =""
		if self.ser.isOpen():
			while True:
				fichier = open("sms.txt","a")
				f = open("tag.txt","a")
				lines = self.ser.readlines()
				print(lines)	
				numero = lines[1]
				vote = lines[2]
				#
				tag = vote.split()
				for i in tag :
					#fichier = open("sms.txt","a")
					numero = numero[7:19]
					fichier.write(numero)
					fichier.write(" ")
					fichier.write(i)
					fichier.write("\n")
					#fichier.close
				else:
					#f = open("tag.txt","a")
					f.write(i)
					f.write("\n")
					#f.close
				#
				#numero = numero[7:19]
				#fichier.write(numero)
				#fichier.write(" ")
				#fichier.write(vote)	
				fichier.close
				f.close
				
		self.ser.close();
