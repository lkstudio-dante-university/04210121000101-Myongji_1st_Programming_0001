import os
import sys

g_nGlobalVal = 0

# Example 10 - 3
def E01Example_10_03(args):
	"""
	nLocalVal 변수는 Example_10_02 메서드 하위에 속해있는 지역 변수이기 떄문에 해당 지역을 벗어난 외부에서는 접근이 불가능하다.
	반면, g_nGlobalVal 변수는 전역 변수이기 때문에 프로그램 어디서든 접근 가능하다는 것을 알 수 있다.
	"""
	print("=====> 지역 변수 및 전역 변수 - 2 <=====")
	# print("지역 변수 : {0}".format(nLocalVal))
	print("전역 변수 : {0}".format(g_nGlobalVal))
	
	"""
	input 메서드란?
	- 콘솔 창으로부터 데이터를 입력 받을 수 있는 메서드를 의미한다. (즉, 해당 메서드를 활용하면 프로그램이 실행 중에 사용자로부터 특정
	데이터를 입력받는 것이 가능하다.)
	
	단, input 메서드는 콘솔 창으로부터 입력 받은 데이터를 문자열 데이터로 반환하기 때문에 정수 or 실수와 같은 숫자 데이터를 입력 받기 위해서는
	문자열 데이터를 숫자 데이터로 변환하는 추가적인 연산이 필요하다.
	"""
	oListTokens = input("\n정수 (2 개) 입력 : ").split()
	
	"""
	문자열 데이터를 정수 or 실수 데이터로 변환하기 위해서는 해당 자료형을 명시해주면 된다.
	
	Ex)
	int("10")		<- 문자열 10 을 정수 10 으로 변환
	float("3.14")	<- 문자열 3.14 를 실수 3.14 로 변환
	"""
	nValA = int(oListTokens[0])
	nValB = int(oListTokens[1])
	
	print("=====> 산술 연산자 <=====")
	print("{0} + {1} = {2}".format(nValA, nValB, nValA + nValB))
	print("{0} - {1} = {2}".format(nValA, nValB, nValA - nValB))
	print("{0} * {1} = {2}".format(nValA, nValB, nValA * nValB))
	print("{0} / {1} = {2}".format(nValA, nValB, nValA / nValB))
	print("{0} % {1} = {2}".format(nValA, nValB, nValA % nValB))
	print("{0} ** {1} = {2}".format(nValA, nValB, nValA ** nValB))
	print("{0} // {1} = {2}".format(nValA, nValB, nValA // nValB))
	
	"""
	관계 연산자 or 논리 연산자는 결과 값으로 참 or 거짓을 반환한다. (즉, bool 자료형 데이터를 연산 결과로 반환한다는 것을 알 수 있다.)
	"""
	print("\n=====> 관계 연산자 <=====")
	print("{0} < {1} = {2}".format(nValA, nValB, nValA < nValB))
	print("{0} > {1} = {2}".format(nValA, nValB, nValA > nValB))
	print("{0} <= {1} = {2}".format(nValA, nValB, nValA <= nValB))
	print("{0} >= {1} = {2}".format(nValA, nValB, nValA >= nValB))
	print("{0} == {1} = {2}".format(nValA, nValB, nValA == nValB))
	print("{0} != {1} = {2}".format(nValA, nValB, nValA != nValB))
	
	print("\n=====> 논리 연산자 <=====")
	print("{0} and {1} = {2}".format(nValA, nValB, nValA and nValB))
	print("{0} or {1} = {2}".format(nValA, nValB, nValA or nValB))
	print("not {0} = {1}".format(nValA, not nValA))
	
	"""
	^ 연산자는 XOR 연산자이다. (즉, 해당 연산자는 좌항과 우항이 서로 다른 경우 참이며 좌항과 우항이 같을 경우 거짓이 된다는 것을 알 수 있다.)
	"""
	print("\n=====> 비트 연산자 <=====")
	print("{0:08b} & {1:08b} = {2:08b}".format(nValA, nValB, nValA & nValB))
	print("{0:08b} | {1:08b} = {2:08b}".format(nValA, nValB, nValA | nValB))
	print("{0:08b} ^ {1:08b} = {2:08b}".format(nValA, nValB, nValA ^ nValB))
	print("{0:08b} << 1 = {1:08b}".format(nValA, nValA << 1))
	print("{0:08b} >> 1 = {1:08b}".format(nValB, nValB >> 1))
	print("~{0:08b} = {1:08b}".format(nValA, ~nValA + 1))
