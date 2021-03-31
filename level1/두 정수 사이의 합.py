def solution(a, b):
    answer = 0
    temp=0
    #대소관계는 정해져있지 않습니다.
    if a>=b:
        temp=a
        a=b
        b=temp
    
    arr=list(range(a,b+1))
    #리스트 만들고 
    #합!
    answer=sum(arr)
    return answer