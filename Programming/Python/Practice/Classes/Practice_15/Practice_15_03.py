import os
import sys
import random


# Practice 15 - 3
def Practice_15_03(args):
	oAnswer = []
	P15_03SetupAnswer(oAnswer)
	
	print("정답 : {0}\n".format(oAnswer))
	
	while True:
		oTokenList = input("숫자 (4 개) 입력 : ").split()
		
		nNumBalls = 0
		nNumStrikes = 0
		
		for i in range(0, len(oAnswer)):
			oDigit = str(oAnswer[i])
			
			nNumBalls += 1 if oDigit in oTokenList and i != oTokenList.index(oDigit) else 0
			nNumStrikes += 1 if oDigit in oTokenList and i == oTokenList.index(oDigit) else 0
		
		print("결과 : {0} Strike, {1} Ball\n".format(nNumStrikes, nNumBalls))
		
		# 게임이 종료 되었을 경우
		if nNumStrikes >= len(oAnswer):
			break
	
	print("게임을 종료합니다.")


# 정답을 설정한다
def P15_03SetupAnswer(a_oAnswer: list):
	while len(a_oAnswer) < 4:
		nVal = random.randint(1, 9)
		
		# 중복 값이 없을 경우
		if nVal not in a_oAnswer:
			a_oAnswer.append(nVal)
