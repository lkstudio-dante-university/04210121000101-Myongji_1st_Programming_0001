import os
import sys

# Example 11 - 1
def E01Example_11_01(args):
	"""
	Python 리스트 선언 방법
	- []
	- list()
	
	Ex)
	oListValues01 = []			<- 아무런 요소도 지니고 있지 않는 빈 리스트 생성
	oListValues02 = list()		<- 아무런 요소도 지니고 있지 않는 빈 리스트 생성
	oListValues03 = [1, 2, 3]	<- 정수 1, 2, 3 을 지니고 있는 리스트 생성
	
	append 또는 insert 메서드를 활용하면 리스트에 새로운 데이터를 추가하는 것이 가능하다. (즉, append 메서드는 리스트의 가장 마지막에
	새로운 데이터를 추가하는 반면 insert 메서드는 특정 위치에 새로운 데이터를 추가 할 수 있다는 차이점이 존재한다.)
	"""
	oListValues = list()
	oListValues.append(1)
	oListValues.append(2)
	oListValues.append(3)
	oListValues.append(4)
	oListValues.append(5)
	
	"""
	[ ] (인덱스 연산자) + 인덱스 번호를 활용하면 리스트에 존재하는 특정 데이터에 접근하는 것이 가능하다. 또한, 인덱스 번호는 0 부터 시작하기
	때문에 인덱스 번호의 범위는 0 ~ 리스트 길이 - 1 인 것을 알 수 있다.
	
	단, 잘못된 인덱스 번호를 명시하면 런타임 에러가 발생하기 때문에 주의가 필요하다. (즉, 인덱스 범위를 벗어난 번호를 명시 할 경우 프로그램이
	오작동 한다는 것을 알 수 있다.)
	"""
	oListValues[0] = 10
	
	print("=====> 리스트 <=====")
	print("{0}, {1}, {2}".format(oListValues[0], oListValues[1], oListValues[2]))
	
	"""
	del 키워드를 사용하면 리스트에 존재하는 특정 데이터를 제거하는 것이 가능하다. 또한, 여러 데이터를 한번에 제거하고 싶다면 슬라이싱 기능을
	활용하면 된다.
	
	슬라이싱이란?
	- 리스트에 존재하는 데이터의 일부분 or 전체를 잘라내는 기능을 의미한다. (즉, 슬라이싱을 활용하면 리스트에 존재하는 특정 데이터만으로
	이루어진 리스트를 손쉽게 만들어내는 것이 가능하다.)
	
	Ex)
	oListValues = [1, 2, 3, 4, 5]
	
	oListValues[0:3]       <- 정수 1, 2, 3 를 지니고 있는 리스트 생성
	oListValues[0:3:2]     <- 정수 1, 3 을 지니고 있는 리스트 생성
	
	del oListValues[0:2]	<- 정수 1, 2 를 제거 (즉, 해당 구문이 실행되면 기존 리스트에는 정수 3, 4, 5 만 남아 있다는 것을 알 수 있다.)
	"""
	del oListValues[0]
	del oListValues[0:2]
	
	"""
	\n 은 개행 문자로서 다음 줄로 이동시키는 역할을 수행한다.
	
	Ex)
	print("A\nB\nC")
	
	A
	B
	C
	
	위와 같이 개행 문자로 인해 A, B, C 가 각각 다른 줄에 출력되는 것을 확인 할 수 있다.
	"""
	print("\n=====> 리스트 - 삭제 후 <=====")
	print("{0}".format(oListValues))
	
	"""
	Python 딕셔너리 선언 방법
	- {}
	- dict()
	
	Ex)
	oDictValues01 = {}						<- 아무런 요소도 지니고 있지 않는 딕셔너리 생성
	oDictValues02 = dict()					<- 아무런 요소도 지니고 있지 않는 딕셔너리 생성
	oDictValues03 = {"1":1, "2":2, "3":3}	<- "1":1, "2":2, "3":3 을 지니고 있는 딕셔너리 생성
	
	[ ] (인덱스 연산자) + 키 데이터를 활용하면 딕셔너리에 새로운 데이터를 추가하거나 기존에 추가 된 데이터를 가져오는 것이 가능하다.
	(즉, 딕셔너리는 리스트와 달리 append 메서드와 같은 데이터를 추가하기 위한 메서드를 제공하지 않는다는 것을 알 수 있다.)
	
	단, 잘못된 키 데이터를 명시하면 런타임 에러가 발생하기 때문에 주의가 필요하다. (즉, 딕셔너리에 존재하지 않는 키 데이터를 명시 할
	경우 프로그램이 오작동한다는 것을 알 수 있다.)
	"""
	oDictValues = dict()
	oDictValues["Key_01"] = 1
	oDictValues["Key_02"] = 2
	oDictValues["Key_03"] = 3
	oDictValues["Key_04"] = 4
	oDictValues["Key_05"] = 5
	
	print("\n=====> 딕셔너리 <=====")
	print("{0}, {1}, {2}".format(oDictValues["Key_01"], oDictValues["Key_02"], oDictValues["Key_03"]))
	
	"""
	딕셔너리는 리스트와 달리 슬라이싱 기능을 제공하지 않기 때문에 여러 요소를 제거하기 위해서는 pop 메서드와 리스트 내포 기능을 활용해야한다.
	"""
	del oDictValues["Key_01"]
	[oDictValues.pop(oKey) for oKey in ["Key_02", "Key_03"]]
	
	print("\n=====> 딕셔너리 - 삭제 후 <=====")
	print("{0}".format(oDictValues))
