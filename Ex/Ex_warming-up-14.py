# 정다면체 확률
# 4, 6, 8, 12, 20 중 하나
# 확률 동일시에는 오름차순 차례대로 출력

def baaaam_by_jeong():
    n = int(input("n 입력!!"))
    m = int(input("m 입력!!"))

    cnt = 0
    toggle = True
    list =[]
    if m>n: cnt = m-n+1
    else: 
        cnt = n-m+1
        toggle=False
    
    for i in range(cnt):
        if toggle: list.append(str(n+i+1))
        else: list.append(str(m+i+1))

    print(' '.join(list))



def baaaam_by_teacher():
    n,m = map(int, input("n,m을 컴마로 구분해서 입력하세요").split(','))

    for i in range(1, n+1):
        for j in range(1, m+1):
            index=i+j
            cnt[index]+=1

    for i in range(n+m+1):
        if cnt[i]>max_val:
            max_val = cnt[i]

    for i in range(n+m+1):
        if cnt[i] == max_val:
            print(i, end=' ')

def mn_dice(n,m):
    if n<m:
        return [xx for xx in range(n+1, m+2)]
    else:
        return [xx for xx in range(m+1, n+2)]


def solution(n, m):
    if n <= m :
        return list(range(n+1, m+2))
    elif m < n:
        return list(range(m+1, n+2))