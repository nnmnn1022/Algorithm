import time
start = time.time()

def solution(A):
    li = []
    answer = []
    # for문 안에서 li[0] 보다 큰 수가 나오면 멈추고 li[0] - li[n] 을 반복해서 담기
    for i, a in enumerate(A):
        li.append(a)
        if len(li) == 0 and li[0] < a:
            li = [a]
        elif len(li) > 1 and li[0] <= a:
            answer.append(li[0] - min(li))
            li = [a]
        elif i == len(A) - 1:
            if len(li) > 1:
                tmp = li.pop()
                answer.append(max(li[0] - min(li), tmp - min(li)))

    # 비교해서 수심 구하기
    return max(answer)

print(solution([1,3,2,1,2,1,5,3,3,4,2]))
print(solution([1,1,1,1,5,1,5,3,3,4,2]))
print("time :", time.time() - start)

