def solution(x):
    answer = True
    
    x=str(x)#일단 x를 str으로 만들고 
    sum=0
    for i in x:#자리수구하고
        sum+=int(i)#더하기
    
    if int(x)%sum==0:#나눠서 0이면 True
        answer=True
    else:
        answer=False#아니면 False
    
    
    return answer