def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([])#이게 신기한게 이중배열할때 이런식으로 
        for j in range(len(arr1[i])):
            answer[i].append(arr1[i][j]+arr2[i][j])#더하는 것 

#배열 넣기 그리고 행 더하고 그 행의 열에 원소 넣기 
            
    return answer