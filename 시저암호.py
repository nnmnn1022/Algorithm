def solution(s, n):
    answer = ''
    for ss in s:
        # 공백 여부 확인 확인
        if ss == " ": 
            answer += " "
            continue

        # 소문자 여부 확인
        _isLower = ss.islower()
        if _isLower : ss = ss.upper()

        # ascii로 변환
        asc = ord(ss)

        # Z를 넘어가면 A로 돌아가도록
        if asc + n > 90 : asc -= 26 
        
        # 거리만큼 추가
        ans = chr(asc + n)

        if _isLower : ans = ans.lower()

        answer += ans

    return answer

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B  Z", 4))