def solution(s):
    answer = []
    tur=[]
    val=[]
    count=""
    for i in range(1,len(s)-1):#문자열을 배열화 하기 {{2},{2,1},{2,1,3},{2,1,3,4}}->[[2],[2,1],[2,1,3],[2,1,3,4]]
        if s[i]=="{":
            line=[]
        elif s[i]=="}":
            line.append(int(count))
            tur.append(line)
        elif s[i]==",":
            if s[i-1]!="}":#원소들 나열하는 안이 아니라 [2,1,3]이게 아니라 [2,1,3],<-요 쉼표일때 line에다 append 
                line.append(int(count))
            count=""
        else:
            count=count+s[i]
            
    tur.sort(key=lambda x:len(x))#배열 크기대로 정렬

    for i in tur:
        ss=list(set(i)-set(val))#뒤 배열에서 앞 배열 뺴서 나온 원소를 answer에 집어넣기.
        val.append(ss[0])
        answer.append(ss[0])
    return answer