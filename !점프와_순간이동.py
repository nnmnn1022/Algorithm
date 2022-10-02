import math

def solution(n):
    # 한 번에 K 칸을 앞으로 점프
    # (현재까지 온 거리) x 2 에 해당하는 위치로 순간이동
    # 순간이동을 하면 건전지 사용량이 줄지 않지만, 앞으로 K 칸을 점프하면 K 만큼의 건전지 사용량
    d = 1
    while(1 < n):
        if n % 2 == 1:
            d += 1
        n = n // 2
        # print(n)

    return d

    # return bin(n).count('1')

print(solution(5))
print(solution(6))
print(solution(5000))


