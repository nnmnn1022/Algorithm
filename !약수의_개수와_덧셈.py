
def solution(left, right):
    answer = []
    for i in range(left, right+1):
        arr = [j for j in range(1, i+1) if i % j == 0]
        if not (len(arr) % 2): # 짝수
            answer.append(i)
        else : # 홀수
            answer.append(-i)
    return sum(answer)

    # 약수가 홀수개인 모든 수는 제곱수
    # for i in range(left, right+1):
    # if int(i**0.5)==i**0.5:
    #     answer -= i
    # else:
    #     answer += i

print(solution(13, 17))
print(solution(24, 27))