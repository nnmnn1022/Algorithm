import math

def solution(n):
    answer = -1
    if (math.sqrt(n).is_integer()):
        answer = (math.sqrt(n)+1) * (math.sqrt(n)+1)
    return int(answer)


number = 3

print(solution(number))