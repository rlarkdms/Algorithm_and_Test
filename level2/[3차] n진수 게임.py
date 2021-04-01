import string
#10진법 ->n 진법으로 바꾸는 법 인터넷에서 참조함.https://security-nanglam.tistory.com/508
tmp = string.digits+string.ascii_uppercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

def solution(n, t, m, p):
    arr=""
    sentence=""
    for i in range(0,m*t):#참가하는 사람*구할 사람의 수 만큼 돌아서 arr에 저장(사실 이렇게 하면 불필요한 정보가 많아지지만 안전하게 하기 위해서...)
        arr=arr+str(convert(i,n))#변환 한 것을 다 arr에 저장.

    #arr=list(arr)
    for i in range(0,len(arr)):
        if len(sentence)==t:
            break
        if i%m==p-1:#나눠서 해당 순서의 setence에 더하기.
            sentence+=arr[i]

    return sentence

