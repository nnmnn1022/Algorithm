import time
start = time.time()

from collections import deque

def solution(my_str, n):
    tmp = ""
    answer = []
    # my_str을 순회하면서 n번째가 되면 append
    for i in range(len(my_str)):
        if i // n > 0 and i % n == 0:
            answer.append(tmp)
            tmp = ""
        tmp += my_str[i]
    
    if tmp != "":
        answer.append(tmp)

    return answer


# print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
# print(solution([1, 1, 9, 1, 1, 1], 5))
print("time :" , time.time() - start)


