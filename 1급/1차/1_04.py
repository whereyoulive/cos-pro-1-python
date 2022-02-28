# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

"""
타임머신
https://www.notion.so/pdg0526/04-f45ec9ebc2be40beb031c6c905d3ade7
"""
def solution(num):
	answer = 0
	answer = str(num + 1).replace('0', '1')
	return int(answer)
    
# ====================
num = 9949999
ret = solution(num)
 
print("solution 함수의 반환 값은", ret, "입니다.")