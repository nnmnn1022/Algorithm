import time
start = time.time()

# 0과 1로 시작하는 피보나치 수

def solution(n):
    dp = [0 for _ in range(n+1)]
    if n >= 1:
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]

    return dp[-1]

print(solution(5)) # 55
print(solution(10)) # 55
print(solution(16)) # 987
print(solution(17)) # 1597
print(solution(18)) # 2584
print(solution(90)) # 2584
print("time :", time.time() - start)