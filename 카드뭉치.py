# 원하는 카드 뭉치에서 카드를 순서대로 한 장씩 사용합니다.
# 한 번 사용한 카드는 다시 사용할 수 없습니다.
# 카드를 사용하지 않고 다음 카드로 넘어갈 수 없습니다.
# 기존에 주어진 카드 뭉치의 단어 순서는 바꿀 수 없습니다.

def solution(cards1, cards2, goal):
    for g in goal:
        if cards1 and cards1[0] == g:
            cards1.pop(0)
        
        elif cards2 and cards2[0] == g:
            cards2.pop(0)
        else:
            return 'No'

    return 'Yes'

print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))