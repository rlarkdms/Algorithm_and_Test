def solution(s):
    stack=[]
    number=[]
    compare=[]
    count=1
    standard=0
    sum=0
    stand=False
    if len(s)==1:
        return 1
    for i in range(1,int(len(s)/2)+1):
        standard=0#기준점 하나 설정. 밑에 3개 다 기준 값을 초기화하기 위해서 존재. standard,stack,compare 3개 다
        stack.clear()
        compare.clear()
        #만약 처음에 stack 배열안에 값이 없으면 기준이 되는 값을 넣기 위해 설정
        for j in range(standard,standard+i):
            stack.append(s[j])
        standard+=i
        while True:# 일단 계속 돌기.
            if standard+i>len(s):# 맨 마지막까지 닿으면 break
                    break
            #이부분은 비교배열 넣는 부분.
            for k in range(standard,standard+i):
                compare.append(s[k])
            standard+=i
            
            # #확인하는 부분.
            if stack==compare:#만약 비교 배열이 같으면 숫자가 하나 커지고->그 앞에 압축부분의 숫자가 1개씩 커지기.
                count+=1
                stand=True
                if standard==len(s):
                    sum=sum+len(str(count))+i
                    print("1똑같아서 더한값 %d %d count 값 %d" %(sum,standard,count))
            else:
                if stand==True:
                    sum=sum+len(str(count))+i
                    print("2똑같아서 더한값 %d %d count 값 %d" %(sum,standard,count))
                else:
                    sum=sum+i
                    print("현재 sum의 값%d" %sum)
                if standard==len(s):
                    sum=sum+i
                stand=False
                count=1
                stack.clear()
                stack=compare.copy()#아니라고 하면 그다음 배열을 넣으려고하는것.같지 않으게 나오면 바로 stack랑 compare
            #그니까 바뀔떄 바뀌어야함.
            #이제부터 여기서 처리해주고싶은건 그 뒤에서 끝에 안닫는 부분까지 더해야함.
            #이게 문제가 중간에 이걸 sum할수도 마지막에 sum 할수도 있다는 점?
            compare.clear()
        if len(s)==standard:
            pass
        else:
            if stand==True:
                sum=sum+len(str(count))+i
                print("3똑같아서 더한값 %d %d number %d" %(sum,standard,count))
                sum=sum+(len(s)-standard)
            else:
                sum=sum+(len(s)-standard)+i
        print(sum)
        number.append(sum)
        sum=0
        stand=False
        count=1
    
    return min(number)