# def solution(N, stages):
#     answer = []
#     dict = {}
#     # str_stages = [str(i) for i in stages]

#     # for s in stages:
#     for i in range(1, N+1):
#         # s 보다 크거나 같은 수를 받아서 문자열 리스트 li 생성
#         li = [a for a in stages if a >= i]

#         # dict[s] = str_stages.count(s) / len(li))
#         if i not in stages : 
#             dict[i] = 0
#         elif i == N+1 :
#             dict[N] = 0
#         else :
#             dict[i] = li.count(i) / len(li)

#     # sorted(dict, keys??)
#     tmp = sorted(dict.items(), key= lambda item : (-item[1], item[0]))
#     answer = [b[0] for b in tmp]
#     return answer

def solution(N, stages):
    answer = []
    fail = []
    info = [0] * (N + 2)
    for stage in stages:
        info[stage] += 1
    for i in range(N):
        be = sum(info[(i + 1):])
        yet = info[i + 1]
        if be == 0:
            fail.append((str(i + 1), 0))
        else:
            fail.append((str(i + 1), yet / be))
    for item in sorted(fail, key=lambda x: x[1], reverse=True):
        answer.append(int(item[0]))
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))

