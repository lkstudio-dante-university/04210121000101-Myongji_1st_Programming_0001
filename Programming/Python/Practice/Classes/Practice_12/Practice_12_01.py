import os
import sys


# Practice 12 - 1
def Practice_12_01(args):
	nScore = int(input("점수 입력 : "))
	
	# F 학점 일 경우
	if nScore < 60:
		print("F 학점입니다.")
	
	else:
		# A 학점 일 경우
		if nScore >= 90:
			print("A", end="")
		
		# B 학점 일 경우
		elif nScore >= 80:
			print("B", end="")
		
		# C 학점 일 경우
		elif nScore >= 70:
			print("C", end="")
		
		else:
			print("D", end="")
		
		# + 학점 일 경우
		if nScore >= 100 or nScore % 10 >= 7:
			print("+ 학점입니다.")
		
		# - 학점 일 경우
		elif nScore % 10 <= 3:
			print("- 학점입니다.")
		
		else:
			print("0 학점입니다.")
