from collections import deque
import time
start = time.time()

# arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거

def solution(arr):
    # arr deque로
    arr = deque(arr)
    # 연속되지 않은 숫자만 넣을 배열
    a = []

    # for 문 돌려서 arr[i]가 arr[i+1]과 같을 때
    for _ in range(len(arr)):
        a.append(arr.popleft())
        if arr and a[-1] == arr[0]:
            a.pop()

    return a



# print(solution(2)) # 1
print(solution([1,1,3,3,0,1,1])) # [1,3,0,1]
print(solution([4,4,4,3,3])) # [4,3]

print("time :", time.time() - start)