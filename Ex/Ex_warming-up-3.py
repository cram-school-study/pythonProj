# 제일 많은 요소를 추출하는 함수

# 1)
# set으로 중복제거
# count를 하나 지정
# 반복문으로 돌리면서 max값 저장 후 계속 비교 및 index값 저장 -> 저장해야할 값 max값, index값
# 반복문 다 돌고 리스트에서 해당 인덱스로 해서 값 리턴

# 2)
# set으로 중복제거
# 리스트 1개 지정, index값 한개 지정
# 반복문으로 돌리면서 해당 [max값, value값] 저장, index값 저장
# 반복문 다 돌고 리스트에서 해당 인덱스로 해서 값 리턴

def most_frequent(data):
    max = 0
    value = ""
    for i in set(data):
        if max < data.count(i):
            max = data.count(i)
            value = i
    return value
    
data = ['apple','samsung','apple','lg','lotte']
print("결과",most_frequent(data))
