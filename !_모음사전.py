from collections import deque
from itertools import permutations, product
import time
start = time.time()

# 이 단어가 사전에서 몇 번째 단어

def solution(word):
    a = ["".join(list(j)) for i in range(1, 6) for j in product(["A", "E", "I", "O", "U"], repeat=i)]    
    a.sort()
    return a.index(word)+1


# print(solution("AAAAE")) # 6
# print(solution("AAAE")) # 10
# print(solution("I")) # 1563
# print(solution("EIO")) # 1189
print(solution("UUUUU")) # 1189


print("time :", time.time() - start)