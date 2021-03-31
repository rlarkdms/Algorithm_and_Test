def solution(n):
    answer = 0
    a=str(n)#string으로 a로 만들고
    
    for i in range(len(a)):#a배열에서 하나하나 뜯어놓고 다 더하기 
        answer+=int(a[i])
    
    return answer