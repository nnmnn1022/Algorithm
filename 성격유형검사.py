survey = ["TR", "RT", "TR"]
choices = 	[7, 1, 3]
dict = {}

def solution(survey, choices):
    for i, c in enumerate(choices) :
        survey_type = list(survey[i])
        score = abs(c-4)

        if (c < 4) :
            if survey_type[0] in dict :
                dict[survey_type[0]] += score
            else : dict[survey_type[0]] = score
        elif (c > 4) :
            if survey_type[1] in dict :
                dict[survey_type[1]] += score
            else : dict[survey_type[1]] = score

    sb = ['RT', 'CF', 'JM', 'AN']
    answer = ''
    for s in sb :
        _s = list(s)
        if (_s[0] in dict and _s[1] in dict):
            if (dict.get(_s[0]) >= dict.get(_s[1])) :
                answer += _s[0]
            else  :
                answer += _s[1]
        elif(_s[0] in dict ) :
            answer += _s[0]
        elif(_s[1] in dict) :
            answer += _s[1]
        else :
            answer += _s[0]

    return answer

print(solution(survey, choices))