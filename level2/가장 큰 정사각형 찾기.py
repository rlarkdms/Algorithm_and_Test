def solution(board):
    answer = 1234
    #사실 큰거부터 작은거로 가면...흠...
    #표의 행의 크기(1000이하의 자연수) 이니까 될 수도...?1->4->16->...->1000인데 개쌉노답 트리인데 문제는 어떻게 하든 개쌉노답 트리인데..?
    #아니 근데 이것도 문제가 일어날 가능성이 큰데...?
    #생각해보니 만약 1이 나오고 0이나 벽을 만날 때까지 돌고, 그 밑까지 가능한지 확인해보면 그 부분은 다 안되는 거 아니야???
    #그니까 0이나 벽 만날때까지
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==1:
                    
            elif board[i][j]==0:
                
            #print(i,j)
        
    
    return answer