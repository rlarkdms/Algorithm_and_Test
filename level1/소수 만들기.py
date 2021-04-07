from itertools import combinations
def solution(nums):
    answer =0   

    prime=[0]*6002
    
    for i in range(2,3001):#이게 에라토스테네스의 체로 소수 구하기 아니 이거 말도 어려워 하지만 이게 소수구하기 방법중 가장 효율성이 좋은것.
        k=0
        if prime[i]==0:
            while k<=3002:
                k=k+i
                prime[k]=1
            prime[i]=0

    
    arr=list(combinations(nums, 3))#3개로 조합.
    for k in arr:
        if prime[sum(k)]==0:
            answer+=1
    return answer