# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
"""
주식으로 최대 수익을 내세요
https://www.notion.so/pdg0526/10-9330f5fdc5804aaea90a7f3d77e861d1
"""
def solution(prices):
	INF = 1000000001
	tmp = INF
	answer = -INF
	for price in prices:
		if tmp != INF:
			answer = max(answer, price- tmp)
		tmp = min(tmp, price)
	return answer

prices1 = [1, 2, 3]
ret1 = solution(prices1)

print("solution 함수의 반환 값은", ret1, "입니다.")
    
prices2 = [3, 1]
ret2 = solution(prices2)

print("solution 함수의 반환 값은", ret2, "입니다.")