def solution(land):
    #DP 문제라서
    for i in range(1,len(land)):#걔중 제일 작은 값을 골라서 계속 더하기
        land[i][0]+=max(land[i-1][1],land[i-1][2],land[i-1][3])
        land[i][1]+=max(land[i-1][0],land[i-1][2],land[i-1][3])
        land[i][2]+=max(land[i-1][0],land[i-1][1],land[i-1][3])
        land[i][3]+=max(land[i-1][1],land[i-1][2],land[i-1][0])    
    
    return max(land[len(land)-1])#마지막까지 더한값에서 max을 구하기.