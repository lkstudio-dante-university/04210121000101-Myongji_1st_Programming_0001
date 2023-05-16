import os
import sys


# Example 11
def Example_11(args):
	Example_11_01(args)
	# Example_11_02(args)
	# Example_11_03(args)
	# Example_11_04(args)


# Example 11 - 1
def Example_11_01(args):
	"""
	Python 리스트 선언 방법
	- []
	- list()
	
	Ex)
	oValList01 = []			<- 아무런 요소도 지니고 있지 않는 빈 리스트 생성
	oValList02 = list()		<- 아무런 요소도 지니고 있지 않는 빈 리스트 생성
	oValList03 = [1, 2, 3]	<- 정수 1, 2, 3 을 지니고 있는 리스트 생성
	
	append 또는 insert 메서드를 활용하면 리스트에 새로운 데이터를 추가하는 것이 가능하다. (즉, append 메서드는 리스트의 가장 마지막에
	새로운 데이터를 추가하는 반면 insert 메서드는 특정 위치에 새로운 데이터를 추가 할 수 있다는 차이점이 존재한다.)
	"""
	oValList = list()
	oValList.append(1)
	oValList.append(2)
	oValList.append(3)
	oValList.append(4)
	oValList.append(5)
	
	"""
	[ ] (인덱스 연산자) + 인덱스 번호를 활용하면 리스트에 존재하는 특정 데이터에 접근하는 것이 가능하다. 또한, 인덱스 번호는 0 부터 시작하기
	때문에 인덱스 번호의 범위는 0 ~ 리스트 길이 - 1 인 것을 알 수 있다.
	
	단, 잘못된 인덱스 번호를 명시하면 런타임 에러가 발생하기 때문에 주의가 필요하다.
	"""
	oValList[0] = 10
	
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
	
	oValList[0:3]       <- 정수 1, 2, 3 를 지니고 있는 리스트 생성
	oValList[0:3:2]     <- 정수 1, 3 을 지니고 있는 리스트 생성
	
	del oValList[0:2]	<- 정수 1, 2 를 제거 (즉, 해당 구문이 실행되면 기존 리스트에는 정수 3, 4, 5 만 남아 있다는 것을 알 수 있다.)
	"""
	del oValList[0]
	del oValList[0:2]
	
	print("\n=====> 리스트 요소 - 삭제 후 <=====")
	print("{0}".format(oValList))
	
	"""
	Python 딕셔너리 선언 방법
	- {}
	- dict()
	
	Ex)
	oValDict01 = {}						<- 아무런 요소도 지니고 있지 않는 딕셔너리 생성
	oValDict02 = dict()					<- 아무런 요소도 지니고 있지 않는 딕셔너리 생성
	oValDict03 = {"1":1, "2":2, "3":3}	<- "1"/1, "2"/2, "3"/3 을 지니고 있는 딕셔너리 생성
	
	[ ] (인덱스 연산자) + 키 데이터를 활용하면 딕셔너리에 새로운 데이터를 추가하거나 기존에 추가 된 데이터를 가져오는 것이 가능하다.
	(즉, 딕셔너리는 리스트와 달리 append 메서드와 같은 데이터를 추가하기 위한 메서드를 제공하지 않는다는 것을 알 수 있다.)
	
	단, 잘못된 키 데이터를 명시하면 런타임 에러가 발생하기 때문에 주의가 필요하다.
	"""
	oValDict = dict()
	oValDict["Key_01"] = 1
	oValDict["Key_02"] = 2
	oValDict["Key_03"] = 3
	oValDict["Key_04"] = 4
	oValDict["Key_05"] = 5
	
	print("\n=====> 딕셔너리 요소 <=====")
	print("{0}, {1}, {2}".format(oValDict["Key_01"], oValDict["Key_02"], oValDict["Key_03"]))
	
	"""
	딕셔너리는 리스트와 달리 슬라이싱 기능을 제공하지 않기 때문에 여러 요소를 제거하기 위해서는 pop 메서드와 리스트 내포 기능을 활용해야한다.
	"""
	del oValDict["Key_01"]
	[oValDict.pop(oKey) for oKey in ["Key_02", "Key_03"]]
	
	print("\n=====> 딕셔너리 요소 - 삭제 후 <=====")
	print("{0}".format(oValDict))


# Example 11 - 2
def Example_11_02(args):
	oTokenList = input("수식 입력 : ").split()
	
	nVal01 = int(oTokenList[0])
	nVal02 = int(oTokenList[2])
	
	"""
	특정 조건을 만족 할 경우 실행 될 명령문은 반드시 if ~ else 조건문보다 한 수준 들여쓰기가 적용되어 있어야한다. (즉, 들여쓰기가 안되어있다면
	해당 명령문은 if ~ else 조건문과는 별개의 명령문이라는 것을 알 수 있다.)
	
	따라서, 조건문과 같이 하위 영역을 지니는 명령문은 : (클론) 기호와 들여쓰기를 통해 구분하는 것이 가능하다.
	"""
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
	elif oTokenList[1] == "/" and nVal02 != 0:
		print("{0} / {1} = {2}".format(nVal01, nVal02, nVal01 / nVal02))
	
	else:
		print("잘못된 수식을 입력했습니다.")


# Example 11 - 3
def Example_11_03(args):
	i = 0
	print("=====> while 반복문 <=====")
	
	"""
	while 반복문 사용 방법
	- while + 조건 + 반복 할 명령문
	"""
	while i < 10:
		print("{0}, ".format(i + 1), end="")
		i += 1
	
	print("\n\n=====> for 반복문 <=====")
	
	"""
	for 반복문 사용 방법
	- for + 반복 변수 + 컬렉션
	
	for 반복문은 컬렉션 or 반복 가능한 객체를 대상으로 동작한다. (즉, for 반복문은 특정 컬렉션을 순회하는 것이 주된 목적이기 때문에
	순회문이라고도 불린다.)
	
	range 메서드는 입력으로 전달 된 데이터를 기반으로 반복 가능한 객체를 생성하는 역할을 수행한다. (즉, 해당 메서드를 활용하면 특정 횟수만큼
	반복하도록 for 반복문의 조건을 명시하는 것이 가능하다.)
	"""
	for i in range(0, 10):
		print("{0}, ".format(i + 1), end="")
		
	print()


# Example 11 - 4
def Example_11_04(args):
	"""
	반복문을 비롯한 제어문은 중첩으로 사용하는 것이 가능하다. (즉, 반복문 내부에 다시 반복문을 작성함으로서 이중 루프 구조를 만드는 것이
	가능하다.)
	"""
	for i in range(2, 10):
		print("=====> {0} 단 <=====".format(i))
		
		for j in range(1, 10):
			print("{0} * {1} = {2}".format(i, j, i * j))
		
		print()
