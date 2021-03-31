def solution(d, budget):
    answer = 0
    d.sort()#오름차순으로 정렬하고
    sum=0
    
    for i in d:
        sum+=i
        if budget<sum:#sum이 budget보다 크면 break
            break
        else:
            answer+=1 #그 전까지는 answer(지원해 주는 부서)을 하나 더하기
    return answer