
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

def solution(numbers, hand):
    cur_left = -1
    cur_right = -3
    hand_initial = list(hand)[0].upper()
    
    answer = ''
    phone = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9],
             [-1, 0, -3]
    ]

    def where_num(n) :
        for i, arr in enumerate(phone) :
            if n in arr:
                return i, arr.index(n)

    for num in numbers :
        if num == 1 or num ==4 or num ==7 :
            answer += "L"
            cur_left = num
        elif num == 3 or num ==6 or num ==9 :
            answer += "R"
            cur_right = num
        else :
            num_row, num_col = where_num(num)
            left_row, left_col = where_num(cur_left)
            right_row, right_col = where_num(cur_right)

            if abs(num_row - left_row) + abs(num_col - left_col) == abs(num_row - right_row) + abs(num_col - right_col) :
                answer += hand_initial
                if hand in "right" :
                    cur_right = num
                else :
                    cur_left = num
            elif abs(num_row - left_row) + abs(num_col - left_col) < abs(num_row - right_row) + abs(num_col - right_col) :
                answer += "L"
                cur_left = num
            else :
                answer += "R"
                cur_right = num
                
    return answer

print(solution(numbers, hand))