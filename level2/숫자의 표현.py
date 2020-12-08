def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        count=0
        for j in range(i,n+1):
            count=count+j
            if count==n:#같으면 answer+=1
                answer+=1
            elif count>n:#넘으면 break
                break
            
            
    return answer