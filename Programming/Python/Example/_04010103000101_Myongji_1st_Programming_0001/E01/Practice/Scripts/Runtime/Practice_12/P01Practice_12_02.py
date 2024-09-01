import os
import sys
import random


# Practice 12 - 2
def P01Practice_12_02(args):
	oListValues = []
	
	for i in range(0, 10):
		oListValues.append(random.randint(1, 99))
	
	print("=====> 리스트 요소 <=====")
	print("{0}".format(oListValues))
	
	nMinVal = oListValues[0]
	nMaxVal = oListValues[1]
	
	for nVal in oListValues:
		nMinVal = nMinVal if nMinVal < nVal else nVal
		nMaxVal = nMaxVal if nMaxVal > nVal else nVal
	
	print("\n최소 값 : {0}".format(nMinVal))
	print("최대 값 : {0}".format(nMaxVal))
