def solution(N, stages):
    answer = []
    user=[0]*(N+2)
    sum=len(stages)
    d={}
    #실패율이 높은 순으로.
    
    for i in stages:
        user[i]+=1#배열 선언하고 그 값마다 플러스 1

    for k in range(1,N+1):#딕셔너리에 실패율이 0이면 0 아니면 그냥 그 전꺼에서 나누기해서 값을 넣어놈
        if user[k]==0:
            d[k]=0
        else:
            d[k]=user[k]/sum
            sum-=user[k]

    redict=list(sorted(d.items(), key=lambda x:x[1],reverse=True))#정렬
    for i in redict:
        answer.append(i[0])
        
                  
    return answer