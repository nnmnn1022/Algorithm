import math

def solution(n):
    answer = 1
    if n % sum(map(int, str(n))) != 0 :
        answer = 0
    return bool(answer)

number = 10
print(solution(number))
number = 12
print(solution(number))
number = 11
print(solution(number))
number = 13
print(solution(number))

