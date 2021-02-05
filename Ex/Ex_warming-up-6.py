import re
# testing_anagram(fword, sword) 함수를 만드시오.
# 애너그램 게임 - 스펠링 갯수를 모두 조합을 시켜 동일한 스펠링의 갯수를 갖는 단어/단어열

# 띄어쓰기 구분
def testing_anagram1(data1, data2):
    return sorted(data1.upper().replace(' ','')) == sorted(data2.upper().replace(' ',''))

# 특수문자 전부 구분
def testing_anagram2(data1, data2):
    print(re.sub('[-=.#\?:$}] ', '', data1.upper()))
    #return sorted(re.sub('[-=.#\?:$}]', '', data1.upper())) == sorted(re.sub('[[-=.#\?:$}]', '' , data2.upper()))

print(testing_anagram2('listen', 'silent'))
print(testing_anagram2('Programming', 'Gram Ring Mop'))
print(testing_anagram2('Dirty room', 'Dorm # # % ^itory'))
print(testing_anagram2('toy', 'yoi'))