def solution(n):
    
    arr=[]
    arr.append(0)
    arr.append(1)
    
    for i in range(2,n+1):
        arr.append(arr[i-2]+arr[i-1])#돌아가면서 넣고
    
    return arr[n]%1234567#나머지 나누기 