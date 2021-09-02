def solution(s):
    if len(s)==1:#문자열의 길이가 1일때는 무조건 return 1
        return 1

    if len(s)==2:#문자열의 길이가 2일때는 둘이 같으면 return 2 다르면 1
        if s[0]==s[1]:
            return 2
        else:
            return 1

    odd_value=odd(s)
    even_value=even(s)
    
    if odd_value>=even_value:#둘 중에 큰 놈 고르기
        return odd_value
    else:
        return even_value

def odd(word):#홀수개의 답을 고를 때 사용.
    standard=2
    best_sum=0
    for i in range(1,len(word)-1):
        sum=1
        if i<(len(word)//2):
            
            for j in range(1,standard):
                if word[i-j]==word[i+j]:
                    sum+=2
                else:
                    break   
            standard+=1
        else:    
            #standard-=1
            #print(standard)
            if len(word)%2==0:#여기 왜 이러는지 모르겠는데 특이 조건이 있음... 길이가 짝수면 일찍히 standard-=1를 해야 함
                standard-=1   
            for j in range(1,standard):
                if word[i-j]==word[i+j]:#하나씩 비교
                    sum+=2
                else:#만약 안맞으면 바로 break로 나오고
                    break
            if len(word)%2==1:# 길이가 홀수면 Standard-=1를 뒤에 해야 함.
                standard-=1
            #print(sum)
        best_sum=max(best_sum,sum)
    return best_sum

def even(word):#짝수개의 답을 고를 때 사용.
    standard=1
    best_sum=0
    for i in range(1,len(word)):
        sum=0
        if i <=(len(word)//2)-1:
            for j in range(0,standard):
                if word[i-j-1]==word[i+j]:
                    sum+=2
                else:
                    break  
            standard+=1
        else:  
            for j in range(0,standard):
                if word[i-j-1]==word[i+j]:
                    sum+=2
                else:
                    break#다르면 그냥 루프 빠져나오기
            standard-=1
        best_sum=max(best_sum,sum)
    return best_sum
