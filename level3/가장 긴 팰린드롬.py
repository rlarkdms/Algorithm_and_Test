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

def odd(word):#홀수
    standard=1
    arr=[]
    for i in range(1,len(word)-1):
        sum=1
        if i <=(len(word)//2)-1:
            standard+=1
            for j in range(1,standard):
                if word[i-j]==word[i+j]:
                    sum+=2
                else:
                    break   
        else:    
            for j in range(1,standard):
                if word[i-j]==word[i+j]:
                    sum+=2
                else:
                    break
            standard-=1
        arr.append(sum)  
    return max(arr)


def even(word):#짝수
    standard=1
    arr=[]
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
                    break
            standard-=1
        arr.append(sum)     
    
    return max(arr)