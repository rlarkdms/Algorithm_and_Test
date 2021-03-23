def solution(s):
    answer = []
    count=0
    number=0
    zero_num=0
    while True:
        if count==1:
            break
        count=0
        for i in s:
            if i=='1':
                count+=1#0제거 후 길이
            else:
                zero_num+=1#제거할 0의 개수          
        a=bin(count)#이진 변환
        s=a[2:]#이진 변환 할때 앞에 0b~~~이래서 앞에 두개를 제외하기.
        number+=1#회차를 세기.
    answer.append(number)
    answer.append(zero_num)
    
    return answer