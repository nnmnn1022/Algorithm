import math

def solution(n):
    return int(''.join(reversed(sorted(str(n)))))

number = 118372

print(solution(number))