# 회의실 문제
# 회의실을 겹치지않게 최대한 회의할수 있게 
def aaaa():
    metting = []
    for i in range(n):
        st, et = map(int, f.readline().split())
        meeting.append((st,et))

        cnt =0
        et =0
        for s,e in metting:
            if s>= et:
                et = e
                cnt +=1

        print(cnt)



def fileopen(filename):
    file = open(filename)
    cnt = file.readline()
    list1 = []
    for i in range(int(cnt)):
        line = file.readline().replace('\n','').split(' ')
        list1.append(tuple(line))
    
    sort_list1 = sorted(list1, key = lambda x : (x[1],x[0]))
    
    start = sort_list1[0]
    del sort_list1[0]
    for i in 
    sort_list1.


fileopen("D:/JWJ/PythonProj/Ex/회의실in1.txt")