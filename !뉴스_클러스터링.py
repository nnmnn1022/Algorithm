import re
import math

# https://velog.io/@munang/%EA%B0%9C%EB%85%90%EC%A0%95%EB%A6%AC-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8B%A4%EC%A4%91-%EC%A7%91%ED%95%A9
def solution(str1, str2):
    # 두 글자씩 끊어서 다중집합의 원소로 만든다. 이때 영문자로 된 글자 쌍만 유효하고,
    # 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다
    # 대문자와 소문자의 차이는 무시한다
    str_li1 = []
    str_li2 = []

    for i in range(len(str1)):
        if i+1 < len(str1):
            st = str1[i].lower() + str1[i+1].lower()
            if not re.search(r'[^a-z]', st):
                str_li1.append(st)

    for i in range(len(str2)):
        if i+1 < len(str2):
            st = str2[i].lower() + str2[i+1].lower()
            if not re.search(r'[^a-z]', st):
                str_li2.append(st)

    # 합집합용
    tmp = str_li2[:]
    result = str_li2[:]

    # 교집합용
    str_li1_tmp = str_li1[:]
    tmp2 = str_li2[:]
    result2 = []

    # 합집합
    for s in str_li1:
        if s in tmp:
            tmp.remove(s)
        else :
            result.append(s)
    
    # 교집합
    for s in str_li1_tmp:
        if s in tmp2:
            result2.append(s)
            tmp2.remove(s)

    len1 = len(result)
    len2 = len(result2)

    if len1 == 0 and len2 == 0:
        return 65536
    elif len1*len2 == 0:
        return 0

    return math.floor(min(len1, len2) / max(len1, len2) * 65536)
    # answer = 0
    # str1 = [s for s in str1.lower()]
    # str2 = [s for s in str2.lower()]

    # if not str1 and not str2:
    #     return 65536

    # str1_li = []
    # str2_li = []
    # for i in range(len(str1)):
    #     st = ''.join(str1[i:i+2])
    #     if not re.search(r'[^a-z]', st):
    #         str1_li.append(st)
    # if len(str1_li[-1]) < 2 : str1_li.pop()
    # for i in range(len(str2)):
    #     st = ''.join(str2[i:i+2])
    #     if not re.search(r'[^a-z]', st):
    #         str2_li.append(st)
    # if len(str2_li[-1]) < 2 : str2_li.pop()


    # li1 = []
    # li2 = str1_li[:]
    # li2.extend(str2_li)
    # for s in str1_li:
    #     if s in str2_li:
    #         li1.append(s)
    #         str2_li.remove(s)
    #         li2.remove(s)

    # len1 = len(li1)
    # len2 = len(str1_li)
    # if len1 == 0 or len2 == 0:
    #     return 0
    # answer = math.floor(min(len1, len2) / max(len1, len2) * 65536)
    

    return 1

print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))


