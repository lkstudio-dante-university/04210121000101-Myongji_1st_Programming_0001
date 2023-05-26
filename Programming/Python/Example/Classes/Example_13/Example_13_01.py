import os
import sys


# Example 13 - 1
def Example_13_01(args):
	oTokenList = input("수식 입력 : ").split()
	
	nVal01 = int(oTokenList[0])
	nVal02 = int(oTokenList[2])
	
	# 곱셈 일 경우
	if oTokenList[1] == "+":
		print("{0} + {1} = {2}".format(nVal01, nVal02, E13_01GetSumVal(nVal01, nVal02)))
	
	# 뺄셈 일 경우
	elif oTokenList[1] == "-":
		print("{0} - {1} = {2}".format(nVal01, nVal02, E13_01GetSubVal(nVal01, nVal02)))
	
	# 뺄셈 일 경우
	elif oTokenList[1] == "*":
		print("{0} * {1} = {2}".format(nVal01, nVal02, E13_01GetMultiplyVal(nVal01, nVal02)))
	
	# 뺄셈 일 경우
	elif oTokenList[1] == "/":
		print("{0} / {1} = {2}".format(nVal01, nVal02, E13_01GetDivideVal(nVal01, nVal02)))


# 덧셈 결과를 반환한다
def E13_01GetSumVal(a_nVal01: int, a_nVal02: int):
	"""
	return 키워드는 메서드를 종료하는 역할을 수행한다. (즉, 메서드 몸체를 실행하는 중에 return 키워드를 만나면 즉시 메서드를 종료 후
	해당 메서드를 호출한 곳으로 프로그램의 흐름이 이동한다는 것을 알 수 있다.)

	또한, 해당 키워드와 더불어 특정 값을 명시했을 경우 해당 값을 메서드를 호출한 곳으로 반환시키는 역할도 수행한다. (즉, 특정 메서드 내부에
	return 키워드와 반환 값을 명시 할 경우 해당 메서드는 반환 값이 존재하는 메서드라는 것을 알 수 있다.)
	"""
	return a_nVal01 + a_nVal02


# 뺄셈 결과를 반환한다
def E13_01GetSubVal(a_nVal01: int, a_nVal02: int):
	return a_nVal01 - a_nVal02


# 곱셈 결과를 반환한다
def E13_01GetMultiplyVal(a_nVal01: int, a_nVal02: int):
	return a_nVal01 * a_nVal02


# 나눗셈 결과를 반환한다
def E13_01GetDivideVal(a_nVal01: int, a_nVal02: int):
	return a_nVal01 / a_nVal02
