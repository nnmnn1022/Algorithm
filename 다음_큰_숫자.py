def solution(n):
    # 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
    # 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
    # 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
    i = n
    while(True):
        i += 1
        if bin(i).count('1') == bin(n).count('1'):
            break

    return i

print(solution(78))
print(solution(15))


