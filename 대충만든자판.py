# 자판 하나에 여러 개의 키가 할당됨
# 1~100 까지 할당 가능
# 같은문자가 다른 자판에 여러 번 할당되었을 수 있음
# 키 하나가 한 자판에 여러 번 할당 되었을 수 있음
# 아예 할당되지 않았을 수 있음

# 할당된 키 모음을 가지고 있는 dict 필요
# key : 알파벳
# value : 할당된 키에 대한 최소 접근 값

def solution(keymap:list, targets:list):
    best_way = {}
    # A~Z
    for a in range(65, 91):
        for i, j in enumerate(keymap):
            key = chr(a)
            # dict에 key가 있는 경우
            value = best_way.get(key)
            new_value = j.find(key) + 1 if j.find(key) > -1 else -1
            if value:
                # 이전 값이 -1이고 현재 값이 -1 보다 크면 넣기
                if value == -1 and new_value > -1: best_way[key] = new_value
                # 이전 값이 -1이 아니고, 현재 값도 -1이 아닐 때 비교해서 작은 값 넣기
                elif value > new_value > -1: best_way[key] = new_value
            # dict에 key가 없는 경우 - 무조건 넣기
            else: 
                best_way[key] = new_value

    answer = []

    for target in targets:
        sum = 0
        for key in target:
            value = best_way.get(key)
            if value == -1:
                sum = -1
                break
            else:
                sum += value
        answer.append(sum)

    return answer

# ["ABACD", "BCEFD"]	["ABCD","AABB"]	[9, 4]
# ["AA"]	["B"]	[-1]
# ["AGZ", "BSSS"]	["ASA","BGZ"]	[4, 6]

print(solution(["ABACD", "BCEFD"],	["ABCD","AABB"]))
print(solution(["AA"],	["B"]))
print(solution(["AGZ", "BSSS"],	["ASA","BGZ"]))