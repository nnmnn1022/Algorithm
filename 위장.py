from operator import mul


def solution(clothes):
    # 매일 다른 옷을 조합하여 입어 자신을 위장
    dict = {}
    for name, category in clothes:
        if category in dict:
            dict[category] += (name, )
        else:
            dict[category] = (name, )

    len_dict = [len(dict[d]) for d in dict]
    if len(len_dict) < 2 :
        multi = 0
    else : multi = 1

    for i in len_dict:
        multi *= i

    return sum(len_dict) + multi

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))


