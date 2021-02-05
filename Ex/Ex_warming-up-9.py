# 로또번호 추출기 1~45 6개, 중복은 안됨
import random

def lotter_number_maker_by_jeong():
    result = []
    while(True):
        result.append(random.randint(1,45))
        if len(set(result)) == 6:
            return sorted(set(result))

def lotter_number_maker_by_teacher():
    return sorted(random.sample(range(1,46),6))



print(lotter_number_maker_by_teacher())