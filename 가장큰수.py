import re
import time
start = time.time()
def solution(numbers):

    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)

    # 
    return str(int(''.join(numbers)))


print(solution([6, 10, 2,0,0,0,0]))
print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([3, 30, 12, 5, 0]))
print(solution([3, 303, 340, 39, 339])) # 39 340 339 3 303

print("time :" , time.time() - start)