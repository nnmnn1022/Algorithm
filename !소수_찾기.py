def solution(n):
    # 에라토스테네스의 체
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i)) # i를 제외한 i의 배수들을 num에서 제외
    return len(num)

print(solution(1000000))
print(solution(5))
