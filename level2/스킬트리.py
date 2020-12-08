def solution(skill, skill_trees):
    answer = 0
    count=[29]*len(skill)#29로 설정한 이유는 가장 큰 값이 26이기 때문임.
    
    for i in skill_trees:#이러면 행으로 나옴"BACDE" 이런식으로
        for k in range(len(skill)):#CBD
            for j in range(len(i)):#행에 나왔던 문자 배열로 보여줌['B','A','C','D','E']
                if skill[k]==i[j]:#만약 같은게 있으면 
                    count[k]=j# 같았던거에 배열의 index을 count배열에 그 자리에 저장 예를 들면 C의 자리가 3번쨰였다 하면 count 0번 배열에 값은 3임 

        for s in range(len(count)-1):
            if count[s]>count[s+1]:#이걸 뒤에 원소가 값이 작으면 break
                break
            
        else:
            answer+=1#위에 for문을 다 돌고도 OK이면 이건 맞는거임 
            
        count=[29]*len(skill)#29로 다시 초기화
  
    return answer