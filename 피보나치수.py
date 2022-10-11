import time
start = time.time()

# 0과 1로 시작하는 피보나치 수

def solution(n):
    if n == 0: return 0
    dp = [0]*(n+1)
    dp[1] = 1

    for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

    return dp[i] % 1234567

print(solution(0)) # 2
print(solution(3)) # 2
print(solution(12)) # 2
print(solution(5)) # 5


print("time :", time.time() - start)