def solution(string):
    arr = []
    # and로 이어진 조건문에서 앞선 조건이 False 처리되면 뒤는 실행되지 않는 것으로 보임 
    if len(arr) != 0 and arr[-1] == s:
        print(arr)
    if len(string) % 2 != 0 : return 0
    for s in string:
        if len(arr) != 0 and arr[-1] == s:
            arr.pop()
        else :
            arr.append(s)
    
    if len(arr) == 0 : return 1
    else : return 0

print(solution('baabaa'))
print(solution('cdcd'))

