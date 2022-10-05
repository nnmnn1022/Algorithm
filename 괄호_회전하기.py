def solution(s):
    answer = 0
    s_arr = list(s)
    bracket = {'[':']', '{':'}', '(':')'}

    for _ in range(len(s_arr)):
        arr = []
        for i in range(len(s_arr)):
            if arr and arr[-1] in bracket and s_arr[i] == bracket[arr[-1]]:
                arr.pop()
            else :
                arr.append(s_arr[i])

        tmp = s_arr.pop(0)
        s_arr.append(tmp)
        if not arr: answer += 1
    
    return answer

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))