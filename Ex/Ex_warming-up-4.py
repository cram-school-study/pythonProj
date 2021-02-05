# Camel 형태의 문자열을 Snake 형으로 문자열을 변경하세요.
# to_snake_case(text) 함수를 만들고 camel형의 문자열을 들어오면 snake형으로 변경한다
# 입력 예 'MyFunction_Name'
# 출력 예 to_snake_case('MyFunctionName') 호출하면 'my_function_name'로 출력


# 대소문자 차이 32

def to_snake_case(data):
    for i in data:
        if i.isupper():
            data=data.replace(i, '_'+i.lower())
    return data.strip('_')

def to_camel_case(data):
    return data.title().replace("_","")

test = 'MyFunctionName'
print(to_snake_case(test))
print(to_camel_case(to_snake_case(test)))