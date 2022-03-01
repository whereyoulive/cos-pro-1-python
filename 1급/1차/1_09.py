# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
"""
계단 게임
https://www.notion.so/pdg0526/09-ca3636ad0b284ad4b32ed3cf315143a7
"""
def func(record): # input에 대해 이기는 output을 반환
	if record == 0: # 가위라면
		return 1 # 바위를 반환
	elif record == 1:# 바위라면
		return 2 # 보자기를 반환
	return 0 # 보자기라면 가위를 반환

# A가 몇 칸에 위치하는지..! 
def solution(recordA, recordB):
	cnt = 0
	for i in range(len(recordA)):
		if recordA[i] == recordB[i]:
			continue
		elif recordA[i] == func(recordB[i]):
			cnt = cnt + 3
		elif cnt > 0:
			cnt = cnt - 1
	return cnt

recordA = [2,0,0,0,0,0,1,1,0,0]
recordB = [0,0,0,0,2,2,0,2,2,2]
ret = solution(recordA, recordB)

print("solution 함수의 반환 값은", ret, "입니다.")