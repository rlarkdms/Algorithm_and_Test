def solution(A, B):#그 유명한 야구게임?
    answer = 0
    # A팀에 대전 순서가 주어질 때 가장 적합한 B의 순서는?
    A.sort()
    B.sort()
    length=len(A)
    standard=0
    for i in range(length):#이게 차분히 올라가는 것.
        for j in range(standard,length):
            standard+=1
            if A[i]<B[j]:
                answer+=1
                break

    return answer