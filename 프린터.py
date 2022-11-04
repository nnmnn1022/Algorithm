import time
start = time.time()

from collections import deque

# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.

# def solution(priorities, location):
#     if len(priorities) == 1: return 1
#     locations = deque(range(len(priorities)))
#     # 인쇄 대기목록 가장 앞에 있는 문서 꺼내기
#     _priorities = deque(priorities)
    
#     # 수 세기
#     i = 1

#     while(_priorities):
#         tmp = _priorities.popleft()
#         tmp_lo = locations.popleft()
#         if not _priorities :
#             return i

#         if tmp < max(_priorities):
#             _priorities.append(tmp)
#             locations.append(tmp_lo)

#         elif tmp_lo == location:
#             return i
#         else :
#             i += 1
#     return i


# 2022.11.04 복습 -- 재복습 요망
def solution(priorities, location):
    answer = 0
    location += 1
    while(len(priorities) >= 1):
        # J 꺼내기
        j = priorities.pop(0)
        location = location - 1 if location > 0 else len(priorities)

        # 우선순위가 더 높은 것이 있는지 확인하고 있으면 마지막에 넣기
        # 그렇지 않으면 인쇄하기
        if priorities:
            if max(priorities) > j:
                priorities.append(j)
            else:
                answer += 1
                if location == 0:
                    return answer
        else :
            return answer + 1

    return answer


# print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
# print(solution([1, 1, 9, 1, 1, 1], 5))
print("time :" , time.time() - start)


