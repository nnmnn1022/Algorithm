import time
start = time.time()

# 카테고리 1 : 이름 3
# 카테고리 2 : 이름 2
# 5 + 6 = 11
# 카테고리 1 : 이름 3
# 카테고리 2 : 이름 2
# 카테고리 3 : 이름 4
# 전체개수(9) + 1,2(6) + 2,3(8) + 1,2,3(24) = 47


def solution(clothes):
    # 매일 다른 옷을 조합하여 입어 자신을 위장
    dict = {}
    # 옷을 하나만 입는 경우의 수
    len_name = 0

    for name, category in clothes:
        len_name += 1
        if category in dict:
            dict[category].append(name)
        else:
            dict[category] = [name]

    len_categories_li = [len(d) for d in dict]
    len_category = len(dict)
    tmp = 0

    # range(1, 카테고리 수+1) 을 순회하며 입을 옷 개수를 선택
    # i 개 입는 경우를 의미
    for i in range(2, len_category+1):
        # tmp = for i in (1, 카테고리 수+1) 를 순회하며  += len(카테고리[i-1]) * len(카테고리[i])
        for j in range(len_category):
            tmp += len_categories_li[j-1] * len_categories_li[j]

    # 옷을 하나만 입는 경우의 수 + tmp(옷을 i개 입는 경우의 수)
    pass

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
print("time :" + time.time() - start)


