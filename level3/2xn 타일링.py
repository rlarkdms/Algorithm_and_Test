def solution(n):
    arr=[0,1,2]
    for i in range(3,n+1):
        arr.append((arr[i-1]+arr[i-2])%1000000007)#여기서 알게된 신기한 사실 연산의 수가 크면 속도가 느려지니 합할때마다 나머지로 나눠줘라
        
    return arr[n]%1000000007