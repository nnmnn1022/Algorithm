def solution(s):
    answer = ""
    i = 0
    for s in list(s) :
        if s != " ":
            answer += s.upper() if not (i % 2) else s.lower()
            i += 1
        else :
            i = 0
            answer += " "
        
    return answer

print(solution("try  dasdf"))