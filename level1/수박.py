def solution(n):
    answer = ''
    for i in range(n):
        if i%2==0:
            answer=answer+"수"//홀수면 '수' 
        else:
            answer=answer+"박"//짝수면 '박' 
    
    return answer