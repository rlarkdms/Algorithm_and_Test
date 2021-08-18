# 풍성 터트리기의 규칙이 있음
import heapq
def solution(a):
    answer=0
    #힙의 복잡도가 미쳐있는데....
    #근데 여기서 a의 수는 모두 다르다가 쫌 좋은 관점인데....
    # 내가 생각했던 방법인 오른쪽의 가장 작은 값을 구하고 그 값이 나오면 다시 update하는건 큰 문제점이 하나 있음 그건....만약 수의 배치가 
    # 1,2,3,4,5...이런식으로 올라가면 연산을 계속 해야하는 문제가 일어날 수 있음...음 일단 해볼까?
    # 해당 풀이는 시간초과가 남.    
    if a==1:
        return 1
    if a==2:
        return 2
    
#     min_left=a[0]
#     min_right=min(a[2:len(a)])
#     answer = 2
    
#     for i in range(1,len(a)-1):
#         #print(i)
#         if a[i]>min_left and a[i]>min_right:#이거는 하나 더해야 함.
#             pass
#         else:
#             answer+=1
            
#         if min_left>a[i]:#이 부분은 아마 맞을 거야.
#             min_left=a[i]
        
#         if a[i]==min_right:
#             min_right=min(a[i+1:len(a)])
#     #이거 내가 아무리봐도 힙정렬 문제임.
    heap_right=[]
    for i in range(2,len(a)):
        heapq.heappush(heap_right,a[i])
    answer=2
    min_left=a[0]
    for i in range(1,len(a)-1):
        if a[i]<min_left or a[i]<heap_right[0]:#이거는 하나 더해야 함.
            answer+=1
            
        if min_left>a[i]:#이 부분은 아마 맞을 거야.
            min_left=a[i]
        
        
        if heap_right[0]==a[i]:#여기부분에서 연산을 더 빨리할 방법을 찾ㅇ아야 함 도는데 더 적은 시간이 걸리는 방법... 결국 여기는 계속 돌면서 최솟값이 일치하면 나머지 곳에서 가장 최솟값을 구하는 곳이기 때문에...이걸 생각해보고 오늘은 여기까지 하자 나머지는 다른 공부해야하니까...^_^;
            heapq.heappush(heap_right,a[i])
            
            
        
        
        
    
        
    
    
    #print(answer)
    
    return answer