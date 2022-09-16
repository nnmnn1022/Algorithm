def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    answer = participant[-1]
    for i in range(len(completion)):
        if participant[i] != completion[i] :
            answer = participant[i]
            break

    return answer


print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))