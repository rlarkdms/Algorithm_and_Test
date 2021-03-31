def solution(n):
    answer = []
    a=str(n)#n을 string으로 만들어 a에 넣고
    
    for i in range(len(a)-1,-1,-1):#배열 뒤집어서 int형으로 answer에 넣기
        answer.append(int(a[i]))
     
    return answer