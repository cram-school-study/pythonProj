# *, ** 차이

# 1.
def lastName_and_FirstName1(*Names):
    for name in Names:
        print("%s %s" %  (name[0], name[1:3]), end=' ')
    print("\n")

lastName_and_FirstName1('이천수')
lastName_and_FirstName1('이천수', '안정환')

def lastName_and_FirstName2(*Names):
    for name in Names:
        print("%s %s" %  (name[0], name[1:3]), end=' ')
    print("\n")

lastName_and_FirstName2('이천수', '안정환')

# 2.
def introduceEnglishName1(**kwargs):
    for key, value in kwargs.items():
        print("{0} is {1}".format(key, value))

introduceEnglishName1(MyName = 'Chris!!')

def introduceEnglishName2(**kwargs):
    for key, value in kwargs.items():
        if 'ant' in kwargs.keys(): print("빠샤")
        else: print("{0} is {1}".format(key, value))

introduceEnglishName2(MyName = 'Chris!!')
introduceEnglishName2(ant = 'Chris!!')

# 3.
주인장이름 = "a"
블로그1 = "ㄱ"
블로그2 = "ㄴ"
블로그3 = "ㄷ"

def blog_printer1(*blogs):
    for post in blogs:
        print(post)

blog_printer1(블로그1, 블로그2, 블로그3)


# 에러!!!
# def blog_printer2(*name, blogs):
#     print(name)
#     for post in blogs:
#         print(post)

# blog_printer2(주인장이름, 블로그1, 블로그2, 블로그3)








# '''
# a : 설명
# b : 설명
# c : 설명

def cafe_store_board(Store_name, *Messages, **cafe_tag):
    '''
    Store_name : 카페이름
    Message : 오늘 알릴 사항
    fruit_tag : 메뉴 구성 및 가격표
    '''
    cnt = 50
    temp = (cnt - len(Store_name))//2

    print("*"*temp , Store_name, "*"*temp)
    for message in Messages:
        print(message)
    for menu, tag in cafe_tag.items():

        print(menu, "*" * (cnt-((len(menu)*2)+len(str(tag)+2))), tag)

    print("*****", Store_name, "*****\n")

cafe_store_board("카페", "메뉴판", 아메리카노=2000, 라떼=3500, 모카=8000, 아이스아메리카노=2500, 스콘=800)