def solution(numbers):
    answer = []
    numbers_cp = numbers[:]
    for _ in numbers:
        n = numbers_cp.pop()
        answer.extend([n+i for i in numbers_cp])

    return sorted(set(answer))

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))
