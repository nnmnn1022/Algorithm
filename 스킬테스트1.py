def solution(x, n):
    if x == 0:
        return list('0'*n)
    elif x < 0 :
        return list(range(x, x*n-1, x))
    else :
        return list(range(x, x*n+1, x))

print(solution(0,5))
# print(solution(2,5))
# print(solution(4,3))
# print(solution(-4,2))

