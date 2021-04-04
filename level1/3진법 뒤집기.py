import string

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :#n진법 10진법으로 바꾸는 법.
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

def solution(n):
    answer = 0
    val=convert(n,3)
    sum=0
    doubleval=0
    val=list(val)

    three=""

    for i in range(len(val)-1,-1,-1):#앞뒤 반전으로 바꾸는 법.
        three=three+val[i]
    

    three=list(str(int(three)))
    
    for k in range(len(three)-1,-1,-1):#앞뒤 반전한 3진법을 10진법으로 변환하기.
        sum=sum+int(three[k])*3**doubleval
        doubleval+=1

    return sum