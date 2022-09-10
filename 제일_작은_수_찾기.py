
from os import remove


def solution(arr):
    d = sorted(arr)[0]
    if len(arr) > 1 :
        arr.remove(d)
        return arr
    else :
        return [-1]

arr = [4,3,2,1]
print(solution(arr))


