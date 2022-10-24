import time
start = time.time()
from collections import Counter

def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)

    return list(p-c)[0]


# print(solution(2)) # 1
print(solution(["leo", "kiki", "eden"],["eden", "kiki"])) # 	"leo"
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"])) # 	"vinko"
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])) # "mislav"

print("time :", time.time() - start)