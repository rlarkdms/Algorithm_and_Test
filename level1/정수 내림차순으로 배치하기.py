def solution(n):
    answer = 0
    a=str(n)
    arr=[]
    string=""
    
    for i in range(len(a)):#여기안에 다 배열에 넣고
        arr.append(a[i])
    
    arr.sort(reverse=True)#그 배열 내림차순으로 배치하고
    
    for j in range(len(a)):#다시 붙여서 int로 바꾸기
        string+=arr[j]
    answer=int(string)
    
    return answer