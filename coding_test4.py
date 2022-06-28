# 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발
# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.

# 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 알고 싶습니다

# 중요도가 순서대로 담긴 배열 priorities
# 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location
# 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return
priorities = [1, 1, 9, 1, 1, 1]
location = 0

# 1322 / 3221 / 221 / 21 /1

def solution(priorities, location):
    answer = 0
    queue0 = [[p, i] for i, p in enumerate(priorities)]

    while(len(queue0) > 0) :
        if queue0[0][0] == max(priorities)  :
            if queue0[0][1] == location :
                answer += 1
                return answer
            else :
                del queue0[0]
                del priorities[0]
                answer += 1
        else :
            tmp = queue0.pop(0)
            tmp2 = priorities.pop(0)
            queue0.append(tmp)
            priorities.append(tmp2)

solution(priorities, location)