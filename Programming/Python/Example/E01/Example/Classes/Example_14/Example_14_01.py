import os
import sys


# Example 14 - 1
def Example_14_01(args):
	nVal = int(input("정수 입력 : "))
	print("결과 : {0}".format(E14_01GetFactorial(nVal)))


# 팩토리얼을 반환한다
def E14_01GetFactorial(a_nVal: int):
	# 재귀가 불가능 할 경우
	if a_nVal <= 1:
		return 1
	
	"""
	메서드 내부에서 자기 자신을 다시 호출하는 것이 가능하며 이를 재귀호출이라고 한다.
	
	단, 재귀 호출은 자기 자신을 반복적으로 호출하기 때문에 반복문과 마찬가지로 재구 호출을 끝내기 위한 명령문을 반드시 작성해야한다. (즉, 재귀
	호출을 끝내기 위한 구문이 없을 경우 프로그램이 오작동한다는 것을 알 수 있다.)
	"""
	return a_nVal * E14_01GetFactorial(a_nVal - 1)
