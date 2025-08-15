import os
import sys


# Practice 15 - 5
def P01Practice_15_05(args):
	oListValues = [
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]
	]
	
	while True:
		P01PrintValues_15_05(oListValues)
		nDirection = int(input("\n방향 입력 (1: 왼쪽, 2: 오른쪽, 0: 종료) : "))
		
		# 종료를 입력 했을 경우
		if nDirection <= 0:
			break
		
		print()
		P01MoveValuesInRow_15_05(oListValues, nDirection)
	
	print("\n프로그램을 종료합니다.")


# 값을 이동 시킨다
def P01MoveValuesInRow_15_05(a_oListValues: list, a_nDirection: int):
	for oListValues in a_oListValues:
		P01MoveValues_15_05(oListValues, a_nDirection)


# 값을 이동 시킨다
def P01MoveValues_15_05(a_oListValues: list, a_nDirection: int):
	nIdx = 0 if a_nDirection <= 1 else len(a_oListValues) - 1
	nVal = a_oListValues[nIdx]
	
	del a_oListValues[nIdx]
	
	# 왼쪽 방향 일 경우
	if a_nDirection <= 1:
		a_oListValues.append(nVal)
	
	else:
		a_oListValues.insert(0, nVal)


# 값을 출력한다
def P01PrintValues_15_05(a_oListValues: list):
	for oListValues in a_oListValues:
		print("{0}".format(oListValues))
