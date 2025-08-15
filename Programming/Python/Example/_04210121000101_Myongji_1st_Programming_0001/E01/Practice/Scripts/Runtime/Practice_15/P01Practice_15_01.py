import os
import sys


# Practice 15 - 1
def P01Practice_15_01(args):
	nNumValues = int(input("개수 입력 : "))
	oListValues = [sys.maxsize] * nNumValues
	
	nOddIdx = 0
	nEvenIdx = nNumValues - 1
	
	for i in range(0, nNumValues):
		nVal = int(input("{0} 번째 숫자 입력 : ".format(i + 1)))
		
		# 홀수 일 경우
		if nVal % 2 >= 1:
			oListValues[nOddIdx] = nVal
			nOddIdx += 1
		
		else:
			oListValues[nEvenIdx] = nVal
			nEvenIdx -= 1
	
	print("\n=====> 결과 <=====")
	print("{0}".format(oListValues))
