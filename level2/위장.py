def solution(clothes):

    #clothes는 ["의상의 이름", "의상의 종류"]임 
    #의상 개수 1~30개
    #스파이는 최소한 하루에 한개의 의상갈아입음.
    a=[]
    b=[]
                   
        #01은 첫번째 카드의 갯수
    
    a.append(clothes[0][1])#옷 종류 하나 더 해놓고
    b.append(1)#숫자 하나 더해 놓고
    for i in range(1,len(clothes)): 
        for j in range(len(a)):#도는데
            if a[j]==clothes[i][1]:#만약 같은 종류의 옷이면 
                b[j]+=1#더하기 1
                break
        else:#다른 종류의 의상이면 그 의상을 a 배열에 넣고 그 의상의 맞는 갯수도 1 ㅊ추가
            a.append(clothes[i][1])
            b.append(1)
    
    #이제 다걸러냈으니 조합만 하면 됨.
    
    answer=1
    for i in range (len(b)):#조합을 하는데 여기서 중요한건! 밑에서
        answer=answer*(b[i]+1)
        
    answer=answer-1
    return answer