import os
import sys

# Example 11 - 4
def E01Example_11_04(args):
	nVal = int(input("구구단 입력 : "))
	
	for i in range(1, 10):
		print("{0} * {1} = {2}".format(nVal, i, nVal * i))
