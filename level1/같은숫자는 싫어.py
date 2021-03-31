def solution(arr):
    answer = []
    
    cnt=-3456#그냥 아무거나 넣어두고
    
    for i in range(len(arr)):#돌면서 
        if cnt!=arr[i]:#앞에꺼랑 값다르면 배열에 넣기 
            cnt=arr[i]
            answer.append(arr[i])
    
    
    return answer