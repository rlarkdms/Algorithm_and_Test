def solution(progresses, speeds):
    answer = []
    day=[]
    for i in range(len(progresses)):#이부분은 걸리는 시간 계산해서 day배열에 넣어둠.
        count=0#이거 그 다음 i을 위해 존재
        while progresses[i]<100:#만약 100이 넘으면
            progresses[i]+=speeds[i]
            count+=1
        day.append(count)#count을 넣음
    

    day.append(9999)#이건 마지막 day의 else을 위해서 존재 
    king=day[0]
    evid=0
    for k in range(len(day)):
        print(king)
        if king>=day[k]:#이게 맞으면 계속 더하는 거고 
            
            evid+=1
        else:
            king=day[k]#그 다음으로 큰 숫자가 나오면 그 숫자로 대체
            answer.append(evid)
            evid=1
    
    return answer