def solution(arr):
    answer = []
    mi=min(arr)#가장 작은 값 고르기 
    print(mi)
    
    arr.remove(mi)#가장 작은 값 가진 것 없애기
    
    for i in range(len(arr)):#그 나머지는 넣기 
        answer.append(arr[i])
    
    if len(arr)==0:#만약 배열길이가 0이면 
        answer.append(-1)#-1 넣기 
    
    return answer