def solution(new_id):#개쌉노가다로 품.
    answer = ''
    stand=False
    new_id=list(new_id)
    new_id1=[]
    new_id2=[]
    new_id3=""
    for i in range(0,len(new_id)):
        if new_id[i].isupper():#1단계 조건
            new_id[i]=new_id[i].lower()
    
    for i in range(0,len(new_id)):#2단계 조건
        if new_id[i].islower() or new_id[i].isdigit() or new_id[i]=='-' or new_id[i]=='_' or new_id[i]=='.':
            new_id1.append(new_id[i])

   
    for i in range(0,len(new_id1)):#3단계 조건
        if new_id1[i]=='.':
            if stand==True:
                pass
            else:
                new_id2.append(new_id1[i])
            stand=True
        else:
            new_id2.append(new_id1[i])
            stand=False 

    if new_id2[0]=='.' or new_id2[len(new_id2)-1]=='.':#4단계 조건
        if len(new_id2)==1:
            new_id2.pop()
        else:
            if new_id2[0]=='.':
                new_id2.pop(0)
            if new_id2[len(new_id2)-1]=='.':
                new_id2.pop()
    

    if len(new_id2)==0:#5단계 조건
        new_id2.append('a')

    
    if len(new_id2)>=16:#6~7단계 조건
        for k in range(0,15):
            if k==14:
                if new_id2[k]=='.':
                    break
                
            new_id3=new_id3+new_id2[k]
            
    elif len(new_id2)==2:
        new_id3=new_id3+new_id2[0]
        new_id3=new_id3+new_id2[1]
        new_id3=new_id3+new_id2[1]
    elif len(new_id2)==1:
        for j in range(0,3):
            new_id3=new_id3+new_id2[0]
    else:
        for k in range(0,len(new_id2)):
            new_id3=new_id3+new_id2[k]

    
    return new_id3