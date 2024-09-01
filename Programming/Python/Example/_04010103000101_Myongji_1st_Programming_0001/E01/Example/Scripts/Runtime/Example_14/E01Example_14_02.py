import os
import sys


# Example 14 - 2
def E01Example_14_02(args):
	nVal = int(input("정수 입력 : "))
	E01PrintHanoi_14_02(nVal, 1, 3, 2)


# 하노이 탑 결과를 출력한다
def E01PrintHanoi_14_02(a_nVal: int, a_nSrc: int, a_nDest: int, a_nTemp: int):
	# 목적지로 이동이 가능 할 경우
	if a_nVal <= 1:
		print("{0} : {1} 번 -> {2} 번으로 이동".format(a_nVal, a_nSrc, a_nDest))
	
	else:
		E01PrintHanoi_14_02(a_nVal - 1, a_nSrc, a_nTemp, a_nDest)
		print("{0} : {1} 번 -> {2} 번으로 이동".format(a_nVal, a_nSrc, a_nDest))
		
		E01PrintHanoi_14_02(a_nVal - 1, a_nTemp, a_nDest, a_nSrc)
