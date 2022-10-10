import time
start = time.time()

# 10인분을 먹으면 음료수 하나를 서비스
# 양꼬치는 1인분에 12,000원
# 음료수는 2,000원

print(580000 - 580000 * 0.2)

def solution(n, k):
    service = n // 10
    return n * 12000 + (k - service) * 2000


print(solution(10, 3)) # 3
print(solution(64, 6)) # 3

print("time :", time.time() - start)