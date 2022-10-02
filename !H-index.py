def solution(citations):
    s_citations = sorted(citations, reverse=True)
    len_c = len(s_citations)
    answer = 0

    for i in range(len_c):
        if i + 1 <= s_citations[i]:
            answer += 1
        if i + 1 == s_citations[i]:
            break
    return answer
    


print(solution([3, 0, 6, 1, 5]))
print(solution([6,6,6,6]))
# print(solution(2,5))
# print(solution(4,3))
# print(solution(-4,2))

