import os
import sys


# Practice 12 - 4
def Practice_12_04(args):
	nNumLines = int(input("라인 수 입력 : "))
	
	for i in range(0, nNumLines):
		for j in range(0, nNumLines):
			print("{0}".format("*" if j <= i else " "), end="")
		
		print()
	
	print()
	
	for i in range(nNumLines - 1, -1, -1):
		for j in range(0, nNumLines):
			print("{0}".format("*" if j <= i else " "), end="")
		
		print()
	
	print()
	
	for i in range(0, nNumLines):
		for j in range(nNumLines - 1, -1, -1):
			print("{0}".format("*" if j <= i else " "), end="")
		
		print()
	
	print()
	
	for i in range(nNumLines - 1, -1, -1):
		for j in range(nNumLines - 1, -1, -1):
			print("{0}".format("*" if j <= i else " "), end="")
		
		print()
	
	print()
	
	for i in range(0, nNumLines):
		nNumCols = (nNumLines * 2) - 1
		nCenter = nNumCols // 2
		
		for j in range(0, nNumCols):
			print("{0}".format("*" if j >= nCenter - i and j <= nCenter + i else " "), end="")
		
		print()
	
	print()
	
	for i in range(nNumLines - 1, -1, -1):
		nNumCols = (nNumLines * 2) - 1
		nCenter = nNumCols // 2
		
		for j in range(0, nNumCols):
			print("{0}".format("*" if j >= nCenter - i and j <= nCenter + i else " "), end="")
		
		print()
