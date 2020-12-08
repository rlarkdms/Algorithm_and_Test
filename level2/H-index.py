def solution(citations):
    citations.sort(reverse=True)
    
    for j in citations:
        sum=0
        for i in range(0,citations.index(j)):# 0부터 그 숫자까지 계속 돌다가 중간에 저 조건에 합당한 경우가 나타나면
            if citations[i]>=j:
                sum+=1# 플러스 1함
        else:
            if sum>=j:#그리고 다 돈다음에 저 sum하고 배열에 값(J)랑 비교해서 sum이 같은경우(보통은 다 같은 경우임) 아니면 큰 경우일 떄
                break #브레이크
    else:#그리고 만약 중간에 안멈추고 끝까지 다 가는 경우가있는데 그럴 경우는 +1 이부분이 이해가 안감 
        sum+=1
    
    return sum