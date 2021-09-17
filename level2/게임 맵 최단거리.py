import heapq
def solution(maps):
    answer = 0
    #이거 다익스트라이면 금방할듯?
    INF=987654321
    n=len(maps)
    graph=[[] for _ in range(((n*n)+1))]
    distance=[[INF]*((n*n)+1)]
    start=1
    
    x_value=[0,1,0,-1]#동남서북
    y_value=[1,0,-1,0]
    for i in range(n):
        for j in range(n):
            #print((i*n)+(j+1))
            for index in range(4):
                if i+x_value[index]>=0 and j+y_value[index]>=0 and i+x_value[index]<n and j+y_value[index]<n:
                    if maps[i+x_value[index]][j+y_value[index]]==1:
                        
                        if i==0:#동
                            graph[(i*n)+(j+1)].append([(i*n)+(j+1)+1,1])
                            graph[(i*n)+(j+1)+1].append([(i*n)+(j+1),1])
                        elif i==1:#남
                            graph[(i*n)+(j+1)].append([((i+1)*n)+(j+1),1])
                            graph[((i+1)*n)+(j+1)].append([(i*n)+(j+1),1])
                        elif i==2:#서
                            graph[(i*n)+(j+1)].append([(i*n)+(j+1)-1,1])
                            graph[(i*n)+(j+1)-1].append([(i*n)+(j+1),1])
                        elif i==3:#북
                            graph[(i*n)+(j+1)].append([((i-1)*n)+(j+1),1])
                            graph[((i-1)*n)+(j+1)].append([(i*n)+(j+1),1])
    print(graph)
                               
#     q=[]
#     heapq.heappush(q,(0,start))
#     distance[start]=0    
#     while q:
#         dist,now=heapq.heappop(q)
#         if distacne[now]<dist:
#             continue
        
#         for i in graph[now]:
#             cost=dist+i[1]
            
#             if cost<distance[i[0]]:
#                 distance[i[0]]=cost
#                 heapq.heappush(q,(cost,i[0]))
            

    return answer