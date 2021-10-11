import itertools
def solution(expression):
    answer = 0
    number=[]
    sign=[]
    num=""
    for i in range(len(expression)):#숫자랑 등호 뽑는 구간.
        if expression[i].isdigit():
            num+=expression[i]
        else:
            number.append(num)
            num=""
            sign.append(expression[i])
    else:
        number.append(num)
    
    #일단 '*'할지 '+'할지 '-'할지 결정하는 문제 이 부분은 데이터가 많이 없기 때문에 이렇게 하는게 생각 시간을 줄임.
    arr=['*','+','-']
    arr_combin=list(itertools.permutations(arr,3))
    

    max_value=-1
    for i in arr_combin:# 계속 돌기.('+','-','*')
        number_copy=number.copy()
        sign_copy=sign.copy()
            
        for k in i:#('*') 이렇게 주는 거임.#아 곱하기가 연속일 수 가 있네...
            while True:
                number_replace=[]
                sign_replace=[]
            
                for index in range(len(sign_copy)):
                    if sign_copy[index]==k:#같은거면 
                        number_replace.append(str(eval(number_copy[index]+sign_copy[index]+number_copy[index+1])))
                        if index!=len(sign_copy)-1: #맨 마지막 sign_copy면,뒤에꺼 다 넣고
                            number_replace+=number_copy[index+2:]
                            sign_replace+=sign_copy[index+1:]
                        break
                    else:
                        number_replace.append(number_copy[index])
                        if index==len(sign_copy)-1:
                            number_replace.append(number_copy[index+1])
                        sign_replace.append(sign_copy[index])
                else:#하나도 걸리는게 없으면 이제 등호는 없다는 거니까 나가고
                    break
                
                number_copy=number_replace.copy()
                sign_copy=sign_replace.copy()
            if len(number_copy)==1:#가장 큰값 구하기.
                max_value=max(max_value,abs(int(number_copy[0])))
        

    return max_value