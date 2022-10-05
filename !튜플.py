from collections import Counter
import re


def solution(s):
    # answer = []
    # s = s.replace('{', '')
    # sorted_s = sorted(s[:-2].split('},'), key=lambda x: len(x))


    # for c in sorted_s:
    #     answer.extend(map(int, c.split(',')))
    #     answer = list(dict.fromkeys(answer))
    
    # return answer
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))