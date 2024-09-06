import os
import sys


# Practice 15 - 2
def P01Practice_15_02(args):
	nNumValues = int(input("개수 입력 : "))
	
	for i in range(0, nNumValues):
		nVal = P01GetFibonacci_15_02(i + 1)
		print("{0}, ".format(nVal), end="")
	
	print("\n")


# 피보나치 수열을 출력한다
def P01GetFibonacci_15_02(a_nVal):
	# 재귀가 불가능 할 경우
	if a_nVal <= 1:
		return 0 if a_nVal <= 0 else 1
	
	return P01GetFibonacci_15_02(a_nVal - 1) + P01GetFibonacci_15_02(a_nVal - 2)
