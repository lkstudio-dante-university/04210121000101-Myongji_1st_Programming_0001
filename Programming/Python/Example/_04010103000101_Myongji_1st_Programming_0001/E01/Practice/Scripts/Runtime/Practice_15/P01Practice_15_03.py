import os
import sys
import random


# Practice 15 - 3
def P01Practice_15_03(args):
	oAnswer = []
	P01SetupAnswer_15_03(oAnswer)
	
	print("정답 : {0}\n".format(oAnswer))
	
	while True:
		oListTokens = input("숫자 (4 개) 입력 : ").split()
		
		nNumBalls = 0
		nNumStrikes = 0
		
		for i in range(0, len(oAnswer)):
			oDigit = str(oAnswer[i])
			
			nNumBalls += 1 if oDigit in oListTokens and i != oListTokens.index(oDigit) else 0
			nNumStrikes += 1 if oDigit in oListTokens and i == oListTokens.index(oDigit) else 0
		
		print("결과 : {0} Strike, {1} Ball\n".format(nNumStrikes, nNumBalls))
		
		# 게임이 종료 되었을 경우
		if nNumStrikes >= len(oAnswer):
			break
	
	print("게임을 종료합니다.")


# 정답을 설정한다
def P01SetupAnswer_15_03(a_oAnswer: list):
	while len(a_oAnswer) < 4:
		nVal = random.randint(1, 9)
		
		# 중복 값이 없을 경우
		if nVal not in a_oAnswer:
			a_oAnswer.append(nVal)
