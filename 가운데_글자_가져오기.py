

def solution(s):
    if len(s) % 2 == 1 :
        answer = s[len(s) // 2]
    else :
        answer = s[len(s) // 2 - 1] + s[len(s) // 2]

    return answer

s = "abcde"
print(solution(s))
s = "qwer"
print(solution(s))



