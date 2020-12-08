import math

def solution(n, words):
    answer = []
    ans=[]
    
    answer.append(words[0])#여기서 word의 첫번째 단어를 answer에 넣음.
    for i in range(1,len(words)):#word의 단어수 만큼 루프를 돌음.
    #이 루프를 도는건 영어끝말잊기가 틀리나 안틀리나를 확인하기 위해서임.    
        
        for j in range(len(answer)):#answer의 숫자만큼 루프를 돌음.
            if words[i]==answer[j]:#여기서 answer랑 word랑 같으면
                if (i+1)%n==0:
                    ans.append(n)
                else:
                    ans.append((i+1)%n)#계속 나눠서 나머지가 앞에 넣기
                ans.append(math.ceil((i+1)/n))#사람 수만큼 나눠서 넣기
                
                return ans
        answer.append(words[i])# 끝말잊기 중복 하기 위해서 넣기
                
        if words[i-1][len(words[i-1])-1]!=words[i][0]:#끝말잊기가 안맞으면
            if (i+1)%n==0:
                ans.append(n)
            else:
                ans.append((i+1)%n)
            ans.append(math.ceil((i+1)/n))
                
            return ans
        
    else:# 중복이랑 끝말잊기가 다 맞으면 0,0 넣기.
        ans.append(0)
        ans.append(0)
        return ans