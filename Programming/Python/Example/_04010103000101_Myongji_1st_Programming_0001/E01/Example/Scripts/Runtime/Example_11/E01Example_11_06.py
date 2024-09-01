import os
import sys

# Example 11 - 6
def E01Example_11_06(args):
	i = 0
	print("=====> while - continue <=====")
	
	while i < 10:
		print("{0}, ".format(i + 1), end="")
		
		# 짝수 일 경우
		if (i + 1) % 2 <= 0:
			"""
			continue 키워드는 반복문 내부에서 사용 할 수 있으며 해당 키워드를 명시하면 프로그램의 현재 흐름을 생략하는 것이 가능하다.
			(즉, while 반복문 내부에서 해당 키워드를 명시 할 경우 프로그램의 흐름을 바로 조건절로 이동시킨다는 것을 알 수 있다.)
			
			단, while 반목문 내부에서 continue 키워드를 사용 할 경우 무한 루프 발생 가능 여부를 항상 염두해둬야한다. (즉, 반복 조건을
			끝내기 위한 명령문의 실행을 생략함으로서 의도치 않게 무한 루프가 발생 할 수 있다는 것을 알 수 있다.)
			"""
			i += 1
			continue
		
		i += 1
	
	print("\n\n=====> for - continue <=====")
	
	for i in range(0, 10):
		print("{0}, ".format(i + 1), end="")
		
		# 짝수 일 경우
		if (i + 1) % 2 <= 0:
			"""
			for 반복문은 while 반복문과 달리 반복문 내부에 continue 키워드를 명시해도 무한 루프가 발생 할 확률이 없기 때문에
			while 반복문에 비해 안전하게 명령문을 작성하는 것이 가능하다.
			"""
			continue
	
	print("\n\n=====> for - break <=====")
	
	for i in range(0, 10):
		print("{0}, ".format(i + 1), end="")
		
		# 짝수 일 경우
		if (i + 1) % 2 <= 0:
			"""
			break 키워드는 continue 와 마찬가지로 반복문 내부에 명시하는 것이 가능하며 해당 키워드는 프로그램의 흐름을 반복문 외부로
			이동시키는 역할을 수행한다. (즉, 반복문 내부에 해당 키워드를 명시 할 경우 가장 반복문이 종료 된다는 것을 알 수 있다.)
			
			단, break 키워드와 continue 키워드 모두 가장 가까운 반복문에만 영향을 미친다. (즉, 2 개 이상의 반복문이 중첩 되어 있을 경우
			안쪽 반복문에서 break 키워드를 명시해도 반복문이 종료 되지 않을 수 있다는 것을 의미한다.)
			
			Ex)
			for i in range(0, 10):
				for j in range(0, 10):
					break
					
			위의 경우 break 키워드에 의해 안쪽 반복문은 종료가 되지만 바깥쪽에 반복문이 존재하기 때문에 다시 안쪽 반복문이 실행 된다는
			것을 알 수 있다.
			"""
			break
	
	print()
