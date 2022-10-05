def func(st):
        a = st.count("0")
        b = bin(st.count("1"))[2:]

        return a, b

def solution(x):
    s = x
    i = 0
    sum = 0
    while(s != "1"):
        i += 1
        t, s = func(s)
        sum += t

    return [i, sum]

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))