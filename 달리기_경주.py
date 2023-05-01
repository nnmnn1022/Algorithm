def solution(players, callings):
    # 사람: 등수
    rank = {p:r for r, p in enumerate(players, start=1)}
    # 등수: 사람
    player = {r:p for r, p in enumerate(players, start=1)}

    for called_player in callings:
        # 현재 불린 사람의 등수
        now_called_rank = rank[called_player]

        # 추월 당한 사람
        overtaked_player = player[now_called_rank - 1]

        # 추월 당한 사람의 원래 등수
        overtaked_rank = rank[overtaked_player]

        # 불린 사람 등수 높이기
        player[now_called_rank] = overtaked_player
        rank[called_player] = overtaked_rank

        # 추월 당한 사람 등수 낮추기
        player[overtaked_rank] = called_player
        rank[overtaked_player] = now_called_rank

    sorted_player = sorted(rank, key=rank.get)
    return sorted_player


# ["mumu", "kai", "mine", "soe", "poe"]
print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))