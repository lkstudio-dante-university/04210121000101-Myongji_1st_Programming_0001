import os
import sys


# Practice 15 - 1
def Practice_15_01(args):
	nNumVals = int(input("개수 입력 : "))
	oValList = [sys.maxsize] * nNumVals
	
	nOddIdx = 0
	nEvenIdx = nNumVals - 1
	
	for i in range(0, nNumVals):
		nVal = int(input("{0} 번째 숫자 입력 : ".format(i + 1)))
		
		# 홀수 일 경우
		if nVal % 2 >= 1:
			oValList[nOddIdx] = nVal
			nOddIdx += 1
		
		else:
			oValList[nEvenIdx] = nVal
			nEvenIdx -= 1
	
	print("\n=====> 결과 <=====")
	print("{0}".format(oValList))
