def solution(n, lost, reserve):
    # 여분 체육복을 도난당한 사람은 제외
    set_lost = list(set(lost) - set(reserve))
    set_reserve = list(set(reserve) - set(lost))

    answer = n - len(set_lost)
    rev_answer = n - len(set_lost)
    lost, reserve = sorted(set_lost), sorted(set_reserve)
    rev_lost, rev_reserve = sorted(set_lost, reverse=True), sorted(set_reserve, reverse=True)

    # lost를 순회해서 멤버 앞뒤로 여분이 있는지 확인
    for l in lost :
        # 부족한 사람은 왼쪽 사람 것을 빌림
        if l-1 in reserve :
            reserve.remove(l-1)
            answer += 1
        # 만약 왼쪽에 여분이 없으면 오른쪽을 빌림.
        elif l+1 in reserve :
            reserve.remove(l+1)
            answer += 1

    for l in rev_lost :
        # 부족한 사람은 왼쪽 사람 것을 빌림
        if l-1 in rev_reserve :
            rev_reserve.remove(l-1)
            rev_answer += 1
        # 만약 왼쪽에 여분이 없으면 오른쪽을 빌림.
        elif l+1 in reserve :
            rev_reserve.remove(l+1)
            rev_answer += 1
    
    return max(answer, rev_answer)


print(solution(5,[2, 4],[1, 3, 5]))
print(solution(5,[2, 4],[3]))
print(solution(3,[3],[1]))