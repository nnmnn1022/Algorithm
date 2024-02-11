def solution(name, yearning, photo):
    answer = []
    point = {n:yearning[i] for i,n in enumerate(name)}

    for p in photo:
        answer.append(sum(map(lambda x: point.get(x, 0), p)))
    return answer

# [19, 15, 6]
print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
# [67, 0, 55]
print(solution(["kali", "mari", "don"],	[11, 1, 55],	[["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]	))
# [5, 15, 0]
print(solution(["may", "kein", "kain", "radi"],	[5, 10, 1, 3],	[["may"],["kein", "deny", "may"], ["kon", "coni"]]	))