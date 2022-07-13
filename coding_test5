# 부터 45까지의 숫자 중 6개를 찍어서 맞히는 대표적인 복권

lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]

def solution(lottos, win_nums):
    win_num = [l for l in lottos if l in win_nums]
    answer = []
    zero_count = lottos.count(0)

    if len(win_num) >= 6 :
        answer.append(1)
    elif len(win_num) == 5 :
        answer.append(2)
    elif len(win_num) == 4 :
        answer.append(3)
    elif len(win_num) == 3 :
        answer.append(4)
    elif len(win_num) == 2 :
        answer.append(5)
    else :
        answer.append(6)
    
    if answer[0] - zero_count <= 1 :
        answer.insert(0, 1)
    else :
        answer.insert(0, answer[0] - zero_count)
    
    return answer

print(solution(lottos, win_nums))
