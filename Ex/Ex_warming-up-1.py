# 리스트의 중간 값 구하기
## 리스트의 길이가 짝수일 경우 중간의 값, 중간의 값+1을 더한 후 평균 추출
## 리스트의 길이가 홀수일 경우 중간의 값 추출

# 1. data 리스트 자체를 정렬 하는것
# data.sort()
# 2. data 리스트 리턴 값만 정렬해서 보내는 것
# sorted.data
# 3. sort 함수의 리턴값을 받는것 이므로 None 타입이 반환된다.
# data.sort

def get_median(data):
    data1 = data.sort()
    data2 = sorted.data
    data3 = data.sort
    center_index = len(data) // 2
    if len(data) % 2 == 1:
        return data[center_index]
    else:
        return (data[center_index]+data[-center_index-1])/2

list1 = [6,5,4,3,2,1]
list2 =[5,4,3,2,1]

get_median(list1)