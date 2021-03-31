def solution(n):
    a=[]
    for i in range(1,n+1):
        if n%i==0:#나눠지는 것 
            a.append(i)#a배열에 넣고
    
    return sum(a)#a 배열의 합