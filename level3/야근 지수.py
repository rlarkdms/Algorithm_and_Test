#Ex) [4,4,4,3,2] n이 7 일 때
#Ex) 처음 값을 빼기 [3,4,4,3,2] 이러면 뒤에 값이 더 커지니까 움직여서 또 뺴주기
#Ex) [3,3,3,3,2] 이렇게 되면 다시 0부터 가기 현재 n이 4
#Ex) [2,2,2,2,2] ->이렇게 되면 n이 0이되고 이게 답이 된다.
#Ex) 그리고 이 문제에서 함정은 아무리 n이 커도 야근지수는 마이너스가 아니라 0이라는거.

def solution(n, works):
    answer = 0
    works.sort(reverse=True)
    i=0
    #works가 하나인 경우
    works.append(-987654321)#이게 있는 이유는 뒤랑 비교하기 위해서
    while True:#가장 큰거랑 그 뒷의 값과 값이 다 같아지면 다시 큰값부터 다시 하나하나씩 줄여나가기.  
        if n==0:#그래서 만약 시간이 다 없어지면 break
            break
        works[i]=works[i]-1#이게 큰값이랑 그 뒤 값이랑 비교하는것
        n=n-1
        if works[i]<works[i+1]:#works가 큰값이면 그 뒷값이 같은 경우밖에 없음 그래서 같으면 옮겨서 한번 계산해주는거임.
            i+=1
        else:
            i=0          
            
    for j in range(len(works)-1):
        if works[j]<0:#만약 음수가 있다는 건 야근을 다 깍았다는 얘기임.
            return 0
        
    for i in range(len(works)-1):
        answer+=works[i]**2
        
    return answer