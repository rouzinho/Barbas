import time

def sim():
	
	numero = "+33600000000"
	vote = "non"
	i = 1
	while True:
		fichier = open("sms.txt","a")
		fichier.write(numero)
		fichier.write(" ")
		fichier.write(vote)
		fichier.write("\n")
		print(repr(i)+" vote envoye")
		i = i + 1
		fichier.close()
		time.sleep(5)

