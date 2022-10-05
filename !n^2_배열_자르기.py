# def solution(n, left, right):
#     arr = []
#     start = left // n + 1
#     end = right // n + 1

#     for i in range(start, end+1):
#         arr.extend([i]*i)
#         arr.extend(list(range(i+1, n+1)))

#     return arr[left%n:(end-start)*n+right%n+1]

def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)
    return answer

print(solution(3, 2, 5))
print(solution(4, 7, 14))
# print(solution(10, 7, 14))

# 1 2 3 4 5 6
# 2 2 3 4 5 6
# 3 3 3 4 5 6
# 4 4 4 4 5 6
# 5 5 5 5 5 6
# 6 6 6 6 6 6

