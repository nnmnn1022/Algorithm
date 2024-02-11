# 숫자로 이루어진 문자열 t와 p
# t에서 p와 길이가 같은 부분문자열 중에서, 이 부분문자열이 나타내는 수가 p가 나타내는 수보다 작거나 같은 것이 나오는 횟수를 return

def solution(t, p):

    return len([t[i:i+len(p)] for i,_ in enumerate(t) if i+len(p) <= len(t) and int(t[i:i+len(p)]) <= int(p)])

print(solution("3141592", "271"))
print(solution("500220839878", "7"))
print(solution("10203", "15"))