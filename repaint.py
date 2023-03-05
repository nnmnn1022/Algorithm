# 벽을 1미터짜리 n개로 나눔
# 1부터 n까지
# 롤러의 길이 m
# 구역 section

def solution(n, m, section):
    answer = 0

    # section을 순회하여 앞에서부터 m씩 칠했을 때
    # section[0] + m 보다 작은 애들은 pass 하고 다음 걸 칠해야 함
    # 칠해진 곳의 마지막 부분
    repainted = 0
    for to_repaint in section:
        # 칠해야 하는 위치가 칠해진 곳 보다 크면 칠하고, 칠이 된 곳 표시
        if to_repaint > repainted:
            answer += 1
            repainted = to_repaint + m - 1
        # 이미 칠해져 있으면 pass
        else :
            continue

    return answer


print(solution(8,4,[2, 3, 6]))  # 2
print(solution(5,4,[1,3])) # 1
print(solution(4,1,[1,2, 3, 4])) # 4
