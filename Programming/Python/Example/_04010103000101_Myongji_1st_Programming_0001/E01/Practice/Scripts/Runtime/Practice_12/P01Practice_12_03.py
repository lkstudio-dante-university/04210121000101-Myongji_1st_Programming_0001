import os
import sys


# Practice 12 - 3
def P01Practice_12_03(args):
	oListValues = []
	oListTokens = input("정수 (3 개) 입력 : ").split()
	
	for oToken in oListTokens:
		oListValues.append(int(oToken))
		print("{0:^4}".format(oToken), end="")
		
	print()
	
	for i in range(0, max(oListValues)):
		for nVal in oListValues:
			print("{0:^4}".format("*" if i < nVal else " "), end="")
			
		print()
