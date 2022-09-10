def solution(s):
    # if len(s) == 4 or len(s) == 6 : 
    #     return s.isdecimal()
    # return False

    return s.isdigit() and len(s) in (4, 6)

s = "a234"
print(solution(s))

s = "1234"
print(solution(s))





