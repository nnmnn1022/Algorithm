def solution(n, words):
    answer = []
    i = 0
    flag = True
    for s in words:
        if s in answer or (answer and s[0] != answer[-1][-1]):
            flag = False
            break
        answer.append(s)
        i += 1
    if flag : return [0,0]

    return [i%n + 1, i // n + 1]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))