import itertools
def solution(orders, course):
    #배열의 크기가 생각보다 크지 않음. 다 도는게 맞다고 생각.
    answer = []
    d={}    
    order=[]
    standard=[0]*11
    
    for i in orders:#주어진 부분을 다 정렬하는 것. ["AVD","ED"]->["ADV","DE"]
        i=list(i)  
        setence=""# 값 리셋
        i.sort()# 값을 정렬하기 위해서 배열에 모아서 정렬하고
        for j in i:
            setence+=j#str로 만들어서 
        order.append(setence)

    for i in order:
        for j in course:
            nCr = list(map(''.join ,itertools.combinations(i, j)))#조합을 통해 dict 생성.
            for k in nCr:
                if k in d.keys():#만약 이전에 있던 값이 있으면+1
                    d[k]=d[k]+1
                else:#없으면 dict에 추가하고 1로 세팅.
                    d[k]=1
                    
    res=sorted(d.items(),key=(lambda x:x[1]),reverse=True)#크기 순서대로 정렬. 5, 4, 3 ,2 ,1 ....
    
    for i in res:#찾고로 여기서 i[1]은 dict의 value의 값을 말함.
        if i[1]==1:#이게 어떤 메뉴든 2이상이 아니면 추가 못함.조건에 보면 있음.
            break
        if standard[len(i[0])]<=i[1]:#standard라는 배열이 있는데 course별로 가장 큰 값을 가지는 keys를 찾아서 answer에 넣어둠.
            standard[len(i[0])]=i[1]#기준 값을 변경 
            answer.append(i[0])    
      
    answer.sort()# sort!!
    
    return answer