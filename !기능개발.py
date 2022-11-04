from collections import deque
import time
start = time.time()

# def solution(progresses, speeds):
#     progresses = deque(progresses)
#     speeds = deque(speeds)
#     answer = []
#     i = 0
#     now = 0
#     # progresses[0]이 몇 일 후에 100 이상이 되는지 확인해서 그 날짜 뒤에 100이 넘는 숫자들을 하나씩 pop 하고 100 미만은 break
#     # for i in range(len(progresses)) 시작
#     while progresses:
#         # 남은 진행율이 있으면 1 추가
#         if (100 - progresses[0]) % speeds[0] > 0:
#             i = (100 - progresses[0]) // speeds[0] + 1
#         else :
#             i = (100 - progresses[0]) // speeds[0]

#         for _ in range(len(progresses)):
#             if progresses[0] + speeds[0]*i >= 100:
#                 now += 1
#                 progresses.popleft()
#                 speeds.popleft()
#             else:
#                 answer.append(now)
#                 now = 0
#                 break
#     answer.append(now)

#     return answer


# def solution(progresses, speeds):
#     print(progresses)
#     print(speeds)
#     answer = []
#     time = 0
#     count = 0
#     while len(progresses)> 0:
#         if (progresses[0] + time*speeds[0]) >= 100:
#             progresses.pop(0)
#             speeds.pop(0)
#             count += 1
#         else:
#             if count > 0:
#                 answer.append(count)
#                 count = 0
#             time += 1
#     answer.append(count)
#     return answer


# 2022.11.04 복습
def solution(progresses, speeds):
    day = 0
    publish_num = 0
    answer = []
    # 가장 먼저 배포되어야 하는 프로젝트가 100%가 되었을 때
    # publish가 몇 개 되는지 확인해서 answer에 push

    for i in range(len(progresses)):
        
        if publish_num == 0:
            day = -((progresses[i] - 100) // speeds[i])
            publish_num += 1

        elif progresses[i] + day*speeds[i] >= 100:
            publish_num += 1

        else:
            answer.append(publish_num)
            day = -((progresses[i] - 100) // speeds[i])
            publish_num = 1

    answer.append(publish_num)

    return answer

# print(solution(2)) # 1
print(solution([93, 30, 55], [1, 30, 5])) # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])) # [1, 3, 2]

print("time :", time.time() - start)