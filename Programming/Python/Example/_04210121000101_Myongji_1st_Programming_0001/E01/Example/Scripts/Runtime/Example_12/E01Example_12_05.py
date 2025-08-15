import os
import sys
import random

# Example 12 - 5
def E01Example_12_05(args):
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
