import re


def solution(wallpaper):
    
    # 가장 왼쪽 파일의 X축 확인
    X_list = []
    Y_list = []
    for i, row in enumerate(wallpaper) :
        for location in re.finditer("#", row):
            X_list.append(location.start())
            Y_list.append(i)

    X_list = sorted(X_list)
    Y_list = sorted(Y_list)

    # [가장 왼쪽 파일 X축, 가장 위 파일 Y축, 가장 오른쪽 파일 X축 + 1, 가장 아래 파일 Y축 + 1]
    # 뒤에 2개를 +1 해주는 이유는 드래그를 그 아래까지 해야 하기 때문
    return [Y_list[0], X_list[0], Y_list[-1] + 1, X_list[-1] + 1]


print(solution([".#...", "..#..", "...#."])) # [0, 1, 3, 4]
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."])) # [1, 3, 5, 8]
# [0, 0, 7, 9]
print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))
print(solution(["..", "#."])) # [1, 0, 2, 1]
