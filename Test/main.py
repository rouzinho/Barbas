#!/usr/bin/env python
		
from EcouteSMS import *
import threading

def main():
	
	sur = EcouteSMS()
	sur.start()

	return 0

if __name__ == '__main__':
	main()

