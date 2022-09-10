def solution(arr1, arr2):
    answer= []
    for i, arr1_i in enumerate(arr1):
        ans = []
        for j, arr1_j in enumerate(arr1_i):
            ans.extend([arr1_j + arr2[i][j]])
        answer.append(ans)
    
    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
print(solution([[1],[2]], [[3],[4]]))