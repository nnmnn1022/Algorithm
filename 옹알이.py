#  "aya", "ye", "woo", "ma" 네 가지 발음과 네 가지 발음을 조합해서 만들 수 있는 발음
# 연속해서 발음할 수 없음

def solution(babbling):
    cando = ['aya', 'ye', 'woo', 'ma']

    # 옹알이하고 남은 발음 = []
    remain = ''
    # 말할 수 있는 단어 개수
    n = 0

    # for
    for b in babbling:
        remain = b
        i = 0
        # 현재 발음 = ''
        now = ''
        # while 돌리기
        while(True):
            # babbling이 cando 중 하나로 시작하면
            if not remain:
                n += 1
                break
            elif i >= 4 :
                break
            elif now != cando[i] and remain.startswith(cando[i]):
                # 현재 발음 넣기
                now = cando[i]
                len_now = len(now)
                # 발음한 부분 빼기
                remain = remain[len_now:]
                i = -1

            i += 1

    return n


print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
# print(solution(10, 7, 14))

# 1 2 3 4 5 6
# 2 2 3 4 5 6
# 3 3 3 4 5 6
# 4 4 4 4 5 6
# 5 5 5 5 5 6
# 6 6 6 6 6 6

