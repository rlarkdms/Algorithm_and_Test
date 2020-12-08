def solution(arr1, arr2):
    #answer = [[0]*len(arr2)]*len(arr1)
    answer=[]#곱 행렬로 가는데
    
		#여기서 중요한 개념이 있음!!!
    #내가 까먹었던 개념인데 곱행렬의 경우 (2행 3열) (3행 2열) 일 경우 (2행 2열)이 나와야함 
    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr2[0])):
            count=0
            for s in range(len(arr2)):
                #print (i,s,s,j)
                count=count+(arr1[i][s]*arr2[s][j])#다 곱해서 넣기    
            answer[i].append(count) 
            
    return answer