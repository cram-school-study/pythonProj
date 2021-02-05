# fix_sentence(text) 함수를 만들고 문장의 첫글자는 대문자로 마침표가 없을떄는 
# 마침표를 추가하여 text return 하는 함수를 만드세요
# 입력 예) sample_sentence = 'hello, everybody'
# 출력 예) fix_sentence(sample_sentence) 호출하면 'Hello, everybody.'출력

# endswith
# capitalize

def fix_sentence(data):
    if not data.endswith('.'):
        data = data + '.'
        return data.capitalize()
    
test = 'hello, everybody'
print(fix_sentence(test))
