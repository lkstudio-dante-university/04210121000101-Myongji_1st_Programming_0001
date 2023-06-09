import os
import sys


# Example 13 - 2
def Example_13_02(args):
	nVal = int(input("정수 입력 : "))
	
	print("\n=====> 구구단 출력 <=====")
	E13_02PrintVals(nVal)


# 구구단을 출력한다
def E13_02PrintVals(a_nVal: int):
	for i in range(1, 10):
		print("{0} * {1} = {2}".format(a_nVal, i, a_nVal * i))
