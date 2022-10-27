from collections import deque
from itertools import permutations
import time
start = time.time()

# 유저가 탐험할수 있는 최대 던전 수

def solution(k, dungeons):
    # 순열을 모두 찾아 리스트화
    permu = deque(permutations(dungeons, len(dungeons)))
    answer = 0
    n = 0

    # 순열 리스트를 모두 순회하는 코드
    # permu에 원소가 있을 때,
    while permu:
        if n > answer : answer = n
        if answer == len(dungeons) : return answer
        n = 0
        # pop하기
        tmp = permu.popleft()
        tmp_k = k
        
        # pop한 내용들을 확인했 때 던전을 몇 번 돌 수 있는지 확인
        for p in tmp:
            if tmp_k >= p[0]:
                tmp_k -= p[1]
                n += 1
    
    return answer


# print(solution(2)) # 1
print(solution(80, [[80,20],[50,40],[30,10]])) # 3


print("time :", time.time() - start)