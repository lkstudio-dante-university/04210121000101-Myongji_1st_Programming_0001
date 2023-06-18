import os
import sys


# Practice 15 - 4
def Practice_15_04(args):
	oValList = [
		1, 2, 3, 4, 5, 6, 7, 8, 9
	]
	
	while True:
		print("{0}".format(oValList))
		nDirection = int(input("방향 입력 (1: 왼쪽, 2: 오른쪽, 0: 종료) : "))
		
		# 종료를 입력 했을 경우
		if nDirection <= 0:
			break
		
		print()
		P15_04MoveVals(oValList, nDirection)
	
	print("\n프로그램을 종료합니다.")


# 값을 이동 시킨다
def P15_04MoveVals(a_oValList: list, a_nDirection: int):
	nIdx = 0 if a_nDirection <= 1 else len(a_oValList) - 1
	nVal = a_oValList[nIdx]
	
	del a_oValList[nIdx]
	
	# 왼쪽 방향 일 경우
	if a_nDirection <= 1:
		a_oValList.append(nVal)
		
	else:
		a_oValList.insert(0, nVal)
	