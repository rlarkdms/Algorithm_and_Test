def solution(dartResult):
    answer = 0
    status=''
    score=[]
    bouns=[]
    value=[0]*3
    option=[1]*3
    for i in range(len(dartResult)):#여기는 문자열 나눠서 각각 score,bouns,option에 넣는 곳.
        if dartResult[i].isdigit():
            if status=='num':
                score.pop()
                score.append(int(dartResult[i-1:i+1]))#이렇게 한 이유가. 숫자 10를 위해서임.
            else:
                score.append(int(dartResult[i]))
            status='num'
        elif dartResult[i].isalpha():
            bouns.append(dartResult[i])
            status='alp'
        elif dartResult[i]=='*':
            option[len(bouns)-1]='*'
            status='*'
        elif dartResult[i]=='#':
            option[len(bouns)-1]='#'
            status='#'
            
    for k in range(0,3):#여기는 배열에 넣은 값들은 연산하는 곳.
        if bouns[k]=='S':
            value[k]=score[k]**1
        elif bouns[k]=='D':
            value[k]=score[k]**2
        elif bouns[k]=='T':
            value[k]=score[k]**3
        
        if option[k]=='*':
            if k==0:
                value[k]*=2
            else:
                value[k]*=2
                value[k-1]*=2
        elif option[k]=='#':
            value[k]*=-1
        
  
    return sum(value)