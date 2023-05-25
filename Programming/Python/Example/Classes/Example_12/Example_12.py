import os
import sys
import random


# Example 12
def Example_12(args):
	# Example_12_01(args)
	# Example_12_02(args)
	# Example_12_03(args)
	# Example_12_04(args)
	Example_12_05(args)


# Example 12 - 1
def Example_12_01(args):
	"""
	Python 튜플 선언 방법
	- ()
	
	Ex)
	oValTuple = (1, 2, 3)
	
	튜플은 리스트와 달리 한번 생생되고 나면 더이상 기존 요소의 값을 변경하거나 새로운 값을 추가하는 것이 불가능하다. (즉, 튜플은 상수 버전
	리스트의 개념이라는 것을 알 수 있다.)
	"""
	oValTuple = (1, 2, 3)
	
	print("=====> 튜플 요소 <=====")
	print("{0}, {1}, {2}".format(oValTuple[0], oValTuple[1], oValTuple[2]))
	
	"""
	Python 셋 선언 방법
	- set()
	
	Ex)
	oValSet = set()
	
	셋은 집합을 나타내는 자료형이다. (즉, 셋은 중복 된 데이터를 허용하지 않는다는 것을 알 수 있다.)
	
	add 또는 update 메서드를 활용하면 셋에 새로운 데이터를 추가하는 것이 가능하다. (즉, add 메서드는 1 개의 데이터를 추가 할 때 사용되며
	update 메서드는 1 개 이상의 데이터를 추가 할 때 사용하는 것이 가능하다.)
	"""
	oValSet = set()
	
	for i in range(0, 10):
		"""
		random 모듈을 활용하면 랜덤한 값을 생성하는 것이 가능하다. (즉, 결과를 예측 할 수 없는 프로그램을 제작 할 때 활용된다는 것을
		알 수 있다.)
		"""
		oValSet.add(random.randint(1, 9))
	
	print("\n=====> 셋 요소 <=====")
	print("{0}".format(oValSet))


# Example 12 - 2
def Example_12_02(args):
	nScore = int(input("점수 입력 : "))
	
	# F 학점 일 경우
	if nScore < 60:
		print("F 학점입니다.")
	
	else:
		# A 학점 일 경우
		if nScore >= 90:
			print("A 학점입니다.")
		
		# B 학점 일 경우
		elif nScore >= 80:
			print("B 학점입니다.")
		
		# C 학점 일 경우
		elif nScore >= 70:
			print("C 학점입니다.")
		
		else:
			print("D 학점입니다.")


# Example 12 - 3
def Example_12_03(args):
	nNumVals = int(input("개수 입력 : "))
	oValList = []
	
	for i in range(0, nNumVals):
		nVal = int(input("{0} 번째 숫자 입력 : ".format(i + 1)))
		oValList.append(nVal)
	
	# 입력 된 숫자가 없을 경우
	if len(oValList) <= 0:
		print("입력 된 숫자가 없습니다.")
	
	else:
		nSumVal = 0
		
		for nVal in oValList:
			nSumVal += nVal
		
		"""
		Python 은 / (나눗셈) 연산자의 우항에 있는 피연산자가 0 일 경우 예외가 발생한다. (즉, 잘못된 연산으로 인해 프로그램이
		오작동 한다는 것을 의미한다.)
		
		따라서, 우항의 값이 0 이 될 가능성이 조금이라도 있다면 반드시 해당 연산자를 사용하기 전에 if ~ else 조건문 등으 활용해서
		예외처리를 해줘야한다.
		"""
		print("\n합계 : {0}".format(nSumVal))
		print("평균 : {0}".format(nSumVal / len(oValList)))


# Example 12 - 4
def Example_12_04(args):
	oValList = []
	
	while True:
		nVal = int(input("{0} 번째 숫자 입력 : ".format(len(oValList) + 1)))
		
		# 0 이하 값을 입력했을 경우
		if nVal <= 0:
			break
		
		oValList.append(nVal)
	
	# 입력 된 숫자가 없을 경우
	if len(oValList) <= 0:
		print("입력 된 숫자가 없습니다.")
	
	else:
		nSumVal = 0
		
		for nVal in oValList:
			nSumVal += nVal
		
		print("\n합계 : {0}".format(nSumVal))
		print("평균 : {0}".format(nSumVal / len(oValList)))


# Example 12 - 5
def Example_12_05(args):
	nVal = 0
	nAnswer = random.randint(1, 99)
	
	print("정답 : {0}\n".format(nAnswer))
	
	while nVal != nAnswer:
		nVal = int(input("숫자 입력 : "))
		
		# 정답 일 경우
		if nVal == nAnswer:
			print("정답입니다.")
		
		else:
			# 입력 한 숫자가 작을 경우
			if nVal < nAnswer:
				print("정답은 {0} 보다 높습니다.".format(nVal))
			
			else:
				print("정답은 {0} 보다 낮습니다.".format(nVal))
		
		print()
