def solution(n):
    answer = 0
    transfered = ''

    while(n > 0):
        # divmod -> (n // 3 , n % 3) 반환
        n, mod = divmod(n, 3)
        transfered += str(mod)

    # int로 n 진수를 정수로 되돌릴 수 있다. str형 n진수, 진수
    return int(transfered, 3)

print(solution(125))