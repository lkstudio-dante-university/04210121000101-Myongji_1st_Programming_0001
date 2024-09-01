import os
import sys

# Example 12 - 3
def E01Example_12_03(args):
	nNumValues = int(input("개수 입력 : "))
	oListValues = []
	
	for i in range(0, nNumValues):
		nVal = int(input("{0} 번째 숫자 입력 : ".format(i + 1)))
		oListValues.append(nVal)
	
	# 입력 된 숫자가 없을 경우
	if len(oListValues) <= 0:
		print("입력 된 숫자가 없습니다.")
	
	else:
		nVal_Sum = 0
		
		for nVal in oListValues:
			nVal_Sum += nVal
		
		"""
		Python 은 / (나눗셈) 연산자의 우항에 있는 피연산자가 0 일 경우 예외가 발생한다. (즉, 잘못된 연산으로 인해 프로그램이
		오작동 한다는 것을 의미한다.)
		
		따라서, 우항의 값이 0 이 될 가능성이 조금이라도 있다면 반드시 해당 연산자를 사용하기 전에 if ~ else 조건문 등으 활용해서
		예외처리를 해줘야한다.
		"""
		print("\n합계 : {0}".format(nVal_Sum))
		print("평균 : {0}".format(nVal_Sum / len(oListValues)))
