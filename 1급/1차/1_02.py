"""
해밍거리 구하기
https://www.notion.so/pdg0526/02-c2ed33643685469ab6bd2cfdec0f9ff8
"""

# [길이가 큰 문자열의 길이 - 길이가 큰 문자열의 길이] 만큼	문자열 앞에 '0'을 붙여서 반환
def func_a(string, length):
	padZero = ""
	padSize = length - len(string)
	for i in range(padSize):
		padZero += "0"
	return padZero + string

# ===================================
def solution(binaryA, binaryB):
	# 두 문자열 중 문자열의 길이가 문자열의 길이 계산
	max_length = max(len(binaryA), len(binaryB))

	# 자릿수를 맞춘 두 문자열 생성
	binaryA = func_a(binaryA, max_length)
	binaryB = func_a(binaryB, max_length)

# 두 문자열의 각 문자가 다르면 해밍거리 += 1
	hamming_distance = 0
	for i in range(max_length):
		if binaryA[i] != binaryB[i]: # 두 문자열의 각 문자가 다르면 해밍거리 += 1
			hamming_distance += 1  
	return hamming_distance
    
# ===================================
binaryA = "10010"
binaryB = "110"
ret = solution(binaryA, binaryB)

print("solution 함수의 반환 값은", ret, "입니다.")