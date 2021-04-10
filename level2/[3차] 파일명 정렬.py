def solution(files):
    answer = []
    d={}
    other={}
    standard=[]#기준이 될만한 배열
    for i in files:#골라내는 과정임.
        num=""
        truth=False
        setence=""
        for j in i:#각각의 문자열에서 HEAD와 NUMBER을 골라내는 과정.
            if j.isdigit()==True:#NUMBER을 골라내는 부분.
                truth=True
                num+=j
            else:
                if truth==True:#만약 NUMBER와 HEAD 다 골라내면 break문! 근데 여기서 중요한건 여기부분은 TAIL에 문자 하나라도 있을때 가정.
                    d[i]=[int(num),setence.lower()]
                    standard.append(setence.lower())#stand가 중요한데 HEAD값이 들어있음
                    break
                else:
                    setence+=j
        else:#TAIL에 아무것도 없을경우에 NUMBER와 HEAD에의 값을 딕셔너리에 넣는 부분 {foo9:['foo',9]}
            d[i]=[int(num),setence.lower()]
            standard.append(setence.lower())
                
            
    redict=sorted(d.items(), key=lambda x : x[1][1])#딕셔너리 정렬
    standard=list(set(standard))#standard 중복 없애기
    standard.sort()#정렬

    for i in standard:#중복이 없는 정렬된 HEAD값을 돌면서
        for k in redict:
            if k[1][1]==i:#만약 HEAD값이 일치하는 것을 찾으면
                other[k[0]]=k[1][0]#딕셔너리에 저장.

        othr=sorted(other.items(), key=lambda x:x[1])#딕셔너리에 저장된것 끼리 NUMBER로 다시 정렬
        for s in othr:
            answer.append(s[0])#그걸 answer에 append 
        other.clear()#값을 다시받기 위해 clear
    
    return answer