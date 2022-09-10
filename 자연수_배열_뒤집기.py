import math

def solution(n):
    return [int(s) for s in str(n)][::-1]
    # list(map(int, reversed(str(n))))

number = 12345

print(solution(number))