def solution(arr):
    arr.sort()#일단 sort 해두고 
    rep=1#해당 숫자를 기준으로 최소공배수를 계산 해나가는 것.
    for i in arr:
        repA=1
        repB=1
        while True:
            if rep*repA==i*repB:#만약 같으면 
                rep=rep*repA#그 값을 최소공배수로 정하고 
                break#break
            elif rep*repA>i*repB:#만약 큰값이 있으면 나머지의 값에 곱하기하는 값을+1
                repB+=1
            elif rep*repA<i*repB:
                repA+=1 
    return rep