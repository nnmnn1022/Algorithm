def solution(N, stages):
    answer = []
    fail_percentage = {}

    # 각 스테이지 인원 체크
    on_stages = sorted(set(stages))
    dict = {i:stages.count(i) for i in on_stages}

    # 해당 스테이지 이상에 속한 인원들을 분모 삼음
    for i in dict.keys() :
        fail = dict[i]
        dict[i] = 0
        if sum(dict.values()) > 0:
            fail_percentage[i] = fail / sum(dict.values())
        else : # on_stages의 마지막 숫자가 N+1일 때 처리
            if fail_percentage[i] = fail / fail + dict[N+1]


    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))