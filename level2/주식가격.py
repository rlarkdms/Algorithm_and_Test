def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        count=0
        for j in range(i+1,len(prices)):#계속 돌면서
            if prices[i]<=prices[j]:#값이 기준이 되는값보다 크면 
                count+=1#더하기
            else:#기준값이 작으면
                count+=1#더하고
                answer.append(count)#append
                break#멈추기
        else:#만약 끝까지 가면
            answer.append(count)#더하기 
        
    return answer