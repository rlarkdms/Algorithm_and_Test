def solution(numbers):
    answer = 0
    arr=[0]*10
    
    for i in numbers:
        arr[i]+=1
        
    for j in range(len(arr)):
        if arr[j]==0:
            answer+=j
    
    return answer