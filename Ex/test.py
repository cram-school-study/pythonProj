# 실패율을 구한후 정렬 시켜야한다
# 1. 분모를 구할것
# 2. 분자를 구할것
# 3. 실패율을 정렬한 후 반환할것

def solution(N, stages):
    try_people = []
    clear_people = []
    count = 0
    fail_rule = []

    stages.sort()
    print(stages)
    
    for i in range(N+2, 0, -1):
        if count == 0:
            try_people.append(stages.count(i-1))
            clear_people.append(stages.count(i))
        else:
            try_people.append(stages.count(i-1) + try_people[count-1])
            clear_people.append(stages.count(i) + clear_people[count-1])
        count = count + 1

    for i in range(1, N+1):
        fail_rule.append(1 - (clear_people[i]/try_people[i]))

    fail_rule.reverse()

    print(clear_people)
    print(try_people)
    print(fail_rule)
    print(fail_rule.index(min(fail_rule)))

    # fail_rule.index(max(fail_rule)) = -0.1

    print(fail_rule)
    # for i in N:
    #     min = 2
    #     for j in N:
    #         if fail_rule[j] < min: 
    #             min = fail_rule[j]

    
    answer = []
    return answer


solution(5,[2, 1, 2, 6, 2, 4, 3, 3])
# solution(4,[4,4,4,4,4])