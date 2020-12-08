def solution(n):
    
    com1=0
    count=bin(n)
    count=count[2:len(count)]
    for i in count:
        if i=='1':
            com1+=1
#기준이 되는 이진수 중 1의 개수
    
    while True:
        count=''
        com2=0
        n=n+1
        count=bin(n)#이걸 출력하면 ob이진수로 나옴
        count=count[2:len(count)]#그래서 앞에 ob을 뺴고
        for i in count:#그 중에 계속 돌다가
            if i=='1':#1의 개수를 세서
                com2+=1
        
        if com2==com1:#만약 기준 com1 과com2이 같으면 n return
            return n