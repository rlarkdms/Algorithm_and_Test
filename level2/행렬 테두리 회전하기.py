from collections import deque
def solution(rows, columns, queries):
    answer = []
    arr=[]
    
    for i in range(rows):#미리 set하기 위해서
        sentence=[]
        for j in range(1,columns+1):
            sentence.append((i*columns)+j)
        arr.append(sentence)
    
    for i in queries:#일일이 하나하나 노가다
        arr_count=deque() # 큐로 구현한 이유가 popleft를 진행하기 위해서이다.
        for k in range(i[1]-1,i[3]-1):
            arr_count.append(arr[i[0]-1][k])
        
    
        for k in range(i[0]-1,i[2]-1):
            arr_count.append(arr[k][i[3]-1])
            
        for k in range(i[3]-1,i[1]-1,-1):
            arr_count.append(arr[i[2]-1][k])
           
        for k in range(i[2]-1,i[0]-1,-1):
            arr_count.append(arr[k][i[1]-1])   
        
        answer.append(min(arr_count))#제일 작은거 고르기
        arr[i[0]-1][i[1]-1]=arr_count.pop()
        for k in range(i[1],i[3]-1):
            arr[i[0]-1][k]=arr_count.popleft()
        for k in range(i[0]-1,i[2]-1):
            arr[k][i[3]-1]=arr_count.popleft()
        for k in range(i[3]-1,i[1]-1,-1):
            arr[i[2]-1][k]=arr_count.popleft()
        for k in range(i[2]-1,i[0]-1,-1):
            arr[k][i[1]-1]=arr_count.popleft()   
        
        
    return answer

# def bingbing(arr,i):
#     arr_count=[]
#     up_left = [i[0]-1,i[1]-1]
#     up_right = [i[0]-1,i[3]-1]
#     down_left = [i[2]-1,i[1]-1]
#     down_right = [i[2]-1,i[3]-1]
#     for k in range(i[1],i[3]):
#         arr_count.append(arr[i[0]-1][k])
#     print(arr_count)
    
#     for k in range(i[0],i[2]):
#         arr_count.append(arr[k][i[3]-1])
#     print(arr_count)    
#     for k in range(i[3]-2,i[1]-2,-1):
#         arr_count.append(arr[i[2]-1][k])
#     print(arr_count)    
#     for k in range(i[2]-2,i[0]-2,-1):
#         arr_count.append(arr[k][i[1]-1])    
#     print(arr_count)
    
#     print(up_left,up_right,down_left,down_right)
    
    
#     return arr