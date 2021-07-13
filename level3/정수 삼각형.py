def solution(triangle):
    arr_answer=[]
    arr_answer.append(triangle[0])
    
    for i in range(1,len(triangle)):#전형적인 DP문제임. 
        sentence=[]
        for j in range(len(triangle[i])):
            if j==0:#첫번쨰와
                sentence.append(triangle[i][0]+arr_answer[i-1][0])
            elif j==len(triangle[i])-1:#맨 뒤에는 계속 더하기만 하고
                sentence.append(triangle[i][-1]+arr_answer[i-1][-1])
            else:#나머지들은 양쪽을 비교해서 큰거를 값으로 넣기.
                sentence.append(max((triangle[i][j]+arr_answer[i-1][j]),(triangle[i][j]+arr_answer[i-1][j-1])))
        arr_answer.append(sentence)#다 넣은걸 arr_answer에 넣고
    
    return max(arr_answer[len(arr_answer)-1])#맨 마지막 리스트에서 가장 큰 값을 고르면 됨.
