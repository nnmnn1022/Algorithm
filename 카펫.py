def solution(brown, yellow):
    y_arr = [[yellow//i, i] for i in range(1, yellow+1) if yellow % i == 0 and i <= yellow//i]

    for i in range(len(y_arr)):
        y_row = y_arr[i][0]
        y_col = y_arr[i][1]

        b_row = y_row + 2
        b_col = y_col + 2

        if (brown == b_row * b_col - yellow):
            return [b_row, b_col]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
