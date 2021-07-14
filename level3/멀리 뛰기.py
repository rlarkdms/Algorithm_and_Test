def solution(n):#DP 문제임.
    arr=[1]*(n+2)
    arr[1]=1
    arr[2]=2
    
    for i in range(2,n+2): #점화식으로 풀 수 있는 문제임.
        arr[i]=(arr[i-1]+arr[i-2])%1234567
    
    return arr[n]