def solution(arr, divisor):
    answer = sorted([i for i in arr if i % divisor == 0])
    if len(answer) < 1 :
        return [-1]
    else : return answer

    #return sorted([i for i in arr if i%divisor == 0]) or [-1]

arr = [2, 36, 1, 3]
divisor = 1
print(solution(arr, divisor))


