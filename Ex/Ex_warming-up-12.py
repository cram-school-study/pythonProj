# 마방진 - 홀수 x 홀수, 홀수 - 3이상
# 가로, 세로 , 대각선이 같은 매트릭스
# 짝수 해봐라~~


import numpy as np
n = int(input("n*n 마방진을 위한 n값을 입력(3이상, 홀수만)="))
matrix = np.zeros((n,n), dtype=int)

s_row=0; s_col=n//2
matrix[s_row, s_col] = 1
row=0; col=0

for i in range(2, n*n+1):
    row = s_row # 전 위치갑 row값 보관
    col = s_col # 전 위치값 col값 보관
    s_row = s_row - 1
    s_col = s_col + 1

    if s_row < 0 :
        s_row = n - 1
    if s_col > n-1:
        s_col = 0

    if matrix[s_row, s_col] == 0:
        matrix[s_row, s_col] == i
    else: # 0이 아니면 다른 숫자 있다는 이야기
        s_row = row + 1
        matrix[s_row, s_col] = i
print(matrix)

# def dd(index):
#     a[index][index] = [][]
#     for i in range(1,index):
#         print(i)

# dd(3)