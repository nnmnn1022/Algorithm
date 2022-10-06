import time
start = time.time()

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 1보다 크거나 같고, 10**6보다 작거나 같은 정수 N

def solution(n):
    dp = [0 for _ in range(n+1)]
    for i in range(2, n+1):
        dp[i] = dp[i-1]+1
        if i % 3 == 0:
            dp[i] = min(dp[i//3]+1, dp[i])
        elif i % 2 == 0:
            dp[i] = min(dp[i//2]+1, dp[i])

    return dp[n]



# print(solution(2)) # 1
print(solution(1000)) # 3

print("time :", time.time() - start)