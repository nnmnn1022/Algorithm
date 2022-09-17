def solution(string):
    if string[0] == ')' or string[-1] == '(':
        return False
    num = 0
    for i in range(len(string)):
        if string[i] == '(':
            num += 1
        else :
            num -= 1
        if num < 0 : return False
    if num != 0 :
        return False
    return True


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))