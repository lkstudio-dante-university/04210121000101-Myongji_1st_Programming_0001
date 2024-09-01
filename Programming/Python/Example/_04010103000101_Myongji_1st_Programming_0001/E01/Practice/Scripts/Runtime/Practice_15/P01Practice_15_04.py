import os
import sys


# Practice 15 - 4
def P01Practice_15_04(args):
	oListValues = [
		1, 2, 3, 4, 5, 6, 7, 8, 9
	]
	
	while True:
		print("{0}".format(oListValues))
		nDirection = int(input("방향 입력 (1: 왼쪽, 2: 오른쪽, 0: 종료) : "))
		
		# 종료를 입력 했을 경우
		if nDirection <= 0:
			break
		
		print()
		P01MoveValues_15_04(oListValues, nDirection)
	
	print("\n프로그램을 종료합니다.")


# 값을 이동 시킨다
def P01MoveValues_15_04(a_oListValues: list, a_nDirection: int):
	nIdx = 0 if a_nDirection <= 1 else len(a_oListValues) - 1
	nVal = a_oListValues[nIdx]
	
	del a_oListValues[nIdx]
	
	# 왼쪽 방향 일 경우
	if a_nDirection <= 1:
		a_oListValues.append(nVal)
		
	else:
		a_oListValues.insert(0, nVal)
	