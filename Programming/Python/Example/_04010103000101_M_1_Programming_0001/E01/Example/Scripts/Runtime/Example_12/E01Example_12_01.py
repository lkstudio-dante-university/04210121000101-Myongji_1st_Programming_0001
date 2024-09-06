import os
import sys
import random

# Example 12 - 1
def E01Example_12_01(args):
	"""
	Python 튜플 선언 방법
	- ()
	
	Ex)
	oTupleValues = (1, 2, 3)
	
	튜플은 리스트와 달리 한번 생생되고 나면 더이상 기존 요소의 값을 변경하거나 새로운 값을 추가하는 것이 불가능하다. (즉, 튜플은 상수 버전
	리스트의 개념이라는 것을 알 수 있다.)
	"""
	oTupleValues = (1, 2, 3)
	
	print("=====> 튜플 요소 <=====")
	print("{0}, {1}, {2}".format(oTupleValues[0], oTupleValues[1], oTupleValues[2]))
	
	"""
	Python 셋 선언 방법
	- set()
	
	Ex)
	oSetValues = set()
	
	셋은 집합을 나타내는 자료형이다. (즉, 셋은 중복 된 데이터를 허용하지 않는다는 것을 알 수 있다.)
	
	add 또는 update 메서드를 활용하면 셋에 새로운 데이터를 추가하는 것이 가능하다. (즉, add 메서드는 1 개의 데이터를 추가 할 때 사용되며
	update 메서드는 1 개 이상의 데이터를 추가 할 때 사용하는 것이 가능하다.)
	"""
	oSetValues = set()
	
	for i in range(0, 10):
		"""
		random 모듈을 활용하면 랜덤한 값을 생성하는 것이 가능하다. (즉, 결과를 예측 할 수 없는 프로그램을 제작 할 때 활용된다는 것을
		알 수 있다.)
		"""
		oSetValues.add(random.randint(1, 9))
	
	print("\n=====> 셋 요소 <=====")
	print("{0}".format(oSetValues))
