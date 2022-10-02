def solution(a, b):
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = ['FRI','SAT','SUN','MON','TUE','WED']
    # print(sum(month[:6])) == 182 6월까지
    # print(sum(month[:5])) == 152 5월까지
    # 152 + 24 
    # print(176 % 7) == 1
    if a == 1 :
        return day[b % 7 - 1]
    else :
        return day[(sum(month[:a-1]) + b) % 7 - 1]


print(solution(3,1))
# print(solution(2,5))
# print(solution(4,3))
# print(solution(-4,2))

