# 격자판 최대합
# 가로, 세로, 대각선의 1줄 다 더하기의 최대값 구하기

# a = [list(map(int,f.readline().splirt())) for _ in range(n)]


def fileopen(filename):
    file = open(filename)
    cnt = int(file.readline())
    list1 = []
    for i in range(cnt):
        line = file.readline()[:-2].replace('\n', '').split(' ')
        list1.append(line)

    max1 = []

    max_value3, max_value4 = 0, 0 # 왼위오아 대각선, 왼아오위 대각선
    for i in range(cnt):
        max_value1, max_value2 = 0, 0 # 가로합, 세로합
        for j in range(cnt):            
            max_value1 = max_value1 + int(list1[i][j])
            max_value2 = max_value2 + int(list1[j][i])
            if i == j:
                max_value3 = max_value3 + int(list1[j][j])
            print(max_value1)
        max_value4 = max_value4 + int(list1[i][cnt-1-i])
        max1.append(max_value1)
        max1.append(max_value2)

    max1.append(max_value3)
    max1.append(max_value4)

    print(max(max1))

fileopen("D:/JWJ/PythonProj/Ex/격자판최대합1.txt")