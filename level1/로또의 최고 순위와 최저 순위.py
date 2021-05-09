def solution(lottos, win_nums):
    answer = []
    numA=0#가장 많이 일치하는 것.
    numB=0#가장 적게 일치하는 것.
    d={6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    
    for i in range(0,len(lottos)):
        for j in range(0,len(win_nums)):
            if lottos[i]==0:
                numA+=1
                break
            if lottos[i]==win_nums[j]:
                numA+=1
                numB+=1
                break
    
    for key,value in d.items():
        if numA==key:
            answer.append(value)
        if numB==key:
            answer.append(value)
    
    return answer