
# 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
# 작업의 진도가 적힌 정수 배열 progresses
# 각 작업의 개발 속도가 적힌 정수 배열 speeds

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

def solution(progresses, speeds):
    answer = []
    while len(progresses) > 0 :
        for i in range(len(progresses)) :
            progresses[i] += speeds[i]
        
        i = 0
        try :
            while (progresses[0] >= 100) :
                del progresses[0]
                del speeds[0]
                i += 1
        except IndexError :
            pass

        if i > 0 : answer.append(i)
    return answer

solution(progresses, speeds)