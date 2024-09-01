import os
import sys

# Example 12 - 2
def E01Example_12_02(args):
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
