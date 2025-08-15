import os
import sys

# Example 13 - 1
def E01Example_13_01(args):
	oListTokens = input("수식 입력 : ").split()
	
	nValA = int(oListTokens[0])
	nValB = int(oListTokens[2])
	
	# 곱셈 일 경우
	if oListTokens[1] == "+":
		print("{0} + {1} = {2}".format(nValA, nValB, E01GetVal_Sum_13_01(nValA, nValB)))
	
	# 뺄셈 일 경우
	elif oListTokens[1] == "-":
		print("{0} - {1} = {2}".format(nValA, nValB, E01GetVal_Sub_13_01(nValA, nValB)))
	
	# 뺄셈 일 경우
	elif oListTokens[1] == "*":
		print("{0} * {1} = {2}".format(nValA, nValB, E01GetVal_Multiply_13_01(nValA, nValB)))
	
	# 뺄셈 일 경우
	elif oListTokens[1] == "/":
		print("{0} / {1} = {2}".format(nValA, nValB, E01GetVal_Divide_13_01(nValA, nValB)))


# 덧셈 결과를 반환한다
def E01GetVal_Sum_13_01(a_nValA: int, a_nValB: int):
	"""
	return 키워드는 메서드를 종료하는 역할을 수행한다. (즉, 메서드 몸체를 실행하는 중에 return 키워드를 만나면 즉시 메서드를 종료 후
	해당 메서드를 호출한 곳으로 프로그램의 흐름이 이동한다는 것을 알 수 있다.)

	또한, 해당 키워드와 더불어 특정 값을 명시했을 경우 해당 값을 메서드를 호출한 곳으로 반환시키는 역할도 수행한다. (즉, 특정 메서드 내부에
	return 키워드와 반환 값을 명시 할 경우 해당 메서드는 반환 값이 존재하는 메서드라는 것을 알 수 있다.)
	"""
	return a_nValA + a_nValB


# 뺄셈 결과를 반환한다
def E01GetVal_Sub_13_01(a_nValA: int, a_nValB: int):
	return a_nValA - a_nValB


# 곱셈 결과를 반환한다
def E01GetVal_Multiply_13_01(a_nValA: int, a_nValB: int):
	return a_nValA * a_nValB


# 나눗셈 결과를 반환한다
def E01GetVal_Divide_13_01(a_nValA: int, a_nValB: int):
	return a_nValA / a_nValB
