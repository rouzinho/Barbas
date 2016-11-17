#!/usr/bin/env python
		
from ConnexionSms import *
from graphique import *
from matplotlib.figure import Figure
#from graphique import *


def main():
	
	sms = ConnexionSms()
	sms.start()


	return 0

if __name__ == '__main__':
	main()

