def solution(n, m):
    answer = []
    # 최대공약수
    GCD = 0
    # 최소공배수
    LCM = 0

    a , b = n, m

    while(b != 0):
        r = a % b
        a = b
        b = r
    GCD = a

    # 두 수 a와 b의 최소공배수는 a와 b의 곱을 a와 b의 최대공약수를 나눈 것과 같다.
    LCM = n * m // GCD 

    return [GCD, LCM]

print(solution(3, 12))
print(solution(2, 5))