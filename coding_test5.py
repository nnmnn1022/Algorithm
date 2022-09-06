import re

s = "ababcdcdababcdcd"

def solution(s):
    str = list(s)
    str_list = []
    for i in range(len(str)) :
        for j in range(i) :
            tmp = []
            tmp.append(str.pop(0))

        print(str_list)
                

    answer = 0
    return answer

solution(s)