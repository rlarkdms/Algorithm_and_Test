def solution(num):
    answer = 0
    
    while(answer<500):#500번 넘게하면 그냥 빠져나오기
        if num==1:
            break#-1나오면 그냥 break
        if num%2==0:
            answer+=1
            num=num/2
        elif num%2==1:
            answer+=1
            num=(num*3)+1
        
    if num!=1:#500번 돌고 num이 1이 아니면 answer을 -1 정의 
        answer=-1
    
    return answer