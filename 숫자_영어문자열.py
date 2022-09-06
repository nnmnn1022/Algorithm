
sss = "one4seveneight"

def solution(string):
    
    if not string.isdigit() :
        dict = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
        for s in dict.keys() :
            if s in string :
                string = string.replace(s, str(dict.get(s)))

    answer = int(string)
    return answer

print(solution(sss))