import os
import sys

# Example 11 - 2
def E01Example_11_02(args):
	oListTokens = input("수식 입력 : ").split()
	
	nValA = int(oListTokens[0])
	nValB = int(oListTokens[2])
	
	"""
	특정 조건을 만족 할 경우 실행 될 명령문은 반드시 if ~ else 조건문보다 한 수준 들여쓰기가 적용되어 있어야한다. (즉, 들여쓰기가 안되어있다면
	해당 명령문은 if ~ else 조건문과는 별개의 명령문이라는 것을 알 수 있다.)
	
	따라서, 조건문과 같이 하위 영역을 지니는 명령문은 : (클론) 기호와 들여쓰기를 통해 구분하는 것이 가능하다.
	"""
	# + 연산자 일 경우
	if oListTokens[1] == "+":
		print("{0} + {1} = {2}".format(nValA, nValB, nValA + nValB))
	
	# - 연산자 일 경우
	elif oListTokens[1] == "-":
		print("{0} - {1} = {2}".format(nValA, nValB, nValA - nValB))
	
	# * 연산자 일 경우
	elif oListTokens[1] == "*":
		print("{0} * {1} = {2}".format(nValA, nValB, nValA * nValB))
	
	# / 연산자 일 경우
	elif oListTokens[1] == "/" and nValB != 0:
		print("{0} / {1} = {2}".format(nValA, nValB, nValA / nValB))
	
	else:
		print("잘못된 수식을 입력했습니다.")
