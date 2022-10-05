import time
start = time.time()
import re

def solution(S):
    li = S.split(' ')
    r = re.compile(r'[^a-zA-Z0-9]')
    # 유효하지 않은 문자열 걸러내기
    li = [w for w in li if not re.search(r, w)]
    answer = 0
    for w in li:
        lenw = len(w)
        # 문자 짝수개 && 숫자 홀수개
        if len(re.findall(r'[a-zA-Z]', w)) % 2 == 0 and len(re.findall(r'[0-9]', w)) % 2 == 1:
            if not  answer :
                answer = lenw
            elif answer < lenw: 
                answer = lenw
            
    if answer == 0:
        answer = -1
    return answer

print(solution("test 5 a0A pass007 ?xy1"))
print("time :", time.time() - start)
print(solution("t"))
print("time :", time.time() - start)
print(solution("test5a0Apass007?xy1"))
print("time :", time.time() - start)
