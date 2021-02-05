# monkey_typing(data, words)함수를 만드시오.
# 원숭이가 마구 컴퓨터 자판을 두드린다.
# 호출 함수의 인자는 첫번째는 스트링, 두번째는 소문자 단어 set으로 넘어간다.
# 몇개의 단어가 의미가 있었는지 확인한다.

def monkey_typing_by_jeong(data, words):
    count = 0
    for i in words: 
        if data.find(i) != -1: count += 1
    return count

def monkey_typing_by_teacher1(data, words):
    count = 0
    for i in words: 
        if i in data: count += 1
    return count

def monkey_typing_by_teacher2(data, words):
    return len([xx for xx in words if xx in data])


#3 단어 찾기
def monkey_typing_by_teacher3(data, words):
    return len([xx for xx in words if xx in data])

print(monkey_typing_by_teacher2('how aregojdoijgodijosjgd you idjfojs idol', {'how', 'are', 'you', 'hello'}))
print(monkey_typing_by_teacher2('gojiojgappleorangeojiogjoyoujiidolfdboyol', {'boy', 'idol', 'orange', 'apple'}))
print(monkey_typing_by_teacher2('dgjajosjhgolfnnlkbaseballanngmsgoodbat', {'baseball', 'golf', 'orange', 'bat'}))