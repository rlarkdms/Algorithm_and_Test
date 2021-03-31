def solution(n):
    answer = 0
    a=[0]*(n+1)

    for i in range(2,n+1):#2부터 도는데
        if a[i]==0:
            k=2
            while(n+1>(k*i)):#0인것중에 자기 배수인건 다 1로 만들어버리기
                a[i*k]=1
                k+=1

    return a.count(0)-2