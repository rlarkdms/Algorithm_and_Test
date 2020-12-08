def solution(n,a,b):
    answer = 0
    
    while True:
        if a==b:
            return answer
        
        a=(a//2)+(a%2) 
        b=(b//2)+(b%2) 
        answer+=1