def solution(n):
    first,last,standard=0,0,0
    number=""
    i,sum=1,3
    while True:#n이 속해있는 범위와 first last의 값을 얻기 위해 존재.
        if n<=sum:
            last=sum
            first=sum-3**i
            break
        i+=1    
        sum=sum+3**i
        
    while True:
        standard=(last-first)/3 #범위를 좁혀나가기위해 존재.
        
        if first<n<=first+standard:#1번째 범위
            last=first+standard# first는 그대로 두고 Last 변경
            number=number+"1"
        elif first+standard<n<=last-standard:#2번째 범위
            first=first+standard#first 변경
            last=last-standard#Last 변경
            number=number+"2"
        elif last-standard<n<=last:#3번째 범위
            first=last-standard#Last는 그대로 두고 first 변경.
            number=number+"4"
        if int(standard)==1:#만약 standard 1이 된거면 break로 빠져나오기.
            break
            
    return number