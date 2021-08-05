#이문제는 사실 자리수가 핵심인데...
#예외적인 경우가 있음 383 38 ->38/383 
# 838 83 -> 838/83 #이 부분에서 알듯이 앞 숫자보다 뒷 숫자가 작은것과 큰것에 대한 순서 차이가 있음.
#아니 10000자리까지
#이 문제 예외적인 사항이 너무 많고 제한사항이 잘못되어 있음...
def solution(numbers):
    answer = ''
    end=''
    if len(set(numbers))==1 and numbers[0]==0:# 얘도 예외적인 사항이라 따로 뺴두기....
        return "0"
        
    length=len(str(max(numbers)))
    
    #10000이랑 0이 예외적인 사항이라서 그냥 빼두기
    numbers.sort()
    for i in range(numbers.count(10000)):
        end+=str(numbers.pop())
    
    numbers.sort(reverse=True)
    for i in range(numbers.count(0)):
        end+=str(numbers.pop())
    
    #아 생각해보니 딕셔너리는 같은 값은 안들어간다....아 그렇다면 이중 배열로 간다.
    dict=[]
    for i in numbers:
        rep=str(i)
        sub_len=length-len(str(i))
        if length==3:#3일때
            # 아 또 depth가 엉망인 코드를 만들어 버렸어....흙...
            if sub_len==1:
                if str(i)[0]>=str(i)[1]:
                    rep+=str(i)[0]
                else:
                    rep+=str(int(str(i)[0])+1)#아 이거 문제였구나....
            else:
                for j in range(sub_len):
                    rep+=str(i)[0]
        elif length==4:#길이가 1000자리일때
            if sub_len==1:
                #print(i)
                if str(i)[0]>=str(i)[1] or str(i)[0]>=str(i)[2]:#앞자리가 뒤에 자리수의 숫자보다 클때는 그냥 더하기
                    rep+=str(i)[0]
                else:#만약 뒤에 나오는 숫자가 더 크면
                    rep+=str(int(str(i)[0])+1)#0번째 숫자에+1하기
                    
            elif sub_len==2:#1번째 보다 0번째가 더 크면 맨 뒤에 +1해서 붙이기.  
                if str(i)[0]>=str(i)[1]:
                    rep+=str(i)[0]+str(i)[0]
                else:
                    rep+=str(i)[0]+str(int(str(i)[0])+1)
            else:#여기도 그냥 3개면 그냥 뒤에 똑같은거 붙이는게 최고임
                for j in range(sub_len):
                    rep+=str(i)[0]
                          
        else:
            for j in range(sub_len):#숫자가 하나밖에 없거나 max의 길이 만큼 있으면 이대로 진행.
                rep+=str(i)[0]
            
        dict.append([i,rep])#결과값 다 넣기
    dict_sort=list(sorted(dict, key=lambda x:(x[1],x[0]), reverse=True))#정리된 값으로 한번 정렬하고 그 다음에 정렬 다시하기.

    for i in dict_sort:
        answer+=str(i[0])

    answer=answer+end#예외적인 부분 붙이기.
    
    return answer