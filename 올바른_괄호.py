# def solution(string):
#     if string[0] == ')' or string[-1] == '(':
#         return False
#     num = 0
#     for i in range(len(string)):
#         if string[i] == '(':
#             num += 1
#         else :
#             num -= 1
#         if num < 0 : return False
#     if num != 0 :
#         return False
#     return True

# 2022.11.04
def solution(string):
    str_li = list(string)
    answer = []
    # str_li 를 순회하며 answer에 값을 push, [-1]에 찍을 이루는 값이 있으면 not push, do pop
    for s in str_li:
        if answer and (s == ")" and answer[-1] == "("):
            answer.pop()
        else: answer.append(s)

    return False if answer else True


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))