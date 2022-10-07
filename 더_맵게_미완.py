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
    min_heap = scoville[:]
    # 최소 힙
    heapq.heapify(scoville)

    # 최소, 차소 값 
    min_1 = 0
    min_2 = 0

    # 섞기
    for i in range(len(scoville)//2):
        min_1 = min_heap[0]
        min_2 = min_heap[1]

        if min_2 == 0: return -1

        # 최소 값이 K 보다 크거나 같으면 break
        if min_1 >= K:
            break
        else :
            heapq.heappush(min_heap, heapq.heappop(min_heap) + heapq.heappop(min_heap)*2)

    return i






print(solution([1, 2, 3, 9, 10, 12], 7)) # 2

print("time :", time.time() - start)