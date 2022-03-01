"""
체스의 나이트
https://www.notion.so/pdg0526/06-c1d67ebbd6794b08894cbcd11ca5929f
"""

def solution(pos):
    answer = 0
    # 파라미터를 좌표상에 표현
    x_place = {}
    y_place = {}
    
    for i in range(8):
        x_place[chr(ord('A') + i)] = i
        y_place[str(i)] = i
    
    x = x_place[pos[0]]
    y = y_place[pos[1]]


    # case 1: 세로 +1
    if y + 1 <= 8:

        if x + 2 <= 8: # 체스 판의 오른쪽
            answer += 1
        if x - 2 >= 0: # 체스 판의 왼쪽
            answer += 1

    # case 2: 세로 +2
    if y + 2 <= 8:
        if x + 1 <= 8: # 체스 판의 오른쪽
            answer += 1   
        if x - 1 >= 0: # 체스 판의 왼쪽
            answer += 1

    # case 3: 세로 -1
    if y - 1 >= 0:
        if x + 2 <= 8: # 체스 판의 오른쪽
            answer += 1
        if x - 2 >= 0: # 체스 판의 왼쪽
            answer += 1
            
    # case 4: 세로 -2
    if y - 2 >= 0:
        if x + 1 <= 8: # 체스 판의 오른쪽
            answer += 1
        if x - 1 >= 0: # 체스 판의 왼쪽
            answer += 1

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# def solution(pos):
#     answer = 0
#     x = ord(pos[0]) - ord('A')  # 0 ~7
#     y = ord(pos[1]) - ord('1')  # 0 ~7

#     dx = [2, 2, 1, 1, -1, -1, -2, -2]
#     dy = [1, -1, 2, -2, 2, -2, 1, -1]

#     for i in range(8):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx >= 0 and nx <= 7 and ny >= 0 and ny <= 7:
#             answer += 1
# =================================

    return answer
pos = "A7"
ret = solution(pos)

print("solution 함수의 반환 값은", ret, "입니다.")


