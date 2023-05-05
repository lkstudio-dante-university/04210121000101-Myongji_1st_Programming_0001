import os
import sys


# Example 11
def Example_11(args):
	# Example_11_01(args)
	# Example_11_02(args)
	Example_11_03(args)


# Example 11 - 1
def Example_11_01(args):
	"""
	append 또는 insert 메서드를 활용하면 리스트에 새로운 데이터를 추가하는 것이 가능하다. (즉, append 메서드는 리스트의 가장 마지막에
	새로운 데이터를 추가하는 반면 insert 메서드는 특정 위치에 새로운 데이터를 추가 할 수 있다는 차이점이 존재한다.)
	"""
	oValList = list()
	oValList.append(1)
	oValList.append(2)
	oValList.append(3)
	
	"""
	[ ] (인덱스 연산자) + 인덱스 번호를 활용하면 리스트에 존재하는 특정 데이터에 접근하는 것이 가능하다. 또한, 인덱스 번호는 0 부터 시작하기
	때문에 인덱스 번호의 범위는 0 ~ 리스트 길이 - 1 인 것을 알 수 있다.
	"""
	print("=====> 리스트 요소 <=====")
	print("{0}, {1}, {2}".format(oValList[0], oValList[1], oValList[2]))
	
	"""
	del 키워드를 사용하면 리스트에 존재하는 특정 데이터를 제거하는 것이 가능하다. 또한, 여러 데이터를 한번에 제거하고 싶다면 슬라이싱 기능을
	활용하면 된다.
	
	슬라이싱이란?
	- 리스트에 존재하는 데이터의 일부분 or 전체를 잘라내는 기능을 의미한다. (즉, 슬라이싱을 활용하면 리스트에 존재하는 특정 데이터만으로
	이루어진 리스트를 손쉽게 만들어내는 것이 가능하다.)
	
	Ex)
	oValList = [1, 2, 3, 4, 5]
	
	oValList[0:3]       <- [1, 2, 3] 요소를 반환한다.
	oValList[0:3:2]     <- [1, 3] 요소를 반환한다.
	"""
	del oValList[0]
	
	print("\n=====> 리스트 요소 - 삭제 후 <=====")
	print("{0}".format(oValList))
	
	"""
	[ ] (인덱스 연산자) + 키 데이터를 활용하면 딕셔너리에 새로운 데이터를 추가하거나 기존에 추가 된 데이터를 가져오는 것이 가능하다.
	(즉, 딕셔너리는 리스트와 달리 append 메서드와 같은 데이터를 추가하기 위한 메서드를 제공하지 않는다는 것을 알 수 있다.)
	"""
	oValDict = dict()
	oValDict["Key_01"] = 1
	oValDict["Key_02"] = 2
	oValDict["Key_03"] = 3
	
	print("\n=====> 딕셔너리 요소 <=====")
	print("{0}, {1}, {2}".format(oValDict["Key_01"], oValDict["Key_02"], oValDict["Key_03"]))
	
	del oValDict["Key_01"]
	
	print("\n=====> 딕셔너리 요소 - 삭제 후 <=====")
	print("{0}".format(oValDict))


# Example 11 - 2
def Example_11_02(args):
	oTokenList = input("수식 입력 : ").split()
	
	nVal01 = int(oTokenList[0])
	nVal02 = int(oTokenList[2])
	
	# + 연산자 일 경우
	if oTokenList[1] == "+":
		print("{0} + {1} = {2}".format(nVal01, nVal02, nVal01 + nVal02))
	
	# - 연산자 일 경우
	elif oTokenList[1] == "-":
		print("{0} - {1} = {2}".format(nVal01, nVal02, nVal01 - nVal02))
	
	# * 연산자 일 경우
	elif oTokenList[1] == "*":
		print("{0} * {1} = {2}".format(nVal01, nVal02, nVal01 * nVal02))
	
	# / 연산자 일 경우
	elif oTokenList[1] == "/":
		print("{0} / {1} = {2}".format(nVal01, nVal02, nVal01 / nVal02))
	
	else:
		print("잘못된 수식을 입력했습니다.")


# Example 11 - 3
def Example_11_03(args):
	pass
