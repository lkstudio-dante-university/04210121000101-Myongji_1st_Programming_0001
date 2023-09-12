import os
import sys


# Practice 12 - 3
def Practice_12_03(args):
	oValList = []
	oTokenList = input("정수 (3 개) 입력 : ").split()
	
	for oToken in oTokenList:
		oValList.append(int(oToken))
		print("{0:^4}".format(oToken), end="")
		
	print()
	
	for i in range(0, max(oValList)):
		for nVal in oValList:
			print("{0:^4}".format("*" if i < nVal else " "), end="")
			
		print()
