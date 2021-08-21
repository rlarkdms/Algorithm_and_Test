#??이게 뭔말인지 이해를 못하겠는데...? 
#X보다 크고 x와 1~2개 다른 수들 중 제일 작은 수...
#문제가 되게 특이하네...
#도저히 뭔 기준인지를 모르겠는데....???
#와 질문하기 보고 알았네 규칙을....
import string
tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]
def solution(numbers):
    answer = []
    
    for i in numbers:
        if i%2==0:#짝수의 경우는 그냥 +1이고
            answer.append(i+1)
        else:#홀수의 경우는 두가지로 나눠진다.
            answer.append(get_answer(i))
    
    return answer

def get_answer(number):
    standard=convert(number,2)
    num=0
    for i in range(len(standard)-1,-1,-1):
        if standard[i]=='0':#뒤에서부터 1의 개수만큼 2의 제곱을 더하는 것이다. 근데 여기서 01으로 된거는 제외 이유는 11로 끝난것도 보면 4를 곱하는게 아니라 2를 곱하는 것이기 떄문에
            if num>0:
                num-=1
            return number+(2**num) 
        else:
            num+=1
    else:#마지막에 처음에 0이 없는 경우를 고려하여 설계.
        num-=1
        return number+(2**num)
    
