import time
start = time.time()

# https://school.programmers.co.kr/learn/courses/30/lessons/42578/solution_groups?language=python3
def solution(clothes):
    # 매일 다른 옷을 조합하여 입어 자신을 위장
    dict = {}
    # answer = 1
    answer = 1

    # 해쉬 테이블로 만들기
    for name, category in clothes:
        if category in dict:
            dict[category].append(name)
        else:
            dict[category] = [name]

    # 매일 다른 옷을 입는 경우의 수 계산
    for key in dict.keys():
        # 옷을 입지 않는 경우의 수도 계산
        answer *= len(dict[key]) + 1
    
    answer -= 1
    return answer


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
print("time :" , time.time() - start)


