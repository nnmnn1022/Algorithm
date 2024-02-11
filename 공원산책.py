def solution(park, routes):
    # route를 나눠서 어떻게 움직일지 결정하는 함수
    def move(cur_location:list, route: str) -> list:
        # "E 5" => ["E", "5"]
        v, n = route.split(" ")
        n = int(n)

        x, y = cur_location

        # park의 x 길이
        x_len = len(park)
        y_len = len(park[0])

        # 동
        if v == 'E': 
            if y+n >= y_len or any(map(lambda a: y< a <= y+n, warn.get(x))):
                return None
            y += n
            
        # 서
        elif v == 'W': 
            if y-n < 0 or any(map(lambda a: y-n<= a < y, warn.get(x))):
                return None
            y -= n
        # 남
        elif v == 'S':
            if x+n >= x_len or any(y in warn.get(a) for a in range(x, x+n+1)):
                return None
            x += n
        # 북
        elif v == 'N':
            if x-n < 0 or any(y in warn.get(a) for a in range(x-n, x+1)):
                return None
            x -= n

        return [x,y]

    start = []
    warn = {}
    warn_list = []

    # 시작 지점 및 장애물 체크
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S": start = [i,j]
            elif park[i][j] == "X": warn_list.append(j)
        warn[i] = warn_list
        warn_list = []

    for route in routes:
        if move(start, route):
            start = move(start, route)

    return start

# [0,1]
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]))
# [2,1]
print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
# [0,0]
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))