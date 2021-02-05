# 1)
# 3
# 125 15232 97
# -> 97

# 2)
# 7
# 137 460 603 40 521 128 125
# -> 137,128

def digit_sum(list):
    max = 0
    for i in range(len(list)):
        flag = int(list[i])
        temp = 0
        # while(True):
        #     if flag//10 != 0: 
        #         temp = temp + flag%10
        #         flag = flag%10
        #     else: break
        # if max < temp: max = temp
        
        # while(True):
        #     if flag != 0: 
        #         temp = temp + flag%10
        #         flag = flag//10
        #     else: break
        # if max < temp: max = temp

def fileopen(filename):
    file = open(filename)
    cnt = file.readline()
    b = file.readline().split(' ')
    print(digit_sum(b))

fileopen("D:/JWJ/PythonProj/Ex/자릿수합input1.txt")





# def digit_sum_by_teacher(num):
#     return sum(map(int,str(num)))


# f = open('D:/JWJ/PythonProj/Ex/자릿수합input2.txt', 'r')
# n = int(f.readline())
# a = list(map(int,f.readline().split()))
# max_val = 0
# lst = []
# final = 0

# for xx in a:
#     tot = digit_sum_by_teacher(xx)
#     if tot >= final:
#         # final=tot
#         # print(lst[i], end = ' ')

#     if tot > max_val:
#         max_val=tot
#         lst = []
#         lst.append(xx)
#     elif tot == max_val: lst.append(xx)
# f.close()        

# print(lst)

