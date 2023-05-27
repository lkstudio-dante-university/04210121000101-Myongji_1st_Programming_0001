import os
import sys
import random


# Practice 12 - 2
def Practice_12_02(args):
	oValList = []
	
	for i in range(0, 10):
		oValList.append(random.randint(1, 99))
	
	print("=====> 리스트 요소 <=====")
	print("{0}".format(oValList))
	
	nMinVal = oValList[0]
	nMaxVal = oValList[1]
	
	for nVal in oValList:
		nMinVal = nMinVal if nMinVal < nVal else nVal
		nMaxVal = nMaxVal if nMaxVal > nVal else nVal
	
	print("\n최소 값 : {0}".format(nMinVal))
	print("최대 값 : {0}".format(nMaxVal))
