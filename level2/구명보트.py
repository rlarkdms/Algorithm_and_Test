def solution(people, limit):
    answer = 0
    people.sort()
    if len(people)==1:#1은 웬만하면 다 예외처리식으로 하는게 좋음.
        return 1
    first=0
    last=len(people)-1
    
    while True:
        if last==first:#이 경우는 2번 케이스일때만 적용되는 경우 왜 1를 더하냐면 앞에 있던 나머지 하나도 결국은 더하는게 맞으니까.
            answer+=1
            break
        if last<first:#아래의 앞뒤로 한 경우라 끝난거고 1번 케이스일 때 적용되는 경우
            break
            
        if people[first]+people[last]<=limit:# 1번 케이스 2개를 보내는 방법으로 맨앞과 맨 뒤에서 하나씩 골라 보내기 
            answer+=1
            first+=1
            last-=1
        else:# 2번 케이스 가장 작은걸 보낼 수 없어서 맨 뒤에서 하나를 보내는 과정.
            last-=1
            answer+=1
    
    return answer