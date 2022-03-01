# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

"""
계산기 by 문자열
https://www.notion.so/pdg0526/03-by-3d5be374fb874c91b403bfe9f27a5a30
"""

# 앞의 수와 뒤의 수를 연산기호에 해당하는 연산을 하여 반환
def func_a(numA, numB, exp):
	if exp == '+':
		return numA + numB
	elif exp == '-':
		return numA - numB
	elif exp == '*':
		return numA * numB

# 문자열 중 연산기호에 해당하는 index 반환
def func_b(exp):
	for index, value in enumerate(exp):
		if value == '+' or value == '-' or value == '*':
			return index

# 연산기호 기준으로 앞의 수와 뒤의 수 반환 
def func_c(exp, idx):
	numA = int(exp[:idx])
	numB = int(exp[idx + 1:])
	return numA, numB

def solution(expression):
	exp_index = func_b(expression) 
	first_num, second_num = func_c(expression, exp_index) 
	result = func_a(first_num, second_num, expression[exp_index]) 
	return result
    
expression = "123+12"
ret = solution(expression)

print("solution 함수의 반환 값은", ret, "입니다.")