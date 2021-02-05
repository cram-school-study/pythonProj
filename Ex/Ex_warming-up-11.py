# 피클 알아보기
# 파이썬 _ 변수
# 피클
# random.seed
# 마방진 만들기 - 인덱스 문제

f = open("C:/Users/JWJ/Desktop/바탕화면/수업파일/실습데이터/사과나무in1.txt", "r")
n = int(f.readline())
a = [list(map(int, f.readline().split())) for _ in range(n)]

def diamond_by_jeong():
    toggle = True
    index = len(a)//2
    cnt, sum = 1, 0
    for i in range(len(a)):
        loop = 0
        for j in range(0,cnt):
            sum = sum + a[i][index-(abs(loop))] + a[i][index+(abs(loop))]
            loop += 1
            print(cnt)
        sum = sum - a[i][index]
        if cnt == index: toggle = not toggle
        if toggle: cnt += 1
        else: cnt -= 1
    return sum

print(diamond_by_jeong())



def diamond_by_teacher():
    for i in range(n):
        for j in range(s,e+1):
            sum+= a[i][j]
        if i < n//2 :
            s=s-1; e=e+1
        else:
            s=s+1; e=e-1


# def N_Matirx(n):
#     import random
#     random.seed(0)
#     return [[random.randint(i,n*n) for i in range(n)] for j in range(n)]

# X=3
# m1 = N_Matirx(X)
# for i in range(X):
#     print(m1[i])



