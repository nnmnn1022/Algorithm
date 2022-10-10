import time
start = time.time()

import math

# 어떤 차량이 입차된 후에 출차된 내역이 없다면, 23:59에 출차된 것으로 간주
# 누적 주차 시간이 기본 시간이하라면, 기본 요금을 청구
# 기본 시간을 초과하면, 기본 요금에 더해서, 초과한 시간에 대해서 단위 시간 마다 단위 요금을 청구합니다.
# 초과한 시간이 단위 시간으로 나누어 떨어지지 않으면, 올림
# ⌈a⌉ : a보다 작지 않은 최소의 정수를 의미합니다. 즉, 올림
# 정수 배열 fees [기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)]
# 자동차의 입/출차 내역을 나타내는 문자열 배열 records가 매개변수 "시각(HH:MM) 차량번호([0-9]{4}) 내역"

def solution(fees, records):
    answer = []
    # 누적 주차 시간에 따라 금액을 계산하는 함수
    # 출차되지 않으면 23:59에 출차 됨.
    def calculate(record):
        hour = 0
        minute = 0
        time = 0
        if len(record) % 2 == 1:
            record.append(["23:59", "_temp", "OUT"])
        # 레코드 IN / OUT 계산해서 누적 시간 확인
        for l in record:
            if l[2] == 'IN':
                hour = int(l[0][0]+l[0][1])
                minute = int(l[0][3] + l[0][4])
            else :
                time = time + 60 * (int(l[0][0]+l[0][1]) - hour) + int(l[0][3] + l[0][4]) - minute

        # 누적 주차시간 <= 기본 시간: 기본 요금
        if time <= fees[0]:
            return fees[1]
        else:
            return fees[1] + fees[3] * math.ceil((time - fees[0]) / fees[2])

        # else : 기본 요금 + 단위 시간(올림 처리) * 단위 요금 

    # records 데이터 분리
    # 차량 오른차순으로 데이터 정리
    sep_records = sorted([r.split(' ') for r in records], key=lambda r: r[1])
    li = []
    now = ''

    # sep_records를 순차적으로 검사
    for r in sep_records:
        # [현재 차량]이 r[1]과 다르면
        if now != '' and now != r[1]:
            # 여태까지 추출한 자료로 금액 정리 후 append
            answer.append(calculate(li))
            li.clear()

        li.append(r)
        now = r[1]

    # 마지막 li에 관련된 정산
    answer.append(calculate(li))
    
    return answer


print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])) # [14600, 34400, 5000]
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])) # 	[0, 591]
print(solution([1, 461, 1, 10],["00:00 1234 IN"])) # 	[14841]

print("time :", time.time() - start)