# 사용된 객실은 퇴실 시간 + 10분 후 이용 가능
# 필요한 최소 객실 수
# 대실시작시각, 종료 시각["HH:MM", "HH:MM"] 24시간제

import datetime
import heapq

def solution(book_time) -> int:

    # 입실시간 순으로 정렬
    book_time = sorted(book_time)

    # room
    rooms = []

    # 입실 시간 리스트를 순회하면서 필요한 방 리스트를 만듦
    for start, end in book_time:
        # rooms[0]이 항상 최솟값을 가져오도록 함.
        # 퇴실 후 10분 뒤를 저장
        # after_cleaning_room = datetime.datetime.strptime(end, '%H:%M') + datetime.timedelta(minutes=10)
        # heapq.heappush(rooms, after_cleaning_room.strftime('%H:%M'))
        end_hour, end_minutes = map(int, end.split(":"))
        end_minutes += 10
        end_hour = str(end_hour + (end_minutes // 60)).zfill(2)
        end_minutes = str(end_minutes % 60).zfill(2)
        after_cleaning_room = end_hour + ":" + end_minutes
        heapq.heappush(rooms, after_cleaning_room)

        # 퇴실 후 10분 뒤의 시간이 시작보다 늦으면 해당 정보 삭제
        if start >= rooms[0]:
            heapq.heappop(rooms)

    answer = len(rooms)

    return answer

print(solution([["14:52", "16:55"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:56"], ["18:20", "21:20"]])) # 3
# print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])) # 3
# print(solution([["09:10", "10:10"], ["10:20", "12:20"]])) # 1
# print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]])) # 3