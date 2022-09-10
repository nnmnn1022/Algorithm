
def solution(n):
    answer = 0
    for i in range(0, 501):
        if n == 1 : 
            return i
        elif not (n % 2) : n = int(n / 2)
        else : n = n * 3 + 1

    if not (n == 1) :
        answer = -1

    return answer

number = 626331
print(solution(number))


