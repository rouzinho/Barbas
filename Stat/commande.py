def authentifie(num):
	adm = False
	try :
		with open('auth.txt', 'r') as openedFile :
			for line in openedFile :
				if num in line:
					adm = True
	except IOError :
		print("IOError!")

	return adm

def authentification(login):
	f = open('auth.txt','a')
	success = False
	print("--------------")
	print(login)
	if login[1] == "1234\r\n":
		f.write(login[0])
		success = True
	print(success)
	print("--------------")
	return success

