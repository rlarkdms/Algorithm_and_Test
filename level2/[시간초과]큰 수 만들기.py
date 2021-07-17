def solution(number, k):
    answer = ''
    #약간 투포인터 문제인데...?
    #nCr = list(itertools.combinations(number, len(number)-k))
    #절대 이 방법으로 해결 못함. 실행시간의 문제가 있음...
    #잘 생각해보면 큰 숫자를 만들기 위한 법칙은 맨 앞의 숫자가 큰 숫자여야 함.
    # 1. 0~k까지에서 가장 큰수를 뺴고 그 뒤에는 
    #10번 케이스가 런타임 에러도 아니고 시간초과가 난 이유는?? 
#10번만 시간 초과나는데 이유를 찾아서 고쳐 보자.
    start=0
    while True:
        length=k+1
        if k==0 or start+length>len(number):
            answer+=number[start:]
            break
            
        standard=max(number[start:start+length])
        

        
        for i in range(start,len(number)): #아 문제는 루프를 도는거 때문이었다...
            if number[i]==standard:
                answer+=number[i]
                start=i+1
                break
            k-=1
            
        if len(set(number[start:len(number)]))==1: # 값이 같을 때의 상황을 고려함.
            start+=k
            answer+=number[start:]
            break            

    
    return answer