import time
start = time.time()

def solution(A):
    dic = {}
    for a in A:
        if dic[a]:
            dic[a] += 1
        else :
            dic[a] = 1

    for a in A:
        if dic[a] == 1:
            return a

    return -1

        
    


print(solution([4,10,5,4,2,10]))
print(solution([1,4,3,3,1,2]))
print(solution([99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,66,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999,99999,88888,88888,7777,7777,99999]))
print("time :", time.time() - start)

