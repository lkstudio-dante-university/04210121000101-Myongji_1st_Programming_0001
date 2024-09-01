import os
import sys

# Example 11 - 5
def E01Example_11_05(args):
	"""
	반복문을 비롯한 제어문은 중첩으로 사용하는 것이 가능하다. (즉, 반복문 내부에 다시 반복문을 작성함으로서 이중 루프 구조를 만드는 것이
	가능하다.)
	"""
	for i in range(2, 10):
		print("=====> {0} 단 <=====".format(i))
		
		for j in range(1, 10):
			print("{0} * {1} = {2}".format(i, j, i * j))
		
		print()
