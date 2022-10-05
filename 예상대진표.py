def solution(n,a,b):
    i = 0
    while(True):
        if a > b:
            tmp = a
            a = b
            b = tmp
        i += 1
        if (a % 2 == 1 and a + 1 == b):
            return i
        a = (a + 1) // 2
        b = (b + 1) // 2
        

print(solution(8,4,7))