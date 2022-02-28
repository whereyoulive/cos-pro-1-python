# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

"""
https://pdg0526.notion.site/05-52157d55ae01453bacb00719730e9ce5
소용돌이 수/ 달팽이 수
"""

def solution(n):
    answer = 0
    # n x n 배열 생성 (0으로 초기화)
    arr = [[0 for _ in range(n)] for _ in range(n)]

    row = 0 # 행 
    col = -1 # 열
    trans = 1 # 행, 열 index 증감 설정 변수
    cnt = 1 #  원소 값

    while n > 0:
        for _ in range(n):
            col += trans
            arr[row][col] = cnt
            cnt += 1
        n -= 1

        for _ in range(n):
            row += trans
            arr[row][col] = cnt
            cnt += 1
        trans *= -1 # 증감방향 전환

    for i in range(len(arr)):
        answer += arr[i][i]

    return answer

# ======================
n1 = 3
ret1 = solution(n1)

print("solution 함수의 반환 값은", ret1, "입니다.")
    
n2 = 2
ret2 = solution(n2)

print("solution 함수의 반환 값은", ret2, "입니다.")
