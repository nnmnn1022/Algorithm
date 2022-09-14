def solution(d, budget):
    for i in range(1, len(d)+1):
        if sum(d) <= budget : return len(d)
        d_ = sorted(d)[:-i]
        if ((sum(d_)) <= budget) : return len(d_)

        # d.sort()
        # while budget < sum(d):
        #     d.pop()

print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))
print(solution([10000,25000,22500,35000,30000], 90000))