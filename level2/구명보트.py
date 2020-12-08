def solution(people, limit):
    answer = 0
    #켓츄크래용 캣츄 그래용 와이 쏘 시리어스~~~오 GD무대나 한번 더 봐야지~_~
    #240 이하 
    people.sort()
    count=0
    #최대 두명만 가능함
    #내가 보니까 앞에서 하나 뒤에서 하나 찾아서  둘이 더해서 없애고 남는거끼리 짝찾기해야함.
    while len(people)!=0:
            
        for i in range(len(people)-1,0,-1):
            if people[0]+people[i]<=limit:
                people.pop(i)
                people.pop(0)
                answer+=1
                break
                
        else:#내가 보니까 이부분 떄문에 시간오류나는 것 같은데...
            people.pop(0)
            answer+=1
            
    return answer