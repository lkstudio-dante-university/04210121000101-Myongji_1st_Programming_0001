import os
import sys

g_nGlobalVal = 0

# Example 10 - 2
def E01Example_10_02(args):
	nLocalVal = 10
	
	global g_nGlobalVal
	g_nGlobalVal = 10
	
	print("=====> 지역 변수 및 전역 변수 - 1 <=====")
	print("지역 변수 : {0}".format(nLocalVal))
	print("전역 변수 : {0}".format(g_nGlobalVal))
