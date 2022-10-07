import heapq
import time
start = time.time()

# 모든 음식의 스코빌 지수를 K 이상
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다
# 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K
# scoville의 길이는 2 이상 1,000,000 이하입니다.
# K는 0 이상 1,000,000,000 이하입니다.
# scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

def solution(scoville, K):
    # 최소힙
    heapq.heapify(scoville)

    i = 0
    # scoville에 값이 있고, scoville의 최솟값이 K보다 작은 동안
    while len(scoville) >= 2 and scoville[0] < K:
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2)
        i += 1
    
    return -1 if scoville[0] < K else i


print(solution([1,2,3], 11)) # 2
print(solution([5, 2, 3, 15, 5, 12], 12)) # 2
print(solution([0,0,0,0,0,0], 12)) # 2

print("time :", time.time() - start)