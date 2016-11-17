
#  
import serial,time,string,subprocess
	

def main():

	ser = serial.Serial( 
			port = '/dev/ttyAMA0', \
			baudrate = 115200, \
			parity=serial.PARITY_NONE, \
			stopbits=serial.STOPBITS_ONE, \
			bytesize = serial.EIGHTBITS, \
			timeout = 0.100 )

	ser.open()
	fichier = open("data.txt","a")
	numero = ""
	vote = ""
	print( "connected to: " + ser.portstr )
	
	ser.write( "AT"+chr(13) )
	
	line = ser.readline()
	print( line )
	line = ser.readline()
	print( line )
	lines = ser.readlines()
	lines =""
	if ser.isOpen():
		while True:
			lines = ser.readlines()
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
				subprocess.call(["espeak",vote,"-v","french","-s","100","-p","40"])
				#fichier.write("\n")
			
				
		ser.close();

	return 0

if __name__ == '__main__':
	main()
