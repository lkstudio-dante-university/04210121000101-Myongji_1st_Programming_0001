import os
import sys

from Example.Classes.Example_13.Example_13_01 import *
from Example.Classes.Example_13.Example_13_02 import *

"""
Python 메서드 구현 방법
- def + 메서드 이름 + 매개 변수 + 메서드 몸체

Python 메서드 호출 방법
- 메서드 이름 + ( ) (메서드 호출 연산자)

메서드 내부에 구현 된 메서드를 실행하기 위해서는 해당 메서드를 호출 (실행) 해줘야한다. (즉, 메서드를 호출하지 않으면 해당 메서드에 명시 된
명령문이 동작하지 않는다는 것을 알 수 있다.)

Ex)
def SomeMethodA():
	# 메서드 몸체
	
def SomeMethodB(a_nLhs, a_nRhs):
	# 메서드 몸체

SomeMethodA()
SomeMethodB(10, 20)

매개 변수란?
- 메서드가 호출 (실행) 될 때 입력으로 전달 된 데이터를 저장하는 변수를 의미한다. (즉, 매개 변수는 일반적인 변수처럼 데이터를 저장하거나
읽어들일 수 있는 공간을 의미한다.)

호출하고자하는 메서드에 입력 데이터 (매개 변수) 가 존재 할 경우 반드시 매개 변수 개수만큼 데이터를 전달 할 필요가 있다.

메서드 몸체란?
- 메서드가 실제로 처리 할 명령문을 의미한다. (즉, 메서드 몸체는 특정 메서드 하위 영역에 위치하기 떄문에 반드시 들여쓰기를 통해 특정 메서드
영역 하위에 위치해있다는 것을 Python 인터프리터에게 알려 줄 필요가 있다.)

Python 메서드 유형
- 입력 O, 출력 O
- 입력 O, 출력 X
- 입력 X, 출력 O
- 입력 X, 출력 X

Python 의 메서드는 입/출력 값의 유/무에 따라 크게 4 가지 유형으로 나뉜다는 것을 알 수 있다.
"""


# Example 13
def Example_13(args):
	# Example_13_01(args)
	Example_13_02(args)
