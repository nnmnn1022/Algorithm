import time
start = time.time()

# 사라질 인형의 개수 구하기
# board = 배열
# moves = 크레인 내리는 곳

def solution(board, moves):
    # 크레인이 집어서 넣을 리스트
    result = []
    # 사라진 인형의 개수
    answer = 0
    # for
    for m in moves:
        for b in board:
            # b[m-1]이 0이 아닐 때
            if b[m-1] != 0:
                # result[-1]이 b[m-1]인지 확인하고 맞으면 pop, answer
                if result and result[-1] == b[m-1]:
                    b[m-1] = 0
                    result.pop()
                    answer += 2
                else :
                    # result.append(b[m-1])
                    result.append(b[m-1])
                    b[m-1] = 0
                break
        
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]	))
print("time :", time.time() - start)