from collections import deque
import time
start = time.time()

# 일차선 다리를 정해진 순
# 모든 트럭이 다리를 건너려면 최소 몇 초
# 다리에는 트럭이 최대 bridge_length대
# weight 이하까지의 무게를 견딜

def solution(bridge_length, weight, truck_weights):
    time = 0 # 시간
    size = len(truck_weights) # 최초 대기 트럭 사이즈
    completed = [] # 다리를 지난 트럭
    in_bridge = deque([0 for _ in range(bridge_length)]) # 다리를 건너는 중인 트럭 | 0은 비어 있음을 의미
    truck_weights = deque(truck_weights) # 대기 트럭
    sum_bridge = 0 # sum을 대신하기 위한 in_bridge 원소들의 합
    
    # while(다리를 지난 트럭 사이즈 < 최초 대기 트럭 사이즈):
    while(len(completed) < size):
        time += 1
        tmp = in_bridge.popleft()
        
        # 조건에 맞으면 다리를 지난 것으로 처리
        if tmp != 0: # 조건 : tmp가 0이 아닐 때
            completed.append(tmp)
            sum_bridge -= tmp
        # 조건에 맞으면 다리를 건너는 중인 것으로 처리
        # 조건 : weight >= 현재 건너는 중인 트럭들의 무게 + 다음 트럭의 무게
        if truck_weights:
            if weight >= sum_bridge + truck_weights[0]:
                tmp2 = truck_weights.popleft()
                in_bridge.append(tmp2)
                sum_bridge += tmp2
            else:
                in_bridge.append(0)
    return time

print(solution(2	,10	, [4,5,7,6]))
print(solution(100	,100	,[10]))
print(solution(100	,100	,[10,10,10,10,10,10,10,10,10,10]))

print("time :" , time.time() - start)


# def solution(bridge_length, weight, truck_weights):
#     second = 0
#     completed = []
#     in_bridge = [0] * bridge_length
#     size = len(truck_weights)
#     while len(completed) < size:
#         second += 1
#         top = in_bridge.pop(0)
#         if top != 0:
#             completed.append(top)
#         if len(truck_weights) > 0: 
#             if sum(in_bridge) + truck_weights[0] <= weight:
#                 in_bridge.append(truck_weights.pop(0))
#             else:
#                 in_bridge.append(0)
#     return second