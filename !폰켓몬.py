import time
start = time.time()

def solution(ls):
    return min(len(ls)/2, len(set(ls)))



# print(solution(2)) # 1
print(solution([3,1,2,3])) # 3
print(solution([3,3,3,2,2,4])) # 3
print(solution([3,3,3,2,2,2])) # 3

print("time :", time.time() - start)