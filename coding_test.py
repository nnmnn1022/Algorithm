
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2



def solution(id_list, report, k):
    answer = [0 for _ in id_list]
    report = list(set(report))
    report_new = [r.split() for r in report]

    for id in id_list :
        reported_num = 0
        report_person = []
        for r in report_new :
            if r[1] != id : continue
            reporter = r[0]
            complainant = r[1]
            if id == complainant and (reporter not in report_person) :
                report_person += [reporter]
                reported_num += 1
        
        if reported_num >= k :
            for person in report_person :
                answer[id_list.index(person)] += 1
    return answer


# def solution(id_list, report, k):
#     answer = [0 for _ in id_list]

#     for id in id_list :
#         reported_num = 0
#         report_person = []
#         for r in report :
#             reporter, complainant = r.split(' ')
#             if id == complainant and (reporter not in report_person) :
#                 report_person += [reporter]
#                 reported_num += 1
        
#         if reported_num >= k :
#             for person in report_person :
#                 answer[id_list.index(person)] += 1
#     return answer

solution(id_list, report, k)