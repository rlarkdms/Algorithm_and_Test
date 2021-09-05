def solution(m, n, board):
    board_list=[]
    for i in range(n):#여기 부분이 행렬를 돌리는 부분. 예를 들면 ["CCBDE", "AAADE", "AAABF", "CCBBF"]를 
        statement=[]# [['C','A','A','C'],['C','A','A','C'],['B','A','A','B'], ['B','B','D','D'], ['F','F','E','E']]로 돌림.
        for j in range(m-1,-1,-1):#이유는 pop,append를 하기 용이하게 하기 위해서 돌림.
            statement.append(board[j][i])
        board_list.append(statement)
    
    return retrieve(m,n,board_list)#그리고 만든 함수를 돌림.
def retrieve(m,n,board):
    arr=[]
    standard=0
    #print("몇번")
    for i in range(n-1):
        for j in range(m-1):
            if board[i][j]!='0':
                if same(board[i][j],board[i+1][j],board[i][j+1],board[i+1][j+1])==1:#밑에 선언한 same 함수를 통해 가 다 같으면 처리해야할 값을 arr에 넣어두기.
                    arr.append([i,j])
                    standard+=1#이 변수는 짝을 맞춰 없어질 패들이 있는지 확인하는 변수
    if standard==0:#패들이 만약 한개도 없어지지 않는다면 0의 개수를 세서 return
        answer=0
        for i in range(n):
            for j in range(m):
                if board[i][j]=='0':
                    answer+=1    
        return answer
    
    for i in arr:#이제 짝이 맞는 곳은 '0'으로 정의
        board[i[0]][i[1]]='0'
        board[i[0]+1][i[1]]='0'
        board[i[0]][i[1]+1]='0'
        board[i[0]+1][i[1]+1]='0'
    for i in range(n):#하나씩 세면서 0인 부분은 뒤로 보내기.그리고 0을 뒤로 보내서 append 이렇게 하는 이유가 재귀로 계속 돌릴려고 하는데 배열의 크기가 맞지 않으면 문제가 생겨서 뒤를 0으로 채워 놓는것.
        for j in range(m-1,-1,-1):
            if board[i][j]=='0':
                board[i].pop(j)
                board[i].append('0')
    
    return retrieve(m,n,board)# 돌려돌려 돌림판
def same(a,b,c,d):#SAME : 4개의 짝이 맞는 지 확인하는 용도.
    if a==b and b==c and c==d and a==d:
        return 1
    else:
        return 0