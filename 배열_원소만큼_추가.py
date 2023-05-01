def solution(arr):
    answer = []
    for a in arr:
        answer.extend([a] * a)
    return answer


print(solution([5, 1, 4])) # [5, 5, 5, 5, 5, 1, 4, 4, 4, 4]
print(solution([6, 6])) # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
print(solution([1])) # [1]