def solution(left, right):
    answer = 0
    #이문제 어디서 봤는데...?
    
    for i in range(left,right+1):
        measure=1
        for k in range(1,(i//2)+1):
            if i%k==0:
                measure+=1
        if measure%2==1:#홀수
            answer-=i
        else:#짝수
            answer+=i
    
    return answer