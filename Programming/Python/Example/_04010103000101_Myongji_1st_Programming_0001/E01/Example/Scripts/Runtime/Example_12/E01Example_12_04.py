import os
import sys

# Example 12 - 4
def E01Example_12_04(args):
	oListValues = []
	
	while True:
		nVal = int(input("{0} 번째 숫자 입력 : ".format(len(oListValues) + 1)))
		
		# 0 이하 값을 입력했을 경우
		if nVal <= 0:
			break
		
		oListValues.append(nVal)
	
	# 입력 된 숫자가 없을 경우
	if len(oListValues) <= 0:
		print("입력 된 숫자가 없습니다.")
	
	else:
		nVal_Sum = 0
		
		for nVal in oListValues:
			nVal_Sum += nVal
		
		print("\n합계 : {0}".format(nVal_Sum))
		print("평균 : {0}".format(nVal_Sum / len(oListValues)))
