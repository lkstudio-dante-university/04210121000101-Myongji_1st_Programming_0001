import os
import sys


# Practice 15 - 2
def Practice_15_02(args):
	nNumVals = int(input("개수 입력 : "))
	
	for i in range(0, nNumVals):
		nVal = P15_02GetFibonacci(i + 1)
		print("{0}, ".format(nVal), end="")
	
	print("\n")


# 피보나치 수열을 출력한다
def P15_02GetFibonacci(a_nVal):
	# 재귀가 불가능 할 경우
	if a_nVal <= 1:
		return 0 if a_nVal <= 0 else 1
	
	return P15_02GetFibonacci(a_nVal - 1) + P15_02GetFibonacci(a_nVal - 2)
