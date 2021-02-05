# 두 개의 스트링 문자열을 받아 공통의 단어를 뽑아 내시오.
# 각 스트링의 단어는 컴마(,)로 구분을 한다. 

def select_common_by_jeong(first, second):
    result = []
    for i in set(first.replace(' ','').split(',')): 
        if second.find(i) != -1: result.append(i) 
    return sorted(result)

# 중복제거 1. set, 2. not in
# set 형식은 집합 형시이기때문에 교집합, 차집합을 사용하여 &,- 활용 가능

def select_common_by_teacher(first, second):
    aset, bset = set(first.replace(' ','').split(',')), set(second.replace(' ','').split(','))
    return ','.join(sorted(aset & bset))

        
print(select_common_by_teacher("one, two, three, six","two, five, six"))
print(select_common_by_teacher('Hello, World', 'The, World, is, very, beautiful'))
print(select_common_by_teacher('samsung, lg, lotte', 'doosan, sk, samsung, lotte'))