# 10자 이상, 최소 한 대문자, 숫자 한개는 반드시 포함하는 조합으로 패스워드를 만들어 이 조건을 만족하면 True 그렇지않으면 False를 출력하는 함수를 만드시오
# 위의 조건을 만족하는 함수를 만들었다면 이제는 특수문자를 반드시 포함하는 함수 is_realgoodpw(ata)로 확장해보시오

def is_goodpw_by_jeong(data):
    if not len_check(data): return False
    if not upper_check(data): return False
    if not lower_check(data): return False
    return True

# 길이 체크
def len_check(data):
    if len(data) >= 10: return True
    return False

# 대문자 체크
def upper_check(data):
    for i in data:
        if ord('A') > ord(i) or ord('Z') < ord(i):
            return False
    return True

#소문자 체크
def lower_check(data):
    for i in data:
        if ord('a') > ord(i) or ord('z') < ord(i):
            return False
    return True


def is_goodpw_by_teacher(data):
    if len(data) < 10: return False
    if data.upper() == data: return False
    if data.lower() == data: return False
    return any(xx.isdigit() for xx in data)

def is_realgoodpw_by_teacher(data):
    if len(data) < 10 : return False
    if data.upper() == data: return False
    if data.lower() == data: return False
    if any( xx in ['!','@','#','$','%','^','&','*','(',')','_','-','+','=','\\','|'] for xx in data):
        return ant(xx.isdigit() for xx in data)
    else: return False

