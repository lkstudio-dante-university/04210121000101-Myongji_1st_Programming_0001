import os
import sys

"""
Python 변수 종류
- 지역 변수
- 전역 변수

지역 변수 vs 전역 변수
- 지역 변수는 특정 영역에 속해있는 변수를 의미하며 해당 변수가 선언 된 지역 내부에서만 사용 할 수 있다는 특징이 존재한다. 반면, 전역 변수는
특정 영역에 속해 읺지 않은 변수를 의미하며 프로그램 전체에서 사용 가능하다는 차이점이 존재한다. (즉, 지역 변수는 해당 변수가 선언 된 영역을
벗어나면 사라지는 특징이 있다는 것을 알 수 있다.)

Python 에서 특정 지역은 : (콜론) 기호로 시작한다. (즉, 해당 기호 하위에 선언 된 변수 또는 매개 변수는 지역 변수라는 것을 의미한다.)

Python 변수 선언 방법
- 변수 이름 + 자료형 (옵션) + 초기화 데이터

Ex)
nVal = 0
nVal: int = 0

Python 은 강력 형식 언어 (Strong Type Language) 가 아니기 때문에 자료형을 명시하지 않고 변수를 선언하는 것이 가능하다.
(즉, Python 은 변수가 관리하는 데이터의 자료형을 제한하지 않는다는 것을 알 수 있다.)

단, Python 은 변수에 자료형을 명시하는 기능을 제공하며 해당 기능을 활용하면 에디터의 인텔리센스 기능의 도움을 받는 것이 가능하다.
(즉, 지역 변수나 매개 변수는 초기화 데이터를 통해 에디터가 해당 변수의 자료형을 유추하는 것이 가능하지만 매개 변수는 초기화 데이터가 존재하지
않기 때문에 자료형을 명시하지 않으면 에디터의 인텔리센스 기능이 동작하지 않는다.)

연산자란?
- 프로그램이 동작하는데 특별한 역할을 수행하는 기호 (심볼) 을 의미한다. (즉, 연산자를 활용하면 특정 데이터를 프로그램의 목적에 맞게 처리하는
것이 가능하다는 것을 알 수 있다.)

Python 연산자 종류
- 산술 연산자 (+, -, *, /, %, **, //)
- 관계 연산자 (<, >, <=, >=, ==, !=)
- 할당 연산자 (=, +=, -=, *=, /=, 등등...)
- 논리 연산자 (and, or, not)
- 비트 연산자 (&, |, ^, <<, >>, ~)
"""


# Example 10
def Example_10(args):
	# Example_10_01(args)
	# Example_10_02(args)
	Example_10_03(args)


# Example 10 - 1
def Example_10_01(args):
	nVal = 10
	fVal = 3.14
	bIsTrue = True
	
	print("=====> 값 형식 자료형 <=====")
	print("{0}, {1}".format(nVal, type(nVal)))
	print("{0}, {1}".format(fVal, type(fVal)))
	print("{0}, {1}".format(bIsTrue, type(bIsTrue)))
	
	oStr = "Hello, World!"
	oList = [1, 2, 3, 4, 5]
	oDict = {"Key_01": 1, "Key_02": 2, "Key_03": 3, "Key_04": 4, "Key_05": 5}
	oTuple = (1, 2, 3, 4, 5)
	
	print("\n=====> 참조 형식 자료형 <=====")
	print("{0}, {1}".format(oStr, type(oStr)))
	print("{0}, {1}".format(oList, type(oList)))
	print("{0}, {1}".format(oDict, type(oDict)))
	print("{0}, {1}".format(oTuple, type(oTuple)))


g_nGlobalVal = 0


# Example 10 - 2
def Example_10_02(args):
	"""
	특정 영역 내부에서 외부에 존재하는 전역 변수에 접근하기 위해서는 반드시 global 키워드를 사용해야한다. (즉, global 키워드는 해당 변수가
	지역 변수가 아닌 전역 변수라는 것을 Python 인터프리터에게 알리는 역할을 수행한다.)
	"""
	nLocalVal = 10
	global g_nGlobalVal
	
	g_nGlobalVal = 20
	
	print("=====> 지역 변수 및 전역 변수 - 1 <=====")
	print("지역 변수 : {0}".format(nLocalVal))
	print("전역 변수 : {0}".format(g_nGlobalVal))


# Example 10 - 3
def Example_10_03(args):
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
	
	할당 연산자란?
	- 우항에 명시 된 데이터를 좌항에 명시 된 변수에 저장하는 연산자를 의미한다. (즉, 특정 변수에 데이터를 저장하기 위해서는 할당 연산자를
	활용하면 된다는 것을 알 수 있다.)
	"""
	oTokenList = input("\n정수 (2 개) 입력 : ").split()
	
	nVal01 = int(oTokenList[0])
	nVal02 = int(oTokenList[1])
	
	print("=====> 산술 연산자 <=====")
	print("{0} + {1} = {2}".format(nVal01, nVal02, nVal01 + nVal02))
	print("{0} - {1} = {2}".format(nVal01, nVal02, nVal01 - nVal02))
	print("{0} * {1} = {2}".format(nVal01, nVal02, nVal01 * nVal02))
	print("{0} / {1} = {2}".format(nVal01, nVal02, nVal01 / nVal02))
	print("{0} % {1} = {2}".format(nVal01, nVal02, nVal01 % nVal02))
	print("{0} ** {1} = {2}".format(nVal01, nVal02, nVal01 ** nVal02))
	print("{0} // {1} = {2}".format(nVal01, nVal02, nVal01 // nVal02))
	
	"""
	관계 연산자란?
	- 데이터의 대/소 여부를 판단하기 위한 연산자를 의미한다. (즉, 해당 연산자의 결과는 참 or 또는 거짓을 나타내는 bool 형 데이터가
	반환된다는 것을 알 수 있다.)
	"""
	print("\n=====> 관계 연산자 <=====")
	print("{0} < {1} = {2}".format(nVal01, nVal02, nVal01 < nVal02))
	print("{0} > {1} = {2}".format(nVal01, nVal02, nVal01 > nVal02))
	print("{0} <= {1} = {2}".format(nVal01, nVal02, nVal01 <= nVal02))
	print("{0} >= {1} = {2}".format(nVal01, nVal02, nVal01 >= nVal02))
	print("{0} == {1} = {2}".format(nVal01, nVal02, nVal01 == nVal02))
	print("{0} != {1} = {2}".format(nVal01, nVal02, nVal01 != nVal02))
	
	print("\n=====> 논리 연산자 <=====")
	print("{0} and {1} = {2}".format(nVal01, nVal02, nVal01 and nVal02))
	print("{0} or {1} = {2}".format(nVal01, nVal02, nVal01 or nVal02))
	print("not {0} = {1}".format(nVal01, not nVal01))
	
	"""
	비트 연산자란?
	- 프로그래밍 언어의 기본 단위는 바이트이기 때문에 대부분의 연산자는 바이트 단위로 동작하는 특징이 존재한다. 반면, 비트 연산자는 비트 단위로
	데이터를 제어하는 것이 가능하다. (즉, 비트 단위로 데이터를 제어함으로서 프로그램이 사용하는 메모리를 최소화 시키는 것이 가능하다.)
	"""
	print("\n=====> 비트 연산자 <=====")
	print("{0:08b} & {1:08b} = {2:08b}".format(nVal01, nVal02, nVal01 & nVal02))
	print("{0:08b} | {1:08b} = {2:08b}".format(nVal01, nVal02, nVal01 | nVal02))
	print("{0:08b} ^ {1:08b} = {2:08b}".format(nVal01, nVal02, nVal01 ^ nVal02))
	print("{0:08b} << 1 = {1:08b}".format(nVal01, nVal01 << 1))
	print("{0:08b} >> 1 = {1:08b}".format(nVal02, nVal02 >> 1))
	print("~{0:08b} = {1:08b}".format(nVal01, ~nVal01 + 1))
