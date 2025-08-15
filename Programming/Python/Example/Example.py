"""
import 키워드란?
- 라이브러리를 추가시키는 역할을 수행하는 키워드를 의미한다. (즉, 해당 키워드를 활용하면 Python 이 제공하는 공식 라이브러리 및
3rd Party 라이브러리 (비공식 라이브러리) 를 추가시켜서 사용하는 것이 가능하다.)

라이브러리란?
- 미리 제작 되어서 제공되는 기능의 모음을 의미한다. (즉, 라이브러리를 활용하면 특정 기능을 처음부터 제작 할 필요가 없기 때문에
작업 시간을 단축시키는 것이 가능하다.)

Python 은 라이브러리라는 용어보다는 모듈이라는 용어를 사용하며 특정 모듈을 추가시키기 위해서는 from 또는 import 키워드를 사용하면 된다.

일반적으로 import 키워드보다는 from 키워드가 좀 더 많이 활용되며 from 키워드를 사용하면 * (와일드 카드) 를 통해 특정 모듈에 존재하는
기능을 손쉽게 모두 가져오는 것이 가능하다.
"""
import os
import sys

from _04210121000101_Myongji_1st_Programming_0001.E01.Example.Scripts.Runtime.Example_09.E01Example_09 import E01Example_09
from _04210121000101_Myongji_1st_Programming_0001.E01.Example.Scripts.Runtime.Example_10.E01Example_10 import E01Example_10
from _04210121000101_Myongji_1st_Programming_0001.E01.Example.Scripts.Runtime.Example_11.E01Example_11 import E01Example_11
from _04210121000101_Myongji_1st_Programming_0001.E01.Example.Scripts.Runtime.Example_12.E01Example_12 import E01Example_12
from _04210121000101_Myongji_1st_Programming_0001.E01.Example.Scripts.Runtime.Example_13.E01Example_13 import E01Example_13
from _04210121000101_Myongji_1st_Programming_0001.E01.Example.Scripts.Runtime.Example_14.E01Example_14 import E01Example_14

from _04210121000101_Myongji_1st_Programming_0001.E01.Practice.Scripts.Runtime.Practice_12.P01Practice_12 import P01Practice_12
from _04210121000101_Myongji_1st_Programming_0001.E01.Practice.Scripts.Runtime.Practice_15.P01Practice_15 import P01Practice_15

"""
Python 학습 사이트
- 생활 코딩 (https://opentutorials.org/course/4769)
- 점프 투 파이썬 (https://wikidocs.net/book/1)

주석이란?
- Python 인터프리터에 의해서 기계어로 변환되지 않는 구문을 의미한다. (즉, 주석은 컴퓨터가 아닌 사용자를 위한 기능이라는 것을 알 수 있다.)
주석은 Python 을 비롯한 대부분의 고수준 언어에서 지원하는 기능으로 해당 기능은 주로 메모 기능으로 활용된다.

한번 작성 된 명령문은 시간이 지남에 따라 개선이 필요하기 때문에 지속적으로 관리되고 보안 될 필요가 있다. (즉, 기존에 작성 된 명령문이 복잡
할 수록 해당 명령문을 분석하는 시간이 소요된다는 것을 알 수 있다.)

따라서, 주석을 통해 명령문의 동작 방식이나 원리 등을 메모해놓는다면 이 후에 해당 명령문을 다시 해석 할 때 소요되는 시간을 단축시키는 것이
가능하다.

Python 주석 사용 방법
- #

Python 의 주석은 # 기호롤 시작한다. (즉, 해당 기호 이후에 작성한 문장은 모두 주석이 된다는 것을 알 수 있다.)

들여쓰기란?
- Python 은 특정 영역을 의미하는 연산자 (기호) 가 별도로 존재하지 않기 떄문에 들여쓰기를 통해서 영역을 구분한다. (즉, 동일한 명령문이라고
하더라도 들여쓰기 수준에 따라 잘못된 동작을 할 수 있다는 것을 의미한다.)

Python 은 들여쓰기도 문법이기 때문에 다른 일반적인 고수준 언어처럼 자유롭게 명령문을 구성하는데 제약이 따른다는 단점이 존재한다.
또한, 들여쓰기는 탭 문자와 공백 문자 모두 사용하는 것이 가능하지만 두 문자를 섞어서 사용하는 것은 추천하지 않는다. (즉, 탭이나 공백 중 하나로
통일해야 잘못 된 들여쓰기에 의한 문제를 사전에 예방 할 수 있다.)

메인 모듈이란?
- 가장 먼저 실행 된 Python 파일을 메인 모듈이라고 한다.
Python 은 진입 메서드가 따로 존재하지 않기 때문에 어떤 파일이 먼저 실행되는지에 따라 프로그램의 결과가 달라지는 단점이 존재한다.

따라서, 항상 동일한 결과를 만들어내기 위해 사용자 (프로그래머) 가 명시적으로 진입 메서드의 역할을 하는 구문을 작성 할 필요가 있으며
현재 모듈의 이름을 비교하는 것으로 해당 구문을 작성 할 수 있다. (즉, __name__ 은 모든 모듈이 지니고 있는 전역 변수이며 해당 변수의 데이터가
__main__ 와 같다면 해당 모듈이 가장 먼저 실행 된 Python 파일이라는 것을 알 수 있다.)
"""
# 메인 모듈 일 경우
if __name__ == "__main__":
	"""
	sys.argv 를 활용하면 Python 프로그램이 실행 될 때 추가적으로 입력 된 데이터를 가져오는 것이 가능하다. (즉, 해당 변수를 활용하면
	프로그램이 시작 될 때 입력 된 데이터를 가져와서 다양한 만들어 낼 수 있다는 것을 알 수 있다.)
	
	Ex)
	python [확장자를 포함한 파이썬 파일 경로] A B C
	
	명령 프롬프트 (맥의 경우 터미널에 해당) 상에서 해당 명령어를 통해 특정 Python 파일을 실행했을 경우 sys.argv 에는 실행한 파일의 경로와
	더불어 A, B, C 데이터도 같이 전달 된다는 것을 알 수 있다.
	"""
	# E01Example_09(sys.argv)
	# E01Example_10(sys.argv)
	# E01Example_11(sys.argv)
	# E01Example_12(sys.argv)
	# E01Example_13(sys.argv)
	# E01Example_14(sys.argv)

	# P01Practice_12(sys.argv)
	P01Practice_15(sys.argv)
