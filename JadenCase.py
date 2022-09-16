def solution(s):
    s_arr = list(s)
    i = 0
    for n in range(len(s)):
        if i == 0 : s_arr[n] = s_arr[n].upper()
        else : s_arr[n] = s_arr[n].lower()
        i += 1
        if s_arr[n] == ' ' : i = 0
    return ''.join(s_arr)


print(solution("3people  unFollowed me"))
print(solution("for the last week"))