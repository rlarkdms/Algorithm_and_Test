def solution(n, arr1, arr2):
    answer = [""]*n
    a1=[[0]*n for _ in range(n)]#이중배열 선언 다 0으로 set.
    a2=[[0]*n for _ in range(n)]
    
    for i in range(n):
        k=n
        s=n
        while k>=0: 
            if arr1[i]>=2**k:#앞에서 부터 돌리는데 2의 k승이 그 숫자보다 작으면 뺴고 뺴고 돌려서 결국 저 이중배열에서 받는다 
                arr1[i]=arr1[i]-2**k
                a1[i][n-k-1]=1
            k-=1
        while s>=0: 
            if arr2[i]>=2**s:
                arr2[i]=arr2[i]-2**s
                a2[i][n-s-1]=1
            s-=1
            
    for i in range(n):
        for j in range(n):
            if a1[i][j]==1 or a2[i][j]==1:
                answer[i]=answer[i]+'#'#돌면서 True가 된 부분은 #로 가져다 넣기
            else:
                answer[i]=answer[i]+' '#False가 된 부분은 공백으로 가져다 넣기 
    
    return answer