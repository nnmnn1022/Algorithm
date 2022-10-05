def solution(n):
    a = 0

    for num in range(1, n+1):
        if n - num == 0: a += 1
        elif n // num > 1:
            sum = 0
            tmp = num
            while(sum < n):
                sum += tmp
                tmp = tmp + 1
            if sum == n : a +=1

    return a

print(solution(15))
print(solution(16))